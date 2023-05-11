from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from csvwriter import write_to_csv
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://mytestingthoughts.com/Sample/home.html"
driver.get(url)
driver.implicitly_wait(5)


soup = BeautifulSoup(driver.page_source, 'html.parser')


form = {"fname": "test1",
        "lname": "lname test",
        "gender": "Male",
        "hobby": "Swimming",
        "dept": "MCTC",
        "user": "jonathan",
        "pass": "Pass@123",
        "email": "abc@gmail.com",
        "contact": "(415)8265413",
        "Add": "abc street, pune"
        }

first_n = driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[1]/div/div/input')
first_n.send_keys(form["fname"])

last_n = driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[2]/div/div/input')
last_n.send_keys(form["lname"])

gender = driver.find_element(By.XPATH, f'//*[@id="inlineRadio{form["gender"]}"]')
gender.click()

hobbies = Select(driver.find_element(By.XPATH, f'//*[@id="exampleFormControlSelect2"]'))
hobbies.select_by_visible_text(form["hobby"])

dept = Select(driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[5]/div/div/select'))
dept.select_by_visible_text(form["dept"])

user_inp = driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[6]/div/div/input')
user_inp.send_keys(form["user"])

pass_inp = driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[7]/div/div/input')
pass_inp.send_keys(form["pass"])

cpass_inp = driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[8]/div/div/input')
cpass_inp.send_keys(form["pass"])

email = driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[9]/div/div/input')
email.send_keys(form["email"])

contact = driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[10]/div/div/input')
contact.send_keys(form["contact"])

add = driver.find_element(By.XPATH, '//*[@id="exampleFormControlTextarea1"]')
add.send_keys(form["Add"])


submit = driver.find_element(By.CSS_SELECTOR, '#contact_form > fieldset > div:nth-child(15) > div > button')#//*[@id="contact_form"]/fieldset/div[13]/div/button"]')
submit.click()

sleep(10)