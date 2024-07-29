# Import the necessary modules
from playwright import sync_playwright

# Create a Playwright instance
with sync_playwright() as p:
    # Launch a new browser instance
    browser = p.chromium.launch()
