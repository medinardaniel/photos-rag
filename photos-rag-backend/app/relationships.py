# relationships.py
# Description: This file contains the code to describe the relationships among the individuals in the image.

def describe_relationships(image_description):
    """
    Describes the relationships among the individuals in the image.
    Input: image_description--A string containing the image description.
    Return: A string that describes the relationships among the individuals in the image.
    """
    relationships = []
    
    # Married
    if "Juan" in image_description and "Graciela" in image_description:
        relationships.append("Juan and Graciela are married.")
    
    # Grandmother
    grandchildren = ["Daniel", "Pipe", "Santiago"]
    for grandchild in grandchildren:
        if "Kika" in image_description and grandchild in image_description:
            relationships.append(f"Kika is {grandchild}'s grandmother.")
    
    # Kika and Tia Angie are friends
    if "Kika" in image_description and "Tia Angie" in image_description:
        relationships.append("Kika and Tia Angie are friends.")
    
    # Kika is Tia Icha's mother
    if "Kika" in image_description and "Tia Icha" in image_description:
        relationships.append("Kika is Tia Icha's mother.")
    
    # Brothers
    brothers = ["Daniel", "Santiago", "Pipe"]
    for i, brother1 in enumerate(brothers):
        for brother2 in brothers[i+1:]:
            if brother1 in image_description and brother2 in image_description:
                relationships.append(f"{brother1} and {brother2} are brothers.")
    
    # Daniel's Friends
    daniels_friends = ["Julio", "Javier", "Will", "Pablo", "Azul", "Sri"]
    for friend in daniels_friends:
        if "Daniel" in image_description and friend in image_description:
            relationships.append(f"Daniel and {friend} are friends.")

    # General Friendship among Julio, Javier, Will, Pablo, Santiago, and Azul
    friends = ["Julio", "Javier", "Will", "Pablo", "Santiago", "Azul"]
    for i, friend1 in enumerate(friends):
        for friend2 in friends[i+1:]:
            if friend1 in image_description and friend2 in image_description:
                relationships.append(f"{friend1} and {friend2} are friends.")

    return " ".join(relationships)
