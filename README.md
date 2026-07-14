🌟 GitHub Code Analysis Chrome Extension 🌟

The GitHub Code Analysis Chrome Extension is a powerful tool that enables users to easily retrieve GitHub repository URLs, analyze their code, and obtain detailed explanations for code snippets.

Powered by OpenAI’s GPT-4o-mini model and built using Python (Flask) with a Chrome Extension frontend, it provides developers with clear, AI-driven insights into repositories — especially useful when documentation is missing or incomplete.

Why This Project?

For many small or mid-sized repositories, finding proper documentation or a comprehensive README can be a challenge.
This extension automatically analyzes code structure and logic to generate a summary and explanation for developers, saving hours of manual exploration.

Note: The analysis time may vary based on your OpenAI token limit and repository size.
If an error occurs, the system will display it — otherwise, just relax and wait for your results! 🚀

Features

1. GitHub Repo URL Retrieval
Paste a GitHub repository URL directly into the extension, and it fetches the repository’s files for analysis.

2. Code Analysis & Explanation
The backend uses GPT-4o-mini’s natural language capabilities (via LangChain) to interpret, explain, and document code files.

3. Summarization of Explanations
After analyzing multiple files, it intelligently summarizes the key logic, workflow, and project overview.

4. Error Handling & Response Logging
Displays user-friendly error messages when rate limits or token issues occur.