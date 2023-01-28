from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time 

chrome_options = webdriver.ChromeOptions()

def ge_chrome_options(chrome_options):
    chrome_options.add_argument('--start-maxmized')
    return chrome_options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ge_chrome_options(chrome_options))
driver = webdriver.Chrome('./chromedriver')

driver.get(url='https://www.naver.com')
driver.find_element(By.NAME, 'query').send_keys('한국 월드컵 일정')
driver.find_element(By.ID, 'search_btn').click()
time.sleep(5)

from PIL import Image
import pytesseract
from datetime import datetime
path = f"./worldCupKorea_{datetime.now().strftime('%y%m%d%H%M%S')}.png"
driver.find_element(By.CLASS_NAME, 'result_box._pageWrapper').screenshot(path)

# from pathlib import Path
# current_path = Path(__file__).resolve().parent

# # get png files in the 

# img = Image.open(img)
# text = pytesseract.image_to_string(img)
# # Print the extracted text
# print(text)
driver.quit()