import os
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from pathlib import Path

def find_project_root():
    """Finds the root of the project (where .env exists) by walking up the directory tree."""
    current_dir = Path(os.getcwd()).resolve().parent  # Start from the script's directory
    while current_dir != current_dir.root:
        if (current_dir / ".env").exists():  # If .env is found, return the directory
            return current_dir
        current_dir = current_dir.parent  # Move up one level
    return None  # Return None if .env is not found

# Load environment variables from .env file
project_root = find_project_root()
load_dotenv(dotenv_path=project_root / ".env")

# Get environment variable
AZURE_AI_SERVICE_NAME = os.getenv("AZURE_AI_SERVICE_NAME")

# Create the token provider
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")

az_model_client = AzureOpenAIChatCompletionClient(
    azure_deployment="gpt-4o",
    api_version="2024-05-01-preview",
    model="gpt-4o",
    azure_endpoint=f"https://{AZURE_AI_SERVICE_NAME}.openai.azure.com/",
    azure_ad_token_provider=token_provider,
)
