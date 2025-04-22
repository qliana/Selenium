import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

screenshot_folder = "Screenshots"
os.makedirs(screenshot_folder, exist_ok=True)
print("Capturing screenshot...")


def capture_element_screenshot(driver, element, folder, element_name):
    print("Capturing screenshot345...")
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Scroll the element into view
    #driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Capture the screenshot
    screenshot_path = os.path.join(folder, f"{element_name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    return screenshot_path



