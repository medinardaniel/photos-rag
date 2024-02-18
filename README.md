# Daniel's Life: RAG-Powered Image Query Application

This application showcases an innovative approach to visualizing Daniel's life through images, combining advanced NLP and image processing techniques. Users can explore images related to Daniel's experiences by inputting descriptive queries. The application utilizes OpenAI's GPT-4 Vision model, BERT embeddings for semantic search, and MongoDB for data storage, offering a unique glimpse into Daniel's memorable moments.

## Workflow Overview

1. **Extract Text Data**: Images were imported from Daniel's local computer using the `extract_data.ipynb` notebook.
2. **Generate Descriptions**: The `generate_descriptions.ipynb` script utilizes OpenAI's 'gpt-4-vision-preview' model to generate comprehensive descriptions for each image, eliminating the need for data chunking.
3. **Database Storage**: MongoDB is employed to store image data efficiently. The 'photo-embeddings' collection holds the filename and corresponding embedding, while 'photo-descriptions' stores filenames alongside their descriptions. Additionally, images are securely stored in an AWS S3 bucket.
4. **Semantic Search Retrieval**: Utilizing BERT model embeddings for image descriptions, the application performs semantic searches. By computing the cosine similarity between the user's query embedding and all stored vector embeddings, the top 5 most similar image descriptions are identified and retrieved.
5. **Contextual Caption Generation**: Image descriptions are transformed into detailed captions through the OpenAI API by embedding them into an LLM prompt. These captions include nuanced details about the individuals present, their relationships, the location, and the event date, providing rich context to each image.

## Technologies Used

- **NLP Model**: BERT for semantic search; OpenAI's GPT-4 for vision-based descriptions
- **Database**: MongoDB for storing embeddings and descriptions; AWS S3 for image storage
- **Data Processing**: Python notebooks for data extraction and description generation
- **Backend**: Frameworks and languages utilized for the backend (e.g., Node.js/Express.js)
- **Frontend**: Technologies used for the frontend (e.g., React.js)

## Setup and Installation

Ensure you have Python, Node.js, MongoDB, and an AWS account configured for S3 storage before starting.

### Extracting and Processing Data

1. Run `extract_data.ipynb` to import images from Daniel's computer.
2. Use `generate_descriptions.ipynb` to generate image descriptions with GPT-4.

### Database and Storage Setup

1. Populate MongoDB collections: 'photo-embeddings' and 'photo-descriptions' with the output from the processing scripts.
2. Upload images to your AWS S3 bucket, noting their filenames.

### Running the Application

To run the backend, cd into photo-rag-frontend and run 'flask run' in the terminal.
To run the frontend, cd into photos-rag-frontend and run 'npm run build' followed by 'npm start' in the terminal.

## Usage

Input a descriptive query about Daniel's life to explore related images. The application processes your query, retrieves relevant images, and displays them with generated captions that enrich the visual experience.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

