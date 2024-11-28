# Document Extraction

This project is designed to extract relevant information from documents such as invoices using OpenAI's GPT-4o model. It allows for structured data extraction based on predefined schemas, making it easy to extract specific data fields from documents. The application processes different types of documents like PDFs and images, and outputs the extracted data in a structured JSON format, which can be used in further applications.

The tool leverages the OpenAI API for processing the documents and extracting the structured data based on the schema provided. It includes support for file uploads, OpenAI integration, and custom schema handling, making it highly flexible and extendable for future use cases.

## Features

- **Document Upload**: Allows you to upload documents such as PDFs or images to extract information.
- **Schema-based Extraction**: Uses predefined JSON schemas to extract relevant data in a structured format.
- **OpenAI Integration**: Leverages OpenAI's GPT-4o to analyze the document and return structured JSON.
- **Extendable**: You can modify the schema to handle different document types like invoices, purchase orders, etc.
- **API Endpoint**: A FastAPI-based server for easy integration and interaction.

## Installation

### Prerequisites
- Python 3.x
- OpenAI API key
- Dependencies listed in `requirements.txt`

### Steps to Install

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/mohanmma/document-extraction.git
Navigate to Project Directory
Navigate into the cloned project directory:

cd document-extraction

Install Dependencies
Install the required dependencies using pip:
pip install -r requirements.txt

Set Up Environment Variables
Create a .env file in the root directory of the project. This file should contain the OpenAI API key. The contents of the .env file should look like:

OPENAI_API_KEY=your-api-key-here
Replace your-api-key-here with your actual OpenAI API key.

Running the Application
Run FastAPI Server
Use uvicorn to start the FastAPI server:
uvicorn app:app --reload
This will start the server locally at http://127.0.0.1:8000.


API Endpoint
POST /extract-invoice-info
This endpoint allows you to upload a document (PDF or image) and extract structured invoice information based on a predefined schema.

Request:
File: Upload a PDF or image file to be processed.
Example Request:


curl -X 'POST' \
  'http://127.0.0.1:8000/extract-invoice-info' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file_content=@yourfile.pdf'
