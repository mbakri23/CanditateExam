import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
promoCode = "rahulshettyacademy"
site="https://rahulshettyacademy.com/seleniumPractise/#/"
products = ["Brocolli", "Tomato","Pumpkin "] # list of products to add to cart
driverLocation = '/Users/mohammadba/Downloads/chromedriver' # Local WebDriver Location 

driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options)
driver.get(site)

search = driver.find_element(By.CLASS_NAME, "search-keyword")

for element in products:
    search.send_keys(element)
    time.sleep(1)

    button = driver.find_element(By.CLASS_NAME, "products").find_element(By.TAG_NAME, "button").click()
    time.sleep(0.5)
    search.clear() # reset search

CartClick= driver.find_element(By.CLASS_NAME, "cart-icon").click()
ProceedToCheckout = driver.find_element(By.CLASS_NAME, "action-block").find_element(By.TAG_NAME,"button").click()
time.sleep(0.5)

ProceedToCheckout = driver.find_element(By.CLASS_NAME,"promoCode")
promoBtn = driver.find_element(By.CLASS_NAME,"promoBtn")
time.sleep(1)

ProceedToCheckout.send_keys(promoCode)
time.sleep(0.2)

promoBtn.click()
time.sleep(5) # Wait for Code Validation

promoBtnColor = driver.find_element(By.CLASS_NAME,"promoInfo").get_attribute('style')
if("green" in promoBtnColor):
    print("Promo Code was successful")
else:
    print("Promo Code is invalid")

driver.close() # Close WebPage

