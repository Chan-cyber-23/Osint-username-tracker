import requests

def check_username(username):
    websites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter (X)": f"https://x.com/{username}",
    }

    for site, url in websites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Username found on {site}: {url}")
            else:
                print(f"[-] Not found on {site}")
        except:
            print(f"[!] Error checking {site}")

# Example usage
username = "nabbiejeon"  # Replace with any username
check_username(username)
