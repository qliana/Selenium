from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import pytest
import os
from screenshot import capture_element_screenshot, screenshot_folder


load_dotenv()
EMAIL = os.getenv("AMAZON_EMAIL")
PASSWORD = os.getenv("AMAZON_PASSWORD")

@pytest.fixture
def driver():
    service = Service(executable_path="chromedriver.exe") 
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_google_search(driver: WebDriver):
    wait = WebDriverWait(driver, 20)
    URL=driver.get("https://www.amazon.in/")
    driver.maximize_window()
    assert "amazon.in" in driver.current_url, f"Expected Amazon.in, but got {URL}"
    capture_element_screenshot(driver, URL, screenshot_folder, "amazon_home")

    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    search=driver.find_element(By.XPATH,"//*[@id='nav-link-accountList-nav-line-1']")
    search.click()
    cap=capture_element_screenshot(driver, search, screenshot_folder, "search_button")
    assert cap, f"Screenshot was not saved at {cap}"
    wait = WebDriverWait(driver, 20)
    
#wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='nav-action-inner']"))).click()

    email=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='ap_email_login']")))
    email.send_keys(EMAIL)
    capt=capture_element_screenshot(driver, email, screenshot_folder, "email")
    assert (capt), f"Screenshot was not saved at {capt}"

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='a-button-input']"))).click()
    password=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='ap_password']")))
    password.send_keys(PASSWORD)
    captu=capture_element_screenshot(driver, password, screenshot_folder, "password")
    assert (captu), f"Screenshot was not saved at {captu}"


    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='signInSubmit']"))).click()
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='hm-icon-label']"))).click()
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space(.)=\"Women\'s Fashion\"]")))
    element.click()
    captur=capture_element_screenshot(driver, element, screenshot_folder, "element")
    assert (captur), f"Screenshot was not saved at {captur}"


    wait = WebDriverWait(driver, 20)
    watch = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'watches_0_2_11_8')]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", watch)
    time.sleep(1)  # Small delay to let any animations finish
    driver.execute_script("arguments[0].click();", watch)
    print("Scrolling to the watch element")
   
    
    print("Scrolling to the bottom of the page")
    time.sleep(10)
    wait = WebDriverWait(driver, 20)
    wrist=wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Wrist Watches')]")))
    wrist.click()
    capturr=capture_element_screenshot(driver, wrist, screenshot_folder, "wrist")
    assert (capturr), f"Screenshot was not saved at {capturr}"
    time.sleep(5)


    Titan = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[text()='Titan'])[16]")))
    Titan.click()
    capturrr=capture_element_screenshot(driver, Titan, screenshot_folder, "Titan")
    assert (capturrr), f"Screenshot was not saved at {capturrr}"



   
#     checkbox = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Titan']/preceding::input[@type='checkbox'][1]"))
# )
#     checkbox.click()
#     captur=capture_element_screenshot(driver, checkbox, screenshot_folder, "checkbox")
#     assert (captur), f"Screenshot was not saved at {captur}"

    #assert (capturr), f"Screenshot was not saved at {capturr}"


# def load_entire_page(driver, pause_time=2):
#     """Scrolls to the bottom of the page to load all dynamic content."""
#     last_height = driver.execute_script("return document.body.scrollHeight")

#     while True:
#         # Scroll down to bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(pause_time)  # Wait for page to load

#         # Check new height after scroll
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

    
#     print("Loading entire page")

    

