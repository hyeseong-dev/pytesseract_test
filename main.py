from selenium import webdriver
from PIL import Image
import pytesseract

# Start a web driver (e.g. Chrome)
driver = webdriver.Chrome()

# Navigate to the live YouTube video
URL = "https://www.youtube.com/watch?v=PmMgqbCJwGI"
driver.get(URL)

# Take a screenshot of the entire page
screenshot = driver.get_screenshot_as_png()

# Open the screenshot as an image using PIL
img = Image.open(screenshot)

# Use pytesseract to extract the text from the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)

# Close the web driver
driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time 



def ge_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maxmized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver = webdriver.Chrome('./chromedriver')
    return driver



driver.get(url='https://www.naver.com')
driver.find_element(By.NAME, 'query').send_keys('한국 월드컵 일정')
driver.find_element(By.ID, 'search_btn').click()
time.sleep(5)

path = 'C:/Users/user/Pictures/worldCupKorea.jpg'
driver.find_element(By.CLASS_NAME, 'result_box._pageWrapper').screenshot(path)