# GitHub MCP Assistant

A production-ready **Model Context Protocol (MCP) server** that gives Claude Desktop read and write access to GitHub repositories.

Built with **FastMCP**, this local integration allows Claude to analyze code, track issues, inspect pull requests, create issues, and post comments directly to GitHub through natural-language commands.

The server runs locally using **stdio**, so your GitHub credentials and repository interactions stay on your machine while communicating directly with the GitHub API.

---

## ✨ Features

GitHub MCP Assistant provides the following tools:

| Tool | Description |
|---|---|
| `get_latest_issues` | Fetches the 5 most recent open issues from a GitHub repository. |
| `get_pr_diff` | Retrieves the code diff for a specific Pull Request. Responses are automatically truncated to 5,000 characters. |
| `create_issue` | Creates a new GitHub issue with a title and description. |
| `comment_on_pr` | Adds a comment to an existing Pull Request. |

### What You Can Do

With Claude Desktop connected to this MCP server, you can:

- 🔍 Analyze GitHub repositories
- 🐛 Fetch and understand open issues
- 🔀 Review Pull Request changes
- 📝 Create GitHub issues
- 💬 Comment on Pull Requests
- 🤖 Perform AI-assisted code reviews
- 📊 Ask Claude to summarize repository activity

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastMCP**
- **Model Context Protocol (MCP)**
- **GitHub API**
- **Claude Desktop**
- **stdio transport**

---

## 📋 Prerequisites

Before installing the project, make sure you have:

- **Python 3.10 or higher**
- **Claude Desktop**
- A **GitHub account**
- A GitHub **Fine-grained Personal Access Token**

You can verify your Python installation with:

```bash
python --version
```

---

# 🚀 Installation

## 1. Install the MCP Server

Install the package directly from GitHub using `pip`:

```bash
pip install git+https://github.com/DivyanshAgarwal7/github-mcp-server.git
```

After installation, the `github-assistant` command will be available globally.

You can verify the installation with:

```bash
github-assistant
```

---

# 🔐 Configuration

To connect the MCP server to Claude Desktop, you need to provide a GitHub Personal Access Token.

## 2. Generate a GitHub Personal Access Token

Go to:

**GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens**

Create a new token and configure:

### Repository Access

Select:

> **Only select repositories**

Then choose the repositories that Claude should be allowed to access.

### Repository Permissions

Grant the required permissions for:

- **Issues** — Read and Write
- **Pull requests** — Read and Write

Generate the token and copy it immediately.

> ⚠️ **Security:** Never commit your GitHub token to a Git repository or share it publicly.

---

# 🖥️ Claude Desktop Configuration

## 3. Locate the Claude Desktop Configuration File

### Windows

The standard configuration file is:

```text
%APPDATA%\Claude\claude_desktop_config.json
```

For the Microsoft Store version of Claude Desktop, it may be located at:

```text
%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json
```

### macOS

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

---

## 4. Add the MCP Server

Open `claude_desktop_config.json` and add:

```json
{
  "mcpServers": {
    "github-assistant": {
      "command": "github-assistant",
      "args": [],
      "env": {
        "GITHUB_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
      }
    }
  }
}
```

Replace:

```text
YOUR_GITHUB_TOKEN_HERE
```

with your actual GitHub Personal Access Token.

### Existing MCP Servers

If you already have other MCP servers configured, **do not replace the entire file**.

Simply add the `github-assistant` entry inside the existing `mcpServers` object.

For example:

```json
{
  "mcpServers": {
    "another-server": {
      "command": "another-server"
    },
    "github-assistant": {
      "command": "github-assistant",
      "args": [],
      "env": {
        "GITHUB_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
      }
    }
  }
}
```

---

# 🔄 Restart Claude Desktop

After modifying the configuration:

1. Completely quit **Claude Desktop**.
2. Make sure Claude is also closed from the system tray.
3. Start Claude Desktop again.
4. Open a new conversation.
5. Check whether the MCP server/tools are available.

