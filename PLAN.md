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

