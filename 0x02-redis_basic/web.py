#!/usr/bin/env python3
""" expiring web cache module """


import requests
import redis


def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a URL and cache the result with
    an expiration time of 10 seconds.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    # Create a Redis connection
    redis_conn = redis.Redis()

    # Increment the count for the URL
    url_count_key = f"count:{url}"
    redis_conn.incr(url_count_key)

    # Check if the HTML content is cached
    cached_html = redis_conn.get(url)
    if cached_html:
        return cached_html.decode()

    # Retrieve the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the HTML content with an expiration time of 10 seconds
    redis_conn.setex(url, 10, html_content)

    return html_content
