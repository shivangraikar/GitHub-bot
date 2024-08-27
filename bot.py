# -*- coding: utf-8 -*-
"""
@author: Shivang
"""
import requests
import time

# Replace with your GitHub personal access token
TOKEN = 'YOUR_GITHUB_TOKEN'

# GitHub API endpoint for following users
API_URL = 'https://api.github.com/user/following'
FOLLOWERS_URL = 'https://api.github.com/users/{username}/followers'

# Set up the headers with the authorization token
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def get_followers(username):
    """Fetch the list of followers of a specific user, handling pagination."""
    followers = []
    page = 1
    while True:
        response = requests.get(FOLLOWERS_URL.format(username=username) + f'?page={page}&per_page=100', headers=headers)
        if response.status_code == 200:
            users = response.json()
            if not users:  # No more users
                break
            followers.extend(user['login'] for user in users)
            page += 1
            time.sleep(1)  # Avoid hitting rate limits
        else:
            print(f"Error fetching followers list: {response.status_code} - {response.text}")
            break
    return followers

def follow_user(username):
    """Follow a specific user by username."""
    follow_url = f"https://api.github.com/user/following/{username}"
    response = requests.put(follow_url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully followed {username}")
    else:
        print(f"Error following {username}: {response.status_code} - {response.text}")

def follow_users_from_account(account_username, limit=500):
    """Follow users from the followers list of a specific account."""
    followers = get_followers(account_username)
    for user in followers[:limit]:  # Only follow up to `limit` users
        follow_user(user)
        time.sleep(1)  # Avoid hitting rate limits

if __name__ == "__main__":
    # Replace 'famous_account' with the username of the account whose followers you want to follow
    follow_users_from_account('famous_account', limit=500)
