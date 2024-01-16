from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

ids = {}
done = []
msg = "Hello World"
 
# initialize an instance of the chrome driver (browser)
driver = webdriver.Chrome()
# visit your target site
driver.get('https://web.telegram.org/k/')
sleep(30)

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

    for member in chat_members:
        ids[member.find_element(By.CLASS_NAME, "user-title").text] = member.get_attribute("data-peer-id")


def access_profiles(message):
    for i in ids:
        url = "https://web.telegram.org/k/#" + str(ids[i])
        print(i)
        driver.get(url)
        sleep(1)
        if(i=='Marc *Calvo*'):
            actions = ActionChains(driver)
            actions.send_keys(message)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            sleep(1)
            

get_ids()
print("------Start------")
print(ids)
print("------End------")
access_profiles(msg)

driver.quit()
