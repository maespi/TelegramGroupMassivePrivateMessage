from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Vars for message, ids and control over already done messages
ids = {}
done = {'Irune Vela Casabón': False, 'Mane Trempats': True, 'Mel Palos Mato Trempats': True, 'Marta Rey Rostoll': False, 'Marc *Calvo*': False, 'èlia / crisma': False, 'eloi': False, 'Kai': True, 'Alex Alsemito Trempats UPF': True, 'Joan Juanito Trempats': True, 'Joan Angerri': False, 'Gurru Laia Gurrutxaga Castells Trempats': True, 'Albert Gos Trempats': True, 'Pere (Keta)': True, 'Marina Canalla Trempats': True, 'ari Floreta Trempats Castells': True, 'Berni': True, 'David Gacía Subirats': False, 'Ari2': False, 'Marta Bernaldez Tuki Trempats Castells': True, 'Joana': False, 'Uriel Minga Trempats': True, 'mar casellas (damm)': False, 'janaa tripi': True, 'Markel (xake)': False, 'Aixa (Mao)': False, 'Candela Serena Candy Trempats Castells': False, 'Carles Pons': True, 'Carla Jutglar': True, 'Tuset (Sutton)': False, 'andrea grau (triumfa)': True, 'Sirena Trempats Castells': True, 'LianT': False, 'Clàudia': False, 'Pol Calsina': False, 'Eudald (Dublín)': False, 'Guillem TD (Mixu)': True, 'nora massegú (gufi)': True, 'Samuu Trempats Castells': True, 'Noel': False, 'Avril Giné Sito Trempats': False, 'Carla Piñera': True, 'guiomar (gigi)': False, 'Belma': False, 'Ariel (espuma)': True, 'Arnau Roca Trempats': True, 'Sofia (Petri) Trempats Castells': True, 'Mara': True, 'joan ayza Casalla Trempats Castells': True, 'Alfons (Xop)': True, 'papallona amàlia': True, 'Sergi Mosquera': False, 'rita Rifu Fuertes Trempats Castells': True, 'Dior': False, 'anna (galileo)': False, 'Laura Pisa Aragon': False, 'Sito': True, 'Oriol Salat': False, 'foix (guineu)': False, 'Albert Blasco': False, 'Nerea Tarifa': False, 'Bernat Girabal': False, 'aina - fum': False, 'Mireia Serrat Trempats Castells': True, 'Quim (mimo)': True, 'Mariona Maria': True, 'Erik (Tinto )': False, 'Martina': False, 'Martina (Tram)': False, 'Arnau Munsó Giró': False, 'Maverick': True, 'Tarik': True, 'Àlvar Trempats Castells': True, 'Sandra': False, 'Paula Carulla': False, 'Ari Coro Trempats Castells': True, 'Juls (Trotsky)': True, 'Nil': False, 'Alba (Arròs)': True, 'Sergi Puig': True, 'noah': False, 'Marc S (Gaspi)': False, 'Ortua (Irene)': True, 'berta orriols (wachi)': False, 'Txamo': True, 'Ibu (Aina)': False, 'Beth': False, 'Nil Trempats': True, 'Aleix Capó': True, 'nil :) Esmolet Trempats': True, 'Berta Sellarès (mouse)': True, 'Adrià Febrer Trempats': True, 'Angela Planas Gueto Trempats Castells': True, 'Cris Sidra': False, 'miranda (berru)': False, 'Filiberto (Lluc)': False, 'Alba Valero': False, 'karla (qk)': True, 'Aitana (daura)': False, 'Bernat Rustu': False, 'lluna (pirata)': False, 'judith (tinky)': False, 'Farners': False, 'carlota Marqueta': False, 'Pinxo (Ferran)': True, 'Xavi Riera': False, 'Joan Garcia': False, 'Xavi/Guaḥe': True, 'Josep Xolo Trempa': True, 'Sebastian :):)': False, 'Júlia camps': False, 'Wagner': True, 'alice': False, 'boira (maria)': False, 'joana aymerich': False, 'Miquel Bisbe (lleó)': True, 'Jordi (Fuet-castells)': True, 'Laia Lloreda': False, 'Carmona': False, 'Jona': False, 'Enric Piñera i Pons': False, 'Isaac Trempats': True, 'Rut Cabús Tur Trempats': True, 'Xorro': False, 'Cèlia': True, 'Trk (Branca)': False, 'Eric 8mil Trempats': True, 'Cèsar (alea)': False, 'Joana Gimbernat': False, 'Carol Rius': False, 'Silvia Silbato Trempats': True, 'Aina / caos': False, 'aina pons': False, 'Sara': False, 'Paula Bozzo Trempats': False, 'Elena B': False, "Lidia(lind'or)": False, 'Rodrigo Gonzalez (RATO)': False, 'Nemo Trempats': True, 'Irene (Airin)': False, 'bruno': False, 'Farraona': False, 'Jansi (Moana)': False, 'Biela': False, 'Jordi (Kali)': True, 'Guillem': False, 'Oleguer (Hop)': False, 'Pau (Kiwi)': False, 'Albert': False, 'raquel (ambar)': False, 'Judith Mandra Trempats Castells': False, 'laia ubeda': True, 'Cristina Llobet (Llop)': False, 'Pau G': False, 'GANSO Masó': False, 'Uri': False, 'Judit Ángel': False, 'Júlia Juvi Vila Trempats': False, 'Charlie (Wonka)': True, 'Ignasi Salat': False, 'Pol Guasch': False, 'Enric To': False, 'Maria París': False, 'Lluís Afonso': False, 'Anna Salido': True, 'Laisa Bonin': True, 'pau': False,
        'Gerçao Carles Paré (Peri)': False, 'Pat Mer UPF': True, 'Tusa': True, 'R@sto': False, 'Antonio Trempats': True, 'Elisenda Rovira': False, 'Altuna': False, 'Àlex Llambrich': False, 'Eloy': False, 'Marina Amorós': False, 'Manu': False, 'reshu': False, 'Aarroncar': False, 'Núria Corominas': False}
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
        sleep(2)
        cont += 1
        # Check if message is send and if to the correct person
        messages = driver.find_elements(By.CLASS_NAME, "message")
        last_msg = messages[-1].text if messages else ""
        chat_name = driver.find_elements(By.CLASS_NAME,"user-title")[-1].text
        if (msg_control not in last_msg) and (i in chat_name):
            #Instead of write message, it gets pasted
            driver.find_elements(By.CLASS_NAME,"input-message-input")[-2].send_keys(Keys.CONTROL + 'v')
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        sleep(2)

        #Check if message is send and if to the correct person
        messages = driver.find_elements(By.CLASS_NAME,"message")
        last_msg = messages[-1].text if messages else ""
        chat_name = driver.find_elements(By.CLASS_NAME,"user-title")[-1].text
        if  (msg_control in last_msg) and (i in chat_name): #
            done[i] = True

        #Reboot driver to avoid memory problems
        if cont%50==0:
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
