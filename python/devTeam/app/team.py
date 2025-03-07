from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from app.agents_file import custom_developer_agent, tester_agent, techlead_agent
from app.config import az_model_client

text_termination = TextMentionTermination("FINISH")

team = SelectorGroupChat(
    [custom_developer_agent, tester_agent, techlead_agent],
    model_client=az_model_client,
    termination_condition=text_termination
)
