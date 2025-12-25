"""
utils.py
--------

This module provides utility functions for the CineMatch AI scraping engine.
Its primary purpose allows our scraper to mimic a legitimate web browser
Avoid being blocked by anti-bot protections.
"""

from typing import Dict

def get_headers() -> Dict[str, str]:
    """
    Constructs and returns a dictionary of HTTP headers to mimick a real browser.

    Returns:
        Dict[str, str]: A dictionary containing standard browser headers.
    """
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
