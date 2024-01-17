from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

ids = {}
done = {}
msg = "Bona tarda colla...\n🥳🥳🥳🥳LA COMEGCIAL ja està quasi aquí. És diumenge a Poblenou i és tracta d'un rodatge per una experiència immersiva de realitat virtual. Serà una oportunitat única per deixar marca com a colla i una experiència que probablement no es torni a presentar. Tindrem catering i tot!! \nSerà xulissim i desde Junta t\'animem a fer un esforç per la colla i venir!🤩\n\n És importantíssima per la colla i necessitem la participació de totes. La remuneració que rebrem per la comercial serà VITAL pel segon tram i el 10é! Per això, desde Junta i per la Colla, necessitem que confirmis a l'aleta si pots venir, que t'apuntis al forms (en cas de no tenir aleta no et preocupis)!! https://forms.gle/U3QxKc96xbBeNoga7 "
msg_control = "Bona tarda colla..."

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:/Users/marca/AppData/Local/Google/Chrome/User Data/Default")
# initialize an instance of the chrome driver (browser)
options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 1,
        }
    )
driver = webdriver.Chrome(
    options=options
)
# visit your target site
driver.get('https://web.telegram.org/k/')
sleep(10)

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
        if member.find_element(By.CLASS_NAME, "user-title").text not in done:
            done[member.find_element(By.CLASS_NAME, "user-title").text] = False

def access_profiles(message):
    global driver
    driver.quit()
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 1,
        }
    )
    # initialize an instance of the chrome driver (browser)
    driver = webdriver.Chrome(options=options)
    cont=0
    for i in ids:
        url = "https://web.telegram.org/k/#" + str(ids[i])
        driver.get(url)
        sleep(3)
        cont += 1
        if(i == 'Marc *Calvo*'):
            driver.find_element(By.CLASS_NAME,"input-message-input").send_keys(Keys.CONTROL + 'v')
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            sleep(2)

        elements = driver.find_elements(By.CLASS_NAME,"message")
        msg_txt = elements[-1].text if elements else ""
        if msg_control in msg_txt:
            print(msg_txt)
            print('Skereeeee')
            done[i] = True

        if cont%50==0:
            driver.quit()
            sleep(3)
            driver = webdriver.Chrome(options=options)

def custom_msg(usr_id,msgs):
    global driver
    driver.quit()
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 1,
        }
    )
    # initialize an instance of the chrome driver (browser)
    driver = webdriver.Chrome(options=options)
    url = "https://web.telegram.org/k/#" + str(ids[usr_id])
    driver.get(url)
    sleep(3)
    for m in msgs:
        driver.find_element(By.CLASS_NAME, "input-message-input").send_keys(m)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(10)


get_ids()
print("------Start------")
for d in done:
    if done[d]:
        ids.pop(d)
print(ids)
print("------End------")
access_profiles(msg)

custom_msg('Marc *Calvo*', [str(done)])


driver.quit()
