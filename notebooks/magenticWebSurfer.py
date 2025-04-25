# Import required libraries
import os
import asyncio
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from pathlib import Path

# Get the absolute path to the .env file
env_path = Path(os.getcwd()).parent / ".env"

# Load the .env file
load_dotenv(dotenv_path=env_path)

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

surfer = MultimodalWebSurfer(
    "WebSurfer",
    model_client=az_model_client,
)

team = MagenticOneGroupChat([surfer], model_client=az_model_client)

# Run the task
asyncio.run(Console(team.run_stream(task="How full are the Auckland dam levels? (April, 2025)")))

# Note: you can also use other agents in the team
# team = MagenticOneGroupChat([surfer, file_surfer, coder, terminal], model_client=model_client)
# file_surfer = FileSurfer("FileSurfer", model_client=model_client)
# coder = MagenticOneCoderAgent("Coder", model_client=model_client)
# terminal = CodeExecutorAgent("ComputerTerminal", code_executor=LocalCommandLineCodeExecutor())
