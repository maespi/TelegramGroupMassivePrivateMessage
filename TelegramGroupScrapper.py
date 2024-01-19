from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Vars for message, ids and control over already done messages
# Vars for message, ids and control over already done messages
ids = {}
done = {'Irune Vela Casabón': True, 'Mane Trempats': True, 'Mel Palos Mato Trempats': True,
            'Marta Rey Rostoll': True, 'Marc *Calvo*': False, 'èlia / crisma': True, 'eloi': True, 'Kai': True,
            'Alex Alsemito Trempats UPF': True, 'Joan Juanito Trempats': True, 'Joan Angerri': True,
            'Gurru Laia Gurrutxaga Castells Trempats': True, 'Albert Gos Trempats': True, 'Pere (Keta)': True,
            'Marina Canalla Trempats': True, 'ari Floreta Trempats Castells': True, 'Berni': True,
            'David Gacía Subirats': True, 'Ari2': True, 'Marta Bernaldez Tuki Trempats Castells': True, 'Joana': True,
            'Uriel Minga Trempats': True, 'mar casellas (damm)': True, 'janaa tripi': True, 'Markel (xake)': True,
            'Aixa (Mao)': True, 'Candela Serena Candy Trempats Castells': True, 'Carles Pons': True,
            'Carla Jutglar': True, 'Tuset (Sutton)': True, 'andrea grau (triumfa)': True,
            'Sirena Trempats Castells': True, 'LianT': True, 'Clàudia': True, 'Pol Calsina': True,
            'Eudald (Dublín)': True, 'Guillem TD (Mixu)': True, 'nora massegú (gufi)': True,
            'Samuu Trempats Castells': True, 'Noel': True, 'Avril Giné Sito Trempats': True, 'Carla Piñera': True,
            'guiomar (gigi)': True, 'Belma': True, 'Ariel (espuma)': True, 'Arnau Roca Trempats': True,
            'Sofia (Petri) Trempats Castells': True, 'Mara': True, 'joan ayza Casalla Trempats Castells': True,
            'Alfons (Xop)': True, 'papallona amàlia': True, 'Sergi Mosquera': True,
            'rita Rifu Fuertes Trempats Castells': True, 'Dior': True, 'anna (galileo)': True,
            'Laura Pisa Aragon': True, 'Sito': True, 'Oriol Salat': True, 'foix (guineu)': True, 'Albert Blasco': False,
            'Nerea Tarifa': False, 'Bernat Girabal': False, 'aina - fum': False,
            'Mireia Serrat Trempats Castells': True, 'Quim (mimo)': True, 'Mariona Maria': True, 'Erik (Tinto )': False,
            'Martina': True, 'Martina (Tram)': False, 'Arnau Munsó Giró': True, 'Maverick': True, 'Tarik': True,
            'Àlvar Trempats Castells': True, 'Sandra': False, 'Paula Carulla': False,
            'Ari Coro Trempats Castells': True, 'Juls (Trotsky)': True, 'Nil': False, 'Alba (Arròs)': True,
            'Sergi Puig': True, 'noah': False, 'Marc S (Gaspi)': True, 'Ortua (Irene)': True,
            'berta orriols (wachi)': True, 'Txamo': True, 'Ibu (Aina)': True, 'Beth': False, 'Nil Trempats': True,
            'Aleix Capó': True, 'nil :) Esmolet Trempats': True, 'Berta Sellarès (mouse)': True,
            'Adrià Febrer Trempats': True, 'Angela Planas Gueto Trempats Castells': True, 'Cris Sidra': True,
            'miranda (berru)': True, 'Filiberto (Lluc)': True, 'Alba Valero': False, 'karla (qk)': True,
            'Aitana (daura)': True, 'Bernat Rustu': False, 'lluna (pirata)': False, 'judith (tinky)': True,
            'Farners': True, 'carlota Marqueta': True, 'Pinxo (Ferran)': True, 'Xavi Riera': False, 'Joan Garcia': True,
            'Xavi/Guaḥe': True, 'Josep Xolo Trempa': True, 'Sebastian :):)': True, 'Júlia camps': False, 'Wagner': True,
            'alice': True, 'boira (maria)': False, 'joana aymerich': True, 'Miquel Bisbe (lleó)': True,
            'Jordi (Fuet-castells)': True, 'Laia Lloreda': True, 'Carmona': True, 'Jona': False,
            'Enric Piñera i Pons': False, 'Isaac Trempats': True, 'Rut Cabús Tur Trempats': True, 'Xorro': False,
            'Cèlia': True, 'Trk (Branca)': False, 'Eric 8mil Trempats': True, 'Cèsar (alea)': False,
            'Joana Gimbernat': True, 'Carol Rius': False, 'Silvia Silbato Trempats': True, 'Aina / caos': True,
            'aina pons': False, 'Sara': True, 'Paula Bozzo Trempats': True, 'Elena B': True, "Lidia(lind'or)": False,
            'Rodrigo Gonzalez (RATO)': False, 'Nemo Trempats': True, 'Irene (Airin)': False, 'bruno': False,
            'Farraona': True, 'Jansi (Moana)': True, 'Biela': False, 'Jordi (Kali)': True, 'Guillem': False,
            'Oleguer (Hop)': False, 'Pau (Kiwi)': True, 'Albert': True, 'raquel (ambar)': True,
            'Judith Mandra Trempats Castells': True, 'laia ubeda': True, 'Cristina Llobet (Llop)': False, 'Pau G': True,
            'GANSO Masó': True, 'Uri': False, 'Judit Ángel': False, 'Júlia Juvi Vila Trempats': True,
            'Charlie (Wonka)': True, 'Ignasi Salat': False, 'Pol Guasch': False, 'Enric To': False,
            'Maria París': False, 'Lluís Afonso': False, 'Anna Salido': True, 'Laisa Bonin': True, 'pau': False,
            'Gerçao Carles Paré (Peri)': False, 'Pat Mer UPF': True, 'Tusa': True, 'R@sto': True,
            'Antonio Trempats': True, 'Elisenda Rovira': True, 'Altuna': True, 'Àlex Llambrich': True, 'Eloy': True,
            'Marina Amorós': True, 'Manu': True, 'reshu': True, 'Aarroncar': True, 'Núria Corominas': True,
            'Gemma (bolet)': True, 'Èlia': True, 'Lucia Peñalver Planas': True, 'Gerçao Maravillao': True,
            'gabrielaa': True, 'Lluís Fonsi': True, 'Tini': True, 'Marina G (nones)': True,
            'Enric Pissarra Fumon Trempats': True, 'Martina petita': True, 'júlia alegre (haxis)': False,
            'Anna Campàs': False, 'Alba (RIGA)': False, 'oriøl': True, 'Laura Polo Dalfó': True,
            'Laia Peiró Trempats Castells': True, 'Paula Costa': True, 'Mimoso': True, 'marcos': False,
            'Irene (Badgyal)': True, 'Angel de Felipe Sainz': False, 'Jonka': False, 'mario': False, 'Vincent': False,
            'SOTO Paula Soto Reina': False, 'Afra Tarradas Olivé': False, 'Maria Mas': False, 'Gemma Ayats': False,
            'Sergi': False, 'jana (queen)': False, 'GUMET': False, 'meritxell': False, 'Lady': False, 'Lia': True,
            'Apolo': False, 'Helena / Goliat': False, 'Caballero': True, 'cristu (martí)': True, 'Aleee (Gat)': False,
            'Jules Jofra': False, 'Moya': False, 'Uri Pallaflam': False, 'mariona carbó ️': False,
            'Núria (Aspa)': False, '@@@ - lisa': False, 'Carla (Varas)': False, 'vall bass': True,
            'Miquel (uep!)': False, 'Aner (Puyol)': False, 'Pere Burgués Carreño': True, 'Jordi Farre Flotats': False,
            'Silvia Colom Cometa Trempats': True, 'Alex Teixido': True, 'Farlopa': False, 'rovelló (lluc)': False,
            'ᴘᴀᴜ ☭': False, 'Jujuu': False, 'María Urbasos Miravé': False, 'Moncho': True, 'Oscar Duran': False,
            'Uxía': False, 'Floquet (gisela)': False, 'Neus Roca': False, 'Ariadna Bajona': False,
            'Laia Bessó (Bessoneta)': False, 'Enric': False, 'Ari Riera': False, 'Pau': False, 'Gerard (Geri)': False,
            'Judit': False, 'Aniol Xolís': False, 'Albert Solanes': False, 'Gabarró': False, 'JB': False,
            'mariona(galàn)': False, 'Anna Fadi': False, 'Júlia (einstein)': False, 'Inés': False,
            'Victor (Vitti)': False, 'aina': False, 'Miquel Alcarria': False, 'Keli (Ari)': False,
            'Núria Lopera': False, 'franco vitola': False, 'Sam Gardner': False, 'Biel Roquet': False,
            'Núria Coll': False, 'Villarejo Tu Papá': False, 'Fidel': False, 'Maria Farràs': False, 'Lillie': True,
            'belén (newton)': False, 'xuculita': False, 'Adrià Canyelles (canyes)': False, 'montana': False,
            'Aina Eberlé': False, 'Laia Sevillano': False, 'Martí Fabrés': False, 'Marc Rivera': False,
            'Txell Muntané': False, 'Marc Anglès': False, 'Sonia Pedrola': True, 'Joan Esquirol': False,
            'Laia Fontbona': False, 'Biel (Eliot)': False, 'Alexandra Codina': False, 'Laia Homdedeu': False,
            'Ton Linus': False, 'Pere De Solà-Morales Casals': True, 'Marta (Pagu)': False,
            'Alba Abelanet (Maia)': False, 'Gerard Bono': False, 'Aina Roglan': False, 'Josephine Cretin': False,
            'Ariadna Márquez': False, 'Alex Baquer': False, 'Amèlia :)': False, 'Pich': False,
            'violeta (alaska)': False, 'Mayayo': False, 'Lucia Matamoros': True, 'sira': True, 'Ana Fariña': True,
            'asha': True, 'Yubei Castellà': True, 'Gemma Simon': True, 'Elens B': True, 'Judit Olives Llabres': True,
            'Miki Redo': True, 'Alex Codina (Riuda)': True, 'Sandra (Aquiles)': True, 'Març': True, 'herbes': True,
            'Nidà Farooq': True, 'Andrea Bertolero (dorayaki)': True, 'Peiret Castells Trempats': True,
            'susi (Sushi) Trempats': True, 'Jan Trempats': True, 'Uri Trempats Roco': True,
            'Aleix Astro Trempats': True, 'iria Trempats Castells': True, 'ansiyu Trempats': True,
            'Mireia Mati Trempats': True, 'David Floquemu': True, 'Claudia (flusky)': True, 'berta jazz': True,
            'DEKA': True, 'Olga (vellaca)': True, 'Marina (Nanu)': True, 'Ena': True, 'marti/obridor': True,
            'Edu Tuno': True, 'Yuni': True, 'Mireia CRESPI': True, 'Gabriel': True, 'Laia Dosta': True, 'Alba': True,
            'Sergio (Ventafocs) :)': True, 'Lidia (GTA)': True, 'carcellé': True, 'Marc Ska': True, 'Vinyet': True,
            'Cisco': True, 'adriana (pastis)': False, 'Nit-Ari': False, 'A': False, 'Alba (Maduixota)': False,
            'Uri2': False, 'maria (medi)': True, 'Aineet': True, 'Floren Ventura': True, 'Sara Barbé': True,
            'Sara (rusalia)': True, 'Diplo': True, 'Daniel G. Crespo': True, '. .': True, 'Laia Coronado Nadal': True,
            'Eric': True, 'Marc Fusté': True, 'Sònia': True, 'Maria Bru': True, 'Adri': True, 'Gerard Bruguera': True,
            'Juju (Judith)': True, 'Carles Paré (Peri)': True, 'Reina Casa Papa': True, 'Telegram': True,
            'Ares Aleix': True, 'Comi Popop': True, 'SCF - Barcelona': True, 'GetIDs Bot': True, 'SabaGram': True,
            'BAAAASSS': True, 'Ferran Elena Elias': True, 'Nova comi gespa': True, 'T-mobilitat Atenció': True,
            'Raska Ainhoa BcTours Puerto': True, 'Arantxa Madriz Granada': True, 'Batfolrades🦇': True,
            'Néstor Punqui Mer': True, 'Mama Sushi Trempars': True, 'Jordà Sanchez': True, 'Sara🦎 (rusalia)': True,
            'Gabriel🦊': True, 'David Floquemu🗿': True, 'Mireia Mati💃 Trempats': True,
            'susi\U0001faf6🏼 (Sushi) Trempats': True, 'Mimoso✨': True, 'Caballero🐻': True, 'Miquel Bisbe (lleó🦁)': True,
            'Alba (Arròs🍚)': True, 'papallona amàlia🦋': True, 'Erik (Tinto 🍷)': True, 'Oleguer (Hop)🐇': True,
            'Legends': True, "Hazelnut's League ⚽️🍻🍾": True, 'BARRA dinar 10è': True, 'Cibersec Ágora': True,
            'Excursió ensaïmada 🥐': True, "Bombolonies '24": True, 'animació furbo💃🤩🤪': True, 'aina - fum💨💨': True,
            'lluna 🏴\u200d☠️ (pirata)': True}

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
        if (i in chat_name):
            #Instead of write message, it gets pasted (msg_control not in last_msg) and
        #    driver.find_elements(By.CLASS_NAME,"input-message-input")[-2].send_keys(Keys.CONTROL + 'v')
        #    actions = ActionChains(driver)
        #    actions.send_keys(Keys.ENTER)
        #    actions.perform()
            done[chat_name]=True
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


