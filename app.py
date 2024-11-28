from fastapi import FastAPI, File, UploadFile, HTTPException
from utils.openai_integration import extract_document_details
import os
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.post("/extract-document-info")
async def extract_document_info(file_content: UploadFile = File(...)):
    try:
        # Load OpenAI API key from environment variables
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="OpenAI API key not found in environment variables.")

        # Read and encode the uploaded file
        contents = await file_content.read()
        base64_file_content = base64.b64encode(contents).decode('utf-8')

        # Extract document details based on schema
        document_info = extract_document_details(base64_file_content, api_key)
        return {"document_info": document_info}
    except Exception as e:
        print(f"Error extracting document information: {str(e)}")
        return {"document_info": {}}
