from selenium import webdriver
import time
import sys 
import subprocess
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import smtplib
from email.message import EmailMessage

email_address = "robbebaeyens.it@gmail.com"
email_password = ""



date = 0
datum = '01'

current_prices = [20, 31, 64, 26, 153, 17, 153, 26]

self = webdriver.Chrome()
options =Options()
options.add_argument("--headless")
self = webdriver.Chrome(options=options)

def sendmail(price, date):
    msg = EmailMessage()
    msg['Subject'] = "Flight price"
    msg['From'] = email_address
    msg['To'] = "robbebaeyenspk@gmail.com"
    msg.set_content("The flight price for " + date + "Februari has changed.\nThe new price is: " + price)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def geturl(datum):
    url = 'https://www.cheaptickets.be/vluchtresultaten?adt=1&chd=0&cls=Y&inf=0&out0_dep_all=false&out0_arr_all=false&out0_dep=EIN&out0_arr=LIS&out0_date=2023-02-' + datum
    return url

def getprice(url, date):
    if(date < 8):
        date = date+1
        datum = '0' + str(date)
        self.get(url)
        time.sleep(1)
        if(date == 1):
            self.find_element("xpath", '/html/body/div[2]/div/div[2]/footer/button').click()
        time.sleep(1)
        clicked = False
        while (clicked != True):
            try:
                price = self.find_element("xpath", '/html/body/div[1]/div/div/div[1]/div/section/div[6]/div/div/div[1]/div[1]/div[2]/div[3]/div[1]/div/div[2]').text
                clicked = True
            except NoSuchElementException:
                time.sleep(1)

        

        print(price)
        with open(sys.argv[1], 'a') as output:
            output.write(str(date) + " Februari = " + price + "\n")
        datum = '0' + str(date+1)
        getprice(geturl(datum), date)
    
getprice(geturl(datum), date)
with open(sys.argv[1], 'a') as output:
    output.write(f"_______________\n")
subprocess.Popen(R'explorer ""C:\Users\robbe\OneDrive\Documenten\IT-projects\Webscraping\LisbonPrices\prices.txt""')
