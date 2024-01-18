from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Vars for message, ids and control over already done messages
ids = {}
done = {}
msg = "Bona tarda colla...\n🥳🥳🥳🥳LA COMEGCIAL ja està quasi aquí. És diumenge a Poblenou i és tracta d'un rodatge per una experiència immersiva de realitat virtual. Serà una oportunitat única per deixar marca com a colla i una experiència que probablement no es torni a presentar. Tindrem catering i tot!! \nSerà xulissim i desde Junta t\'animem a fer un esforç per la colla i venir!🤩\n\n És importantíssima per la colla i necessitem la participació de totes. La remuneració que rebrem per la comercial serà VITAL pel segon tram i el 10é! Per això, desde Junta i per la Colla, necessitem que confirmis a l'aleta si pots venir, que t'apuntis al forms (en cas de no tenir aleta no et preocupis)!! https://forms.gle/U3QxKc96xbBeNoga7 "
msg_control = "Bona tarda colla..."

#Get driver and set default user use existing sessions
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

#Get ids from group id
def get_ids():
    driver.get('https://web.telegram.org/k/#-1338476666')
    sleep(2)
    #Access group info
    element = driver.find_element(By.CLASS_NAME, "person")
    element.click()
    sleep(10)
    #Access group participants list and data, check which div contains participants
    chats_divs = driver.find_elements(By.CLASS_NAME, "chatlist")
    chat_members = driver.find_element(By.CLASS_NAME, "chatlist").find_elements(By.TAG_NAME,'a')
    for chat in chats_divs: #Check chatlist for members
        members = chat.find_elements(By.TAG_NAME,'a')
        if len(chat_members)<len(members): chat_members = members

    #Register participants data
    for member in chat_members:
        ids[member.find_element(By.CLASS_NAME, "user-title").text] = member.get_attribute("data-peer-id")
        if member.find_element(By.CLASS_NAME, "user-title").text not in done:
            done[member.find_element(By.CLASS_NAME, "user-title").text] = False

#Access each user profile and send message
def access_profiles(message):
    #Configure new driver
    global driver
    driver.quit()
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 1,   #If value 2, images dont get loaded
        }
    )
    driver = webdriver.Chrome(options=options)

    cont=0
    for i in ids:
        url = "https://web.telegram.org/k/#" + str(ids[i])  #Access user
        driver.get(url)
        sleep(1)
        cont += 1
        if(i in 'Juls )'):
            #Instead of write message, it gets pasted
            driver.find_elements(By.CLASS_NAME,"input-message-input")[-2].send_keys(Keys.CONTROL + 'v')
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        sleep(1)

        #Check if message is send and if to the correct person
        messages = driver.find_elements(By.CLASS_NAME,"message")
        last_msg = messages[-1].text if messages else ""
        chat_name = driver.find_elements(By.CLASS_NAME,"user-title")[-1].text
        if  (i in chat_name): #(msg_control in last_msg) and
            print('Found')
            done[i] = True

        #Reboot driver to avoid memory problems
        if cont%100==0:
            driver.quit()
            sleep(2)
            driver = webdriver.Chrome(options=options)

#Send custom message to user id
def custom_msg(usr_id,msgs):
    # Configure new driver
    global driver
    driver.quit()
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 1,       #If value 2, images dont get loaded
        }
    )
    driver = webdriver.Chrome(options=options)
    url = "https://web.telegram.org/k/#" + str(usr_id)
    driver.get(url)
    sleep(3)
    #Send messages
    for m in msgs:
        driver.find_element(By.CLASS_NAME, "input-message-input").send_keys(m)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(10)


get_ids()

print("------Start------")
#Select special id to send message
main_id = ids['Marc *Calvo*']
#Check already messaged users
for d in done:
    if done[d]:
        ids.pop(d)

print(ids)
access_profiles(msg)
print("------End------")

custom_msg(main_id, [str(done)])


driver.quit()
