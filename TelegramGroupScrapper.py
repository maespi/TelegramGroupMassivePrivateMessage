from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
 
# initialize an instance of the chrome driver (browser)
driver = webdriver.Chrome(r"C:\Users\portatil_upf\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# visit your target site
driver.get('https://web.telegram.org/k/')
sleep(25)

def get_ids():
    driver.get('https://web.telegram.org/k/#-1338476666')
    sleep(2)
    element = driver.find_element(By.CLASS_NAME, "person")
    element.click()
    sleep(10)
    chats_divs = driver.find_elements(By.CLASS_NAME, "chatlist")
    chat_members = driver.find_element(By.CLASS_NAME, "chatlist").find_elements(By.TAG_NAME,'a')
    for chat in chats_divs: #Check chatlist for members
        members = chat.find_elements(By.TAG_NAME,'a')
        if len(chat_members)<len(members): chat_members = members

    ids = []
    for member in chat_members:
        ids.append(member.get_attribute("data-peer-id"))
    
    
    return ids

def access_profiles(ids):
    for id_num in ids:
        url = "https://web.telegram.org/k/#" + str(id_num)
        print(url)
        driver.get(url)
        sleep(3)

ids = get_ids()
print("------Start------")
print(ids)
print("------End------")
access_profiles(ids)

driver.quit()