def AccessAndSendMEssageGroupMembers():
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
        StaleElementReferenceException


    # Get driver and set default user use existing sessions
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:/Users/marca/AppData/Local/Google/Chrome/User Data/Default")
    driver = webdriver.Chrome(
        options=options
    )
    # visit your target site
    driver.get('https://web.telegram.org/k/#-1338476666')
    sleep(5)
    # Access group info
    element = driver.find_element(By.CLASS_NAME, "person")
    element.click()
    sleep(20)
    # Access group participants list and data, check which div contains participants
    chats_divs = driver.find_elements(By.CLASS_NAME, "chatlist")
    chat_members = driver.find_element(By.CLASS_NAME, "chatlist").find_elements(By.TAG_NAME, 'a')
    for chat in chats_divs:  # Check chatlist for members
        members = chat.find_elements(By.TAG_NAME, 'a')
        if len(chat_members) < len(members): chat_members = members

    for m in range(len(chat_members)):
        username = chat_members[m].find_element(By.CLASS_NAME, "user-title").text
        try:
            if username not in done or not done[username]:
                chat_members[m].click()
                done[username] = True
                sleep(2)
                driver.find_elements(By.CLASS_NAME, "input-message-input")[-2].send_keys(Keys.CONTROL + 'v')
                ActionChains(driver).send_keys(Keys.ENTER).perform()
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                sleep(2)
            driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""",
                                  chat_members[m])
        except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
            print("Exception user: ", username)
            done[username] = False

    sleep(5)

    driver.get('https://web.telegram.org/k/#872091572')
    sleep(1)

    driver.find_elements(By.CLASS_NAME, "input-message-input")[-2].send_keys(str(done))
    sleep(10)
    print(done)

print("------Start------")

AccessAndSendMEssageGroupMembers()

print("------End------")

driver.quit()
