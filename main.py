from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

follower_list = []
username = "your username"
password = "your password"

# log in part 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")
user_name = driver.find_element("name", "username")
for char in username:
    user_name.send_keys(char)
    time.sleep(0.1)
user_password = driver.find_element("name", "password")
for char in password:
    user_password.send_keys(char)
    time.sleep(0.1)
login = driver.find_element("xpath", "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
login.click()
time.sleep(10)

# opens another tab after logging in
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get("https://www.instagram.com/your username/followers/")
time.sleep(20)
# finds people who follow you 
scroll_box = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]")
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    time.sleep(1)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)
    link1 = scroll_box.find_elements("tag name", "a")
    follower = [name.text for name in link1 if name != '']

# opens another tab
driver.execute_script("window.open('about:blank', 'thirdtab');")
driver.switch_to.window("thirdtab")
driver.get("https://www.instagram.com/jiajunkk/following/")
time.sleep(20)
# finds people who you follow 
scroll_box = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]")
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    time.sleep(1)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)
    link2 = scroll_box.find_elements("tag name", "a")
    following = [name.text for name in link2 if name != '']
# print out people who don't follow back you 
for user in following:
    if user not in follower:
        print(user)
# close the chrom after 10 seconds 
time.sleep(10)
