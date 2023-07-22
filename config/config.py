import os
import tempfile

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

OUTPUT_DIR = os.path.join(
    tempfile.gettempdir(),
    'rkk-document-gpt',
    'output'
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
