import sys
import os
import requests

def post_comment_on_pull_request(owner, repo, pull_number, token, comment_data):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/comments'
    
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, json=comment_data)

    if response.status_code == 201:
        print("Comment posted successfully.")
    else:
        print(f"Failed to post comment. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <commit_id> <changed_files> <pull_request_number> updated")

    commit_id = sys.argv[1]
    changed_files = sys.argv[2]
    pull_number = os.environ.get('PULL_REQUEST_NUMBER')

    print(f"${commit_id}, ${changed_files}, ${pull_number}")
    owner = "RavindranathShenoy"
    repo = "genAI"
    token = "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"

    comment_data = {
        "body": "03 dec comment",
        "commit_id": commit_id,
        "path": changed_files.splitlines()[0] if changed_files else None,
        "position": 1
    }

    post_comment_on_pull_request(owner, repo, pull_number, token, comment_data)
