import requests
import time

# Replace with your GitHub personal access token
TOKEN = 'YOUR_GITHUB_TOKEN'

# GitHub API endpoint for following users
API_URL = 'https://api.github.com/user/following'

# Set up the headers with the authorization token
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def get_following_users():
    """Fetch the list of users you are following, handling pagination."""
    following_users = []
    page = 1
    while True:
        response = requests.get(f"{API_URL}?page={page}&per_page=100", headers=headers)
        if response.status_code == 200:
            users = response.json()
            if not users:  # No more users
                break
            following_users.extend(user['login'] for user in users)
            page += 1
            time.sleep(1)  # Avoid hitting rate limits
        else:
            print(f"Error fetching following list: {response.status_code} - {response.text}")
            break
    return following_users

def unfollow_user(username):
    """Unfollow a specific user by username."""
    unfollow_url = f"https://api.github.com/user/following/{username}"
    response = requests.delete(unfollow_url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully unfollowed {username}")
    else:
        print(f"Error unfollowing {username}: {response.status_code} - {response.text}")

def unfollow_users(limit=500):
    """Unfollow a specified number of users."""
    following_users = get_following_users()
    for user in following_users[:limit]:  # Only unfollow up to `limit` users
        unfollow_user(user)
        time.sleep(1)  # Avoid hitting rate limits

if __name__ == "__main__":
    unfollow_users(limit=500)