# utils.py

from fake_useragent import UserAgent

def get_random_user_agent():
    """Returns a random User-Agent string."""
    return UserAgent().random
