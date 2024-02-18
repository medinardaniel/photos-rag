# embed.py
# Description: This file contains the code to embed the user query using the BERT model.
from transformers import BertModel, BertTokenizer
import torch

class BertEmbedder:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def embed_query(self, query):
        """
        Embed the query using the BERT model.
        Input: query--The query to embed.
        Return: The embedded query.
        """
        # Tokenize the query
        tokenized_query = self.tokenizer(query, padding=True, truncation=True, return_tensors='pt')

        # Embed the query
        with torch.no_grad():
            outputs = self.model(**tokenized_query)
        
        # Extract the last hidden states
        last_hidden_states = outputs.last_hidden_state

        # Take the mean of the last hidden states
        mean_embedding = torch.mean(last_hidden_states, dim=1).tolist()[0]

        return mean_embedding
