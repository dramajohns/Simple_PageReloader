import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- Configuration ---
PAGE_URL = "https://www.google.com"  # Replace with the URL you want to open and reload
RELOAD_INTERVAL_SECONDS = 15

# Path to your ChromeDriver executable
CHROMEDRIVER_PATH = "/path/to/your/chromedriver" # <--- IMPORTANT: Update this path!

# Path to your Opera GX browser executable
# --- IMPORTANT: Update this path to where Opera GX is installed on your system! ---
OPERA_BROWSER_PATH = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Opera GX\\launcher.exe" # Example for Windows
# OPERA_BROWSER_PATH = "/Applications/Opera GX.app/Contents/MacOS/Opera" # Example for macOS
# OPERA_BROWSER_PATH = "/usr/bin/opera-gx" # Example for Linux

def open_and_reload_page(url: str, interval: int):
    """
    Opens a specified URL in Opera GX and reloads it at a given interval.

    Args:
        url (str): The URL of the page to open.
        interval (int): The time in seconds to wait before reloading the page.
    """
    print(f"Starting Opera GX to open and reload: {url}")
    print(f"Reloading every {interval} seconds...")

    driver = None
    try:
        # Set up Chrome options to point to Opera GX
        opera_options = Options()
        opera_options.binary_location = OPERA_BROWSER_PATH
        # You can add other options here, like headless mode if you don't want a UI
        # opera_options.add_argument("--headless")

        # Set up the ChromeDriver service
        service = Service(CHROMEDRIVER_PATH)

        # Initialize the WebDriver with Opera GX options
        driver = webdriver.Chrome(service=service, options=opera_options)

        driver.get(url)
        print(f"Page opened: {url}")

        while True:
            print(f"Waiting for {interval} seconds before reloading...")
            time.sleep(interval)
            driver.refresh()
            print(f"Page reloaded at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            print("Closing browser.")
            driver.quit()

if __name__ == "__main__":
    open_and_reload_page(PAGE_URL, RELOAD_INTERVAL_SECONDS)