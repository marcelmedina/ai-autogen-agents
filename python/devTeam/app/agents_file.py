import asyncio
from autogen_agentchat.agents import AssistantAgent
from app.file_tools import file_tool, directory_write_tool, list_all_files, delete_file, read_file_tool
from app.config import az_model_client

tools = [file_tool, directory_write_tool, list_all_files]
super_tools = [file_tool, directory_write_tool, list_all_files, delete_file]

custom_developer_agent = AssistantAgent(
    name="developer",
    model_client=az_model_client,
    description="A software developer",
    system_message=
    """
    Your final answer must include the python code implementing the solution.
    You have access to tools which can read files, write files and create directories.
    """,
    tools=tools
)

tester_agent = AssistantAgent(
    name="tester",
    model_client=az_model_client,
    description="A test engineer",
    system_message=
    """
    You are a test engineer.
    Always write the test cases for the code implemented by the developer.
    You have access to tools which can read files, write files and create directories.
    """,
    tools=tools
)

techlead_agent = AssistantAgent(
    name="techlead",
    model_client=az_model_client,
    description="A technical lead",
    system_message=
    """
    You are a technical lead.
    You must challenge the code and provide constructive feedback according to the best practices.
    Be meticulous, don't allow multiple classes in a single file. Split them into separate files.
    Create markdown documentation.
    Create the requirements.txt with package dependencies.
    Delete files in the new directory that are not of any use. Never delete the source.
    If you are happy with the outcome, respond with 'FINISH' to terminate the conversation.
    """,
    tools=super_tools
)
