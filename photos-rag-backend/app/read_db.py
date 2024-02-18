# read_db.py
# Description: This file contains the ReadDB class, which is used to read data from the MongoDB database.
import os
from pymongo import MongoClient
import numpy as np
import logging

class ReadDB:
    def __init__(self):
        self.uri = os.getenv('MONGODB_URI')
        self.client = None
        self.db_name = 'photo-rag-db'
        self.collection_emb_name = 'photo-embeddings'
        self.collection_desc_name = 'photo-descriptions'
        self._connect_to_db()

    def _connect_to_db(self):
        """Connect to the MongoDB client and set up the database and collections."""
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            self.collection_emb = self.db[self.collection_emb_name]
            self.collection_desc = self.db[self.collection_desc_name]
        except Exception as e:
            logging.error(f"An error occurred while connecting to MongoDB: {e}")
            raise

    @staticmethod
    def cosine_similarity(embedding1, embedding2):
        """
        Calculate the cosine similarity between two embeddings.
        Input: embedding1--The first embedding.
               embedding2--The second embedding.
        Return: The cosine similarity between the two embeddings.
        """
        dot_product = np.dot(embedding1, embedding2)
        magnitude1 = np.linalg.norm(embedding1)
        magnitude2 = np.linalg.norm(embedding2)
        similarity = dot_product / (magnitude1 * magnitude2)
        return similarity

    def find_similar_documents(self, query_embedding, top_k=5):
        """
        Find the top K similar documents to the query embedding.
        Input: query_embedding--The query embedding.
               top_k--The number of similar documents to return.
        Return: The top K similar documents.
        """
        similarities = []
        for document in self.collection_emb.find():
            db_vectors = np.array(document['embedding'])
            similarity = self.cosine_similarity(query_embedding, db_vectors)
            similarities.append((document['filename'], similarity))
        
        # Sort the results by similarity score in descending order
        similarities.sort(key=lambda x: x[1], reverse=True)
        # Return the top K similar documents
        return similarities[:top_k]

    def get_similar_image_descriptions(self, query_embedding, top_k=5):
        """
        Get the descriptions of the similar documents from the MongoDB collection.
        Input: similar_documents--The similar documents.
        Return: The descriptions of the similar documents.
        """
        try:
            similar_documents = self.find_similar_documents(query_embedding, top_k)
            descriptions = []
            for filename, _ in similar_documents:
                description_doc = self.collection_desc.find_one({'filename': filename})
                description = description_doc['description'] if description_doc else "No description found"
                descriptions.append((filename, description))
            return descriptions
        except Exception as e:
            logging.error(f"An error occurred while retrieving image descriptions: {e}")
            raise
