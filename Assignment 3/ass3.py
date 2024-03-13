# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(9)

#Clicking on New Release button
new_release_button = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[3]")
new_release_button.click()
#Waiting for new release page to load
time.sleep(5)

#clicking on button that loads next products
next_products_button = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[3]/a/span")
next_products_button.click()
#waiting for new products to load
time.sleep(3)

#clicking on button that loads next products
next_products_button = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[3]/a/span")
next_products_button.click()
#waiting for new products to load
time.sleep(3)

#selecting one product from page 3/10
product_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/ol/li[1]/div/div[2]/div/a[2]/span/div")
product_link.click()
#waiting for product page to load
time.sleep(3)

# Adding the product to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()
#waiting for cart to update
time.sleep(4)

#clicking on proceed to checkout button
proceed_to_checkout= driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/form/span/span/span/input")
proceed_to_checkout.click()
#waiting for page to load
time.sleep(2)



