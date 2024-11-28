import base64
import json
import magic
from openai import OpenAI
from pathlib import Path

# Load schema from a JSON file
SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "required_details.json"

# You can replace 'required_details.json' with any other JSON schema file to extract data based on a different schema.
with open(SCHEMA_PATH, "r") as schema_file:
    invoice_schema = json.load(schema_file)

def extract_document_details(base64_file_content, api_key):
    try:
        file_content = base64.b64decode(base64_file_content)

        # Detect MIME type
        mime_type = magic.from_buffer(file_content, mime=True)
        if mime_type == "application/pdf":
            from .file_processing import convert_file_to_png
            png_content = convert_file_to_png(file_content)
            png_base64_content = base64.b64encode(png_content).decode("utf-8")
        else:
            png_base64_content = base64.b64encode(file_content).decode("utf-8")

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Extract relevant fields from the document and represent it as a JSON object based on the provided schema. Here is the schema: {json.dumps(invoice_schema)}",
                        },
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{png_base64_content}"}}  
                    ],
                }
            ],
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error in OpenAI integration: {str(e)}")
        return {}
