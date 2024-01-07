from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import Select

# Set the path to your WebDriver
driver_path = '/chromedriver.exe'

# Create a new instance of the Chrome driver
#driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()

# Navigate to the shopping website
driver.get('https://megaeshop.pk/')  # Replace with the URL of the shopping website

# Find the search input element by ID
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'dgwt-wcas-search-input-2'))
)

# Send the search query
search_query = '60W Adjustable Soldering Iron'
search_input.send_keys(search_query)

# Press Enter to perform the search
search_input.send_keys(Keys.RETURN)

#time.sleep(5)

# Wait for the "Dismiss" link to be clickable
dismiss_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'woocommerce-store-notice__dismiss-link'))
)

# Click the "Dismiss" link
dismiss_link.click()

#time.sleep(5)

# Wait for the "Buy Now" button to be clickable
buy_now_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'wd-add-to-cart'))
)

# Click the "Buy Now" button
buy_now_button.click()

#time.sleep(5)

# Wait for the input field to be present on the page
input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'billing_first_name'))
)

# Type your name into the input field
your_name = "Fake Name"  # Replace with your actual name
input_field.send_keys(your_name)

# Wait for the phone input field to be present on the page
phone_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'billing_phone'))
)

# Type your phone number into the input field
phone_number = "0333-0312538"  # Replace with your actual phone number
phone_input.send_keys(phone_number)

# Wait for the email input field to be present on the page
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'billing_email'))
)

# Type your email into the input field
email_address = "fake_email@gmail.com"  # Replace with your actual email
email_input.send_keys(email_address)

# Wait for the address input field to be present on the page
address_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'billing_address_1'))
)

# Type your address into the input field
full_address = "My house, my street, My City"  # Replace with your actual address
address_input.clear()
address_input.send_keys(full_address)

# Wait for the city input field to be present on the page
city_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'billing_city'))
)

# Type your city into the input field
city_name = "Islamabad"  # Replace with your actual city
city_input.send_keys(city_name)

# Wait for the dropdown to be present on the page
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//span[@aria-label="State"]'))
)

# Click the dropdown to open it
dropdown.click()

# Simulate pressing the Enter key
dropdown.send_keys(Keys.ENTER)

time.sleep(10)

# Wait for the "Place order" button to be present on the page
place_order_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'place_order'))
)

# Click the "Place order" button
place_order_button.click()

time.sleep(60)

# Close the browser
driver.quit()
