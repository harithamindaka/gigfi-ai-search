from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents import SearchClient
from azure.search.documents.indexes.models import (
    ComplexField,
    SimpleField,
    SearchFieldDataType,
    SearchableField,
    SearchIndex,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch
)
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv
import json
from DTOs.Gig import GigDTO

load_dotenv()

class SearchService:
    def __init__(self):
        endpoint = os.getenv("AZ_SEARCH_ENDPOINT")
        index_name = os.getenv("AZ_SEARCH_INDEX_NAME")
        secret_key = os.getenv("AZ_SEARCH_KEY")
        self.semantic_config = os.getenv("AZ_SEARCH_SEMANTIC_CONFIG")

        credential = AzureKeyCredential(secret_key)
        self.search_client = SearchClient(endpoint=endpoint,index_name=index_name,credential=credential)

    def semanticSearch(self, search_text, count=10, select='*'):
        results =  self.search_client.search(query_type='semantic', semantic_configuration_name=self.semantic_config, search_text=search_text, select=select, top=count)
        return results

