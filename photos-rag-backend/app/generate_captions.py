from .config import Config
import openai as OpenAI
from .relationships import describe_relationships

def generate_single_caption(image_description):
    """
    Creates a context from the image_descriptions to be used as input to the OpenAI API.
    Input: image_descriptions--A list of image descriptions.
    Return: A string that is the context.
    """
    relationships = describe_relationships(image_description)
    
    prompt = ("Below is an image description that may contain the names of the people in the image ('People:'), "
              "the location, and the date the image was taken. Using this information, create a short caption "
              "based on the provided image context, names (if provided), date, and location, and relationships. "
              "Only include the names of the individuals present in the image. If there are no names in the "
              "description, do not include any names in the caption. "
              "Avoid starting with redundant phrases like \n'In this image,\n' focusing instead on "
              "directly diving into the narrative. Balance formal and casual language, capturing "
              "the atmosphere, actions, and overall vibe of the scene with assertiveness and confidence, "
              "while incorporating specific names, relationships and locations into cohesive narratives.\n"
              )
    
    context = prompt + relationships + "\n"

    # connect to openai
    client = OpenAI.Client(api_key=Config.OPENAI_API_KEY)

    try:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": image_description}
            ]
        )

        # Get the response from the completion
        response = completion.choices[0].message.content

        # Check if the reply is empty, indicating the question may be out of context
        if not response:
            response = "I am sorry, but I am not equipped to respond to that query."
    except Exception as e:
        print("Failed to generate response.")
        print(e)
    
    return response

def generate_captions(image_descriptions):
    """
    Generates a response to the image description using the OpenAI API.
    Input: image_descriptions-- a list of tuples containing the filename and the image description.
    Return: The response to the image description.
    """

    # for each image in image_descriptions, generate a description
    responses = {}
    for filename, description in image_descriptions:
        response = generate_single_caption(description)
        # append the filename and response to a list of tuples
        responses[filename] = response
    
    return responses

