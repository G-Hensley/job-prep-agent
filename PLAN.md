# Job Prep Agent Plan

## Objective
The objective of the Job Prep Agent is to assist users in preparing for job applications by choosing the best resume, writing cover letters, and suggesting improvements to the resume based on the job description shared by the user. It will also keep a log of all jobs the user has applied to, including the job title, company name, and application date. The log will also include what skills the user doesn't have - but are required for the job, and suggest ways to acquire those skills.

## Technical Details
- Built with Anthropic SDK (Python) — NOT Claude Code, not Conductor
- Uses tool use pattern: read_skills, read_experience, select_resume_variant, analyze_job_posting, generate_cover_letter
- Reads from my knowledge base JSON files directly
- Can optionally log the application to my applications.json via the MCP server

## What This Teaches
- Anthropic SDK tool use at the API level (the #1 interview question for AI Engineer roles)
- Multi-step agent orchestration without a framework
- Structured output parsing
- Python project structure (pyproject.toml, proper packaging)

## Steps to Implement
1. **Define the Agent**: Create a new agent class `JobPrepAgent` that uses the methods defined in the tools. This class will be responsible for orchestrating the entire job preparation process.
2. **Create Multiple Tools**: Implement the necessary tools for reading skills, experience, selecting resume variants, analyzing job postings, and generating cover letters.
3. **Implement Agent Logic**: In the agent's main method, orchestrate the use of the tools to achieve the objective. This will involve:
   - Reading the user's skills and experience from the knowledge base.
   - Analyzing the job posting to identify required skills and experience.
   - Selecting the best resume variant based on the job description.
   - Generating a tailored cover letter for the job application.
4. **Logging Applications**: Implement functionality to log the job applications to a JSON file, including the job title, company name, application date, missing skills, and suggestions for acquiring those skills.
5. **Testing**: Write tests to ensure that the agent and its tools are functioning correctly and that the logging is accurate.