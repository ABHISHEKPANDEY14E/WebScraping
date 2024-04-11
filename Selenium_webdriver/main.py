from selenium import webdriver
from selenium.webdriver.common.by import By
# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Us-Blu-ray-Lupita-Nyongo/dp/B07PDTXZG9/ref=sr_1_3?sr=8-3")

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"The Price is {price_dollar}.{price_cents}")
# close or quit chrome programatically

# here driver.close() closes just the tab which we open
# it closes the particular tab
driver.close()



