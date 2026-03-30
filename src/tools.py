# Tools to allow the agent to look over files/directories and extract information from them
from claude_agent_sdk import Tool
import os

@Tool("read_skills", "Read users skills from the myself directory")
async def read_skills():
    return open("~/Desktop/Projects/code-projects/myself/profile/skills.json", "r").read()

@Tool("read_experience","Read users experience from the myself directory")
async def read_experience():
    return open("~/Desktop/Projects/code-projects/myself/profile/experience.json", "r").read()

@Tool("read_resume_variants", "Read users resume variants from the myself directory")
async def read_resume_variants():
    # The agent should read the names of the resume files before reading the contents of the files, so it can decide which resume to use based on the job description
    for file in os.listdir("~/Desktop/Projects/code-projects/myself/profile/resumes"):
        if file.endswith(".pdf"):
            return file