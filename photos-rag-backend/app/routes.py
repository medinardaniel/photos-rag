# routes.py
from flask import Blueprint, request, jsonify
from .embed import BertEmbedder
from .read_db import ReadDB
from .generate_captions import generate_captions
from .generate_signed_url import get_signed_urls
from flask_cors import cross_origin

main = Blueprint('main', __name__)

@main.route('/get_images', methods=['POST'])
@cross_origin()
def get_images():
    """
    Return the image filenames and descriptions that are most similar to the user query.
    Input: query--The user query.
    Return: The top K similar images and their AI generated descriptions.
    """
    # get the user query and top K from the request
    data = request.get_json()
    user_query = data['query']
    # top_k = data['top_k']

    # ensure user_message is not empty
    if not user_query:
        return jsonify({'error': 'Empty query.'}), 400
    
    try:
        # embed the user query
        embedder = BertEmbedder()
        query_embedding = embedder.embed_query(user_query)

        # read the database and get top K similar images
        db = ReadDB()
        similar_image_descriptions = db.get_similar_image_descriptions(query_embedding)

        # generate responses to the image descriptions
        captions = generate_captions(similar_image_descriptions)

        # generate signed URLs for the images
        signed_urls = get_signed_urls(list(captions.keys()))
                                     
        # create the response combining captions and signed URLs
        response = {}
        for filename, caption in captions.items():
            signed_url = signed_urls[filename]
            response[signed_url] = caption

        # return the responses
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
