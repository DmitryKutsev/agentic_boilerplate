import os

import chromadb
from chromadb.utils.embedding_functions.openai_embedding_function import (
    OpenAIEmbeddingFunction,
)
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEXTS_PATH = os.getenv("TEXTS_PATH")


class ChromaDbCollection:
    def __init__(self, collection_name: str = "marcus_collection"):
        self.file_path = TEXTS_PATH if TEXTS_PATH else "marcus_quotes.txt"
        self.collection_name = collection_name
        self.marcus_quotes = []
        self.ids = []
        self.collection = None
        self._initialize()

    def __new__(cls, collection_name: str = "marcus_collection"):
        instance = super().__new__(cls)
        instance.__init__(collection_name)
        return instance.collection

    def _initialize(self):
        self._load_quotes()

        embedding_function = OpenAIEmbeddingFunction(
            api_key=OPENAI_API_KEY, model_name=EMBEDDING_MODEL
        )
        chroma_client = chromadb.Client()
        self.collection = chroma_client.create_collection(
            name=self.collection_name, embedding_function=embedding_function
        )
        self.collection.add(documents=self.marcus_quotes, ids=self.ids)

    def _load_quotes(self):
        with open(self.file_path, "r") as reader:
            self.marcus_quotes = reader.readlines()
        self.ids = [f"id{i+1}" for i in range(len(self.marcus_quotes))]


chroma_collection = ChromaDbCollection()
