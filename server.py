from fastmcp import FastMCP
import httpx
import os

# 1. Initialize the MCP Server
mcp = FastMCP(name="GitHub-Assistant")

# 2. Add a tool using a decorator
@mcp.tool
def get_latest_issues(owner: str, repo: str) -> dict:
    """Fetches the 5 most recent open issues for a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "FastMCP-Python-Server"
    }
    params = {"state": "open", "per_page": 5}
    
    # Execute the HTTP request
    response = httpx.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        issues = response.json()
        return {"issues": [{"title": i["title"], "url": i["html_url"]} for i in issues]}
    else:
        return {"error": f"Failed to fetch issues: {response.status_code}"}

# 3. Adding a Pull Request analyzer transforms
@mcp.tool
def get_pr_diff(owner: str, repo: str, pr_number: int) -> dict:
    """Fetches the raw code differences (diff) for a specific GitHub pull request."""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    
    # We change the Accept header to ask GitHub for the raw code diff instead of JSON
    headers = {
        "Accept": "application/vnd.github.v3.diff",
        "User-Agent": "FastMCP-Python-Server"
    }
    
    response = httpx.get(url, headers=headers)
    
    if response.status_code == 200:
        # Because we requested a diff, the response is raw text, not JSON
        diff_text = response.text
        
        # We truncate the text to 5000 characters so we don't overwhelm the AI's context window
        # if someone submits a massive PR.
        return {
            "repository": f"{owner}/{repo}",
            "pr_number": pr_number,
            "diff_preview": diff_text[:5000] 
        }
    else:
        return {"error": f"Failed to fetch PR: {response.status_code}"}

# 4. Adding a new issue creating tool

@mcp.tool
def create_issue(owner: str, repo: str, title: str, body: str) -> dict:
    """Creates a new issue in a GitHub repository."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return {"error": "Authentication failed. GITHUB_TOKEN environment variable is missing."}

    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    
    # We must include the Authorization header for POST requests
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "FastMCP-Python-Server"
    }
    
    # The data we are sending to GitHub
    payload = {
        "title": title,
        "body": body
    }
    
    # Use httpx.post and pass the payload as json
    response = httpx.post(url, headers=headers, json=payload)
    
    if response.status_code == 201: # 201 means "Created"
        data = response.json()
        return {"success": True, "issue_url": data["html_url"]}
    else:
        return {"error": f"Failed to create issue: {response.text}"}

# 5. Adding a comment tool

@mcp.tool
def comment_on_pr(owner: str, repo: str, pr_number: int, body: str) -> dict:
    """Adds a comment to a specific Pull Request."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return {"error": "Authentication failed. GITHUB_TOKEN environment variable is missing."}

    # In GitHub's backend architecture, PR comments share the /issues/ endpoint
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "FastMCP-Python-Server"
    }
    
    payload = {
        "body": body
    }
    
    response = httpx.post(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        data = response.json()
        return {"success": True, "comment_url": data["html_url"]}
    else:
        return {"error": f"Failed to post comment: {response.text}"}

    
# 6. Make the server executable
if __name__ == "__main__":
    mcp.run()