import asyncio
from autogen_agentchat.ui import Console
from app.team import team

task = """
There is a folder DotNet8WebApiProject that is available one directory level higher, which contains a dotnet application.
Create a FastAPI template project and migrate the dotnet application to python.
"""

async def main():
    #user_input = input("Enter your task:")
    await Console(team.run_stream(task=task))

if __name__ == "__main__":
    asyncio.run(main())
