# Document Data Extraction using OpenAI GPT-4o

This module is designed to extract structured data from various document types using OpenAI's GPT-4o model. The data extraction process is guided by a JSON schema, which specifies the fields to be extracted from the document.

## Features
- Supports different document formats (e.g., PDF, images).
- Customizable schemas to handle different document types (e.g., invoices, contracts, receipts).
- Automatically converts PDFs to images for processing.

---

## How to Add and Use Custom Schemas

The extraction logic is based on a JSON schema that defines the structure of the output. By default, the module uses the `required_details.json` schema, but you can add your own schemas to extract data from other types of documents.

### Steps to Add a New Schema

1. **Create the Schema File**:
   - Navigate to the `schemas` directory in your project.
   - Create a new JSON file for your schema. For example:
     ```
     schemas/
       - invoice_schema.json
       - receipt_schema.json
       - custom_schema.json
     ```

2. **Define the Schema**:
   - Write your JSON schema in the file. For example, a schema for a receipt might look like this:
     ```json
     {
       "$schema": "http://json-schema.org/draft-07/schema#",
       "title": "Receipt",
       "description": "A schema for extracting data from receipts.",
       "type": "object",
       "properties": {
         "storeName": { "type": "string" },
         "transactionDate": { "type": "string", "format": "date" },
         "totalAmount": { "type": "number" }
       },
       "required": ["storeName", "transactionDate", "totalAmount"]
     }
     ```

3. **Update the Code to Use Your Schema**:
   - Update the `SCHEMA_PATH` in the code to point to your new schema:
     ```python
     SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "receipt_schema.json"
     ```
   - Alternatively, dynamically pass the schema path if you want to handle multiple schemas in a single execution:
     ```python
     def extract_document_details(base64_file_content, api_key, schema_path):
         with open(schema_path, "r") as schema_file:
             document_schema = json.load(schema_file)
         # Use `document_schema` for processing...
     ```

4. **Run the Extraction**:
   - Call the function with the document you want to process. The output will be structured according to your schema.

---

## Example Usage

### Extracting Data Using a Custom Schema

```python
from document_extraction import extract_invoice_details

base64_document = "..."  # Base64-encoded document
api_key = "your_openai_api_key"
schema_path = "/path/to/your/custom_schema.json"

# Update the schema path dynamically
with open(schema_path, "r") as schema_file:
    custom_schema = json.load(schema_file)

result = extract_invoice_details(base64_document, api_key)
print(result)
