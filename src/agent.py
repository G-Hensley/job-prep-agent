# Agent Logic & Definitions
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

class JobPrepAgent:
    def __init__(self):
        self.options = ClaudeAgentOptions(
            system_prompt="You're an expert job preparation assistant. Help Gavin prepare for his job search by reviewing job descriptions and providing a selected resume from his list, write a cover letter if needed, and write a log",
            allowed_tools=["Read", "Glob", "Grep"]
        )