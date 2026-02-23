import os
import requests
from crewai.tools import tool


@tool("github_repo_auditor")
def github_repo_auditor(repo_name: str):

    """
    Analyzes a GitHub repository and returns technical stats like stars, issues, and forks.
    Args:
        repo_name (str): The full repository name in 'owner/repo' format (e.g., 'crewAIInc/crewAI').
    """
    

    token = os.getenv("GITHUB_TOKEN")
    header = {"Authorization": f"toekn {token}"} if token else {}
    url = f"https://api.github.com/repos/{repo_name}"

    response = requests.get(url, headers=header)
    if response.status_code==200:
        data = response.json()
        return{
            "full_name": data.get("full_name"),
            "stars":data.get("stargazers_count"),
            "open_issues":data.get("open_issues_count"),
            "description": data.get("description"),
            "forks_count": data.get("forks_count")
        }
    return f"Error: Could not find repo {repo_name}. Status: {response.status_code}"


