from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb
import pickle
import time
import locators
import unicodedata
from unidecode import unidecode



# driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
page = 1
rating = 77
tuple_of_players = []

def get_names():
    elems1 = driver.find_elements_by_class_name("player_tr_1")
    elems2 = driver.find_elements_by_class_name("player_tr_2")
    for each in elems1:
        name = each.text
        name = name.split("\n", 1)[0]
        name = unidecode(name)
        tuple_of_players.append(name)
    for each in elems2:
        name = each.text
        name = name.split("\n", 1)[0]
        name = unidecode(name)
        tuple_of_players.append(name)

for link in range(1,4,1):
    print("page ", str(link) )
    link = "https://www.futbin.com/19/players?page=" + str(page) + "&player_rating=" + str(rating)+ "-" + str(rating) + "&version=gold_rare&sort=Player_Rating&order=asc"
    # link = "https://www.futbin.com/players?page=" + str(page) + "&sort=ps_price&version=gold_rare&order=desc&ps_price=50000-100000"
    #link = "https://www.futbin.com/players?page=1&ps_price=30000-50000&sort=ps_price&version=gold_rare&order=desc"
    driver.get(link)
    time.sleep(5)
    get_names()
    print len(tuple_of_players)
    page = page + 1

print(tuple_of_players)
pdb.set_trace()

#for each in elems1: name = each.text; name = name.split("\n", 1)[0]; name = name.encode('ascii'); new_dict.append(name)
#for each in elems1: name = each.text; name = name.split("\n", 1)[0]; name = name.encode('ascii', 'ignore'); new_dict.append(name)



#options = webdriver.ChromeOptions()
#$options.add_argument(r"user-data-dir=C:\Users\qadmin\AppData\Local\Google\Chrome\User Data")

#driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

# Click Search
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/article/div[1]/div[2]/div/div[1]/div[1]/span[1]"))).click()




# fp = webdriver.FirefoxProfile(r'C:\Users\qadmin\AppData\Roaming\Mozilla\Firefox\Profiles\0rnj92jz.default')
# driver = webdriver.Firefox(fp)

driver.implicitly_wait(10)
#driver.get('https://www.easports.com/fifa/ultimate-team/web-app')

#driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")


# Transfers
driver.find_element_by_xpath(".//*[@id='footer']/button[5]").click()
# Transfer Search
driver.find_element_by_xpath("/html/body/section/article/div[1]").click()
# Consumables
driver.find_element_by_xpath("/html/body/section/article/div[1]/div[1]/div/a[4]").click()
# Button Search
driver.find_element_by_xpath("/html/body/section/article/div[1]/div[2]/div/div[1]/div[1]/span[1]").click()


# Transfers
driver.find_element_by_xpath(".//*[@id='footer']/button[5]").click()
# Transfer Search
driver.find_element_by_xpath("/html/body/section/article/div[1]").click()


# Consumables
driver.find_element_by_xpath("/html/body/section/article/div[1]/div[1]/div/a[4]").click()

driver.find_element_by_xpath("/html/body/section/article/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/ul/li[6]").click()
driver.find_element_by_css_selector('btnFooter.btnTransfers').click()
driver.find_element_by_class_name("tile col-mobile-1-2 col-1-2 transferListTile").click()
content = driver.find_elements_by_class_name("tileContent")
content[1].click()

driver.find_element_by_class_name("btn-text").click()
driver.find_element_by_xpath("/html/body/section/article/div[2]").click()
driver.find_element_by_xpath("/html/body/section/article/section/section[2]/div/div/div[3]/div[2]/button").click()
driver.find_element_by_css_selector('standard.call-to-action.bidButton').click()
driver.find_element_by_class_name("slick-slide slick-current slick-active").click()

