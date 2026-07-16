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

## Setup & Usage

### Prerequisites

- Python 3.8+
- Google Chrome
- An OpenAI API key with access to GPT-4o-mini

### 1. Run the backend

```bash
git clone https://github.com/ajayvardhan03/github_analyser.git
cd github_analyser
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The Flask server starts on `http://localhost:8000`.

### 2. Load the Chrome extension

1. Open Chrome and go to `chrome://extensions`.
2. Enable **Developer mode** (top right).
3. Click **Load unpacked** and select the root of this repository (the folder containing `manifest.json`).
4. Pin the extension for quick access.

### 3. Analyze a repository

1. Navigate to any GitHub repository page in Chrome.
2. Click the extension icon and enter your OpenAI API key.
3. Submit the current page's repository URL and wait for the AI-generated summary.

Keep the local backend (`python app.py`) running while using the extension, since the popup sends requests to `http://localhost:8000`.
