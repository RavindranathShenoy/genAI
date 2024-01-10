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
        print("Latest comment added")
        print("end  task  ")
    else:
        print(f"Failed to post comment. Status code: {response.status_code}")
        print(response.text)
        

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python script.py <commit_id> <changed_files> <pull_request_number> updated")

    # commit_id = sys.argv[1]
    # changed_files = sys.argv[2]
    pull_number = 8

    # print(f"${commit_id}, ${changed_files}, ${pull_number}")
    owner = "RavindranathShenoy"
    repo = "genAI"
    token = "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"

    comment_data = {
        "body": "03 dec comment",
        "commit_id": "8eac9d33ece7aa9a599efe82ece9d536f3a0909f",
        "path": "main.py",
        "position": 1
    }

    post_comment_on_pull_request(owner, repo, pull_number, token, comment_data)