If the server is configured correctly, Claude should be able to access the GitHub MCP tools.

---

# 💡 Usage Examples

Once the MCP server is connected, you can interact with GitHub using natural language.

### Get Latest Issues

```text
Use github-assistant to fetch the latest issues in microsoft/vscode and summarize them.
```

### Review a Pull Request

```text
Pull the diff for PR #123 in my DivyanshAgarwal7/Demo repository.

What is the core logic change?
```

### Create an Issue

```text
Create a new issue in DivyanshAgarwal7/Demo titled
"Update Database Schema"

Write a brief description of the required changes.
```

### Comment on a Pull Request

```text
Comment on PR #45 in my repository saying:

"Looks good, but please add unit tests for the new API endpoint."
```

### AI-Assisted Code Review

You can also ask Claude to analyze a Pull Request and provide feedback:

```text
Review PR #25 in my repository.

Check for:
- Bugs
- Security issues
- Code quality problems
- Missing tests
- Potential performance issues
```

---

# 🔒 Security & Privacy

GitHub MCP Assistant is designed to run as a **local stdio MCP server**.

### Local Execution

The MCP server runs directly on your computer rather than being hosted on a third-party server.

### Direct GitHub API Communication

Your machine communicates directly with the GitHub API.

### No Cloud Hosting

The MCP server does not require a separate cloud backend to operate.

### Token Handling

Your GitHub Personal Access Token is supplied through the Claude Desktop configuration as an environment variable.

> **Important:** Your `claude_desktop_config.json` contains sensitive credentials. Do not upload it to GitHub or share it publicly.

---

# 🏗️ How It Works

```text
┌───────────────────┐
│   Claude Desktop  │
└─────────┬─────────┘
          │
          │ MCP / stdio
          ▼
┌───────────────────┐
│ GitHub MCP        │
│ Assistant         │
│                   │
│ FastMCP Server    │
└─────────┬─────────┘
          │
          │ GitHub API
          ▼
┌───────────────────┐
│      GitHub       │
│                   │
│ Repositories      │
│ Issues            │
│ Pull Requests     │
└───────────────────┘
```

Claude sends MCP tool requests to the local server.

The server then communicates with GitHub using the configured GitHub token and returns the results to Claude.

---

# 📁 Project Structure

```text
github-mcp-server/
│
├── src/
│   └── ...
│
├── README.md
└── pyproject.toml
```

---

# 🧪 Troubleshooting

## MCP Server Is Not Appearing in Claude

Check the following:

1. Verify that `github-assistant` is installed.
2. Run:

```bash
github-assistant
```

3. Verify that your GitHub token is correct.
4. Check the Claude Desktop configuration file for JSON syntax errors.
5. Completely restart Claude Desktop.
6. Make sure the `command` value matches the installed executable.

---

## GitHub API Authentication Fails

Verify that:

- Your token has not expired.
- The token has access to the requested repository.
- Issues and Pull Requests have the required permissions.
- The token is correctly placed in the configuration.

Example:

```json
"env": {
  "GITHUB_TOKEN": "github_pat_xxxxxxxxxxxxx"
}
```

---

## Claude Cannot Access a Repository

For fine-grained GitHub tokens, make sure the repository is included under:

```text
Repository access
→ Only select repositories
```

Then verify that the required repository permissions have been granted.

---

# 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository.
2. Clone your fork.

```bash
git clone https://github.com/DivyanshAgarwal7/github-mcp-server.git
```

3. Create a new branch.

```bash
git checkout -b feature/your-feature
```

4. Make your changes.
5. Test the changes locally.
6. Commit your changes.

```bash
git add .
git commit -m "Add your feature"
```

7. Push your branch.

```bash
git push origin feature/your-feature
```

8. Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Divyansh Agarwal**

GitHub:  
https://github.com/DivyanshAgarwal7

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

If you encounter a bug or have a feature request, open an **Issue** in the repository.