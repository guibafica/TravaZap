from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Initialize the browser driver
options = Options()
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to search for a contact
def buscar_contato(nome_contato): 
  driver.implicitly_wait(10)

  # Find the search field
  search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')

  # Enter the contact's name in the search field
  search_box.send_keys(nome_contato)
  time.sleep(2)  

  # Finds the contact in the list
  contatos = driver.find_elements(By.XPATH, '//span[@class="x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1rg5ohu _ao3e"][contains(@title, "{}")]'.format(nome_contato))

  contatos[0].click()
  return True

driver.get('https://web.whatsapp.com/')

time.sleep(10)

contactName = input("Enter the contact name and press Enter: ")

# Search for the contact in the contact list
contato_encontrado = buscar_contato(contactName)

# Checks if the contact was found
if not contato_encontrado:
  print(f'Contact "{contactName}" not found in the list.')
  driver.quit()
  exit()

# Opens the text file containing the lines from the film
with open('falas_carros.txt', 'r', encoding='utf-8') as file:
    falas = file.readlines()

# Loop through all the lines and send them one by one via WhatsApp
for fala in falas:
    # Find the text field to type the message
    chat_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    
    # Type your speech in the text field
    chat_box.send_keys(fala)
    
    # Press Enter to send the message
    chat_box.send_keys(Keys.RETURN)
    
    # Waits a short interval before sending the next message
    time.sleep(1)

# Close the browser after sending all messages
driver.quit()
