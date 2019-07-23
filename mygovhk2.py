from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from selenium.webdriver.remote.webelement import WebElement


# Open Chrome and navigate to mygovhk
browser = webdriver.Chrome('C:\\Users\\user\Desktop\chromedriver.exe')
browser.get('https://www.gov.hk/en/theme/mygovhk/')

# Click 'Login'
elem = browser.find_element_by_css_selector('#innerPageSideNav > article > div.articleHolder.recommendHolder > div > section > div.btns > div:nth-child(1) > a')
elem.click()

# Switch to newly opened window
time.sleep(4)
getHandle = browser.window_handles
print(getHandle)
browser.switch_to.window(getHandle[1])


# Input Username
elem = browser.find_element_by_css_selector('#myid')

elem.send_keys('CL')
elem.send_keys('EM')
elem.send_keys('EN')
elem.send_keys('TC')
elem.send_keys('HA')
elem.send_keys('N0')
elem.send_keys('1')

elem.submit()


# Input Password
elem = browser.find_element_by_css_selector('#password')

elem.send_keys('***password***')
elem.submit()

# Click 'Bills'
elem = browser.find_element_by_css_selector('#SMB')
elem.click()

# Click 'Details'
elem = browser.find_element_by_css_selector('#showDetail_T0000000000000180996')
elem.click()

# Switch to newly opened window
getHandle = browser.window_handles
browser.switch_to_window(getHandle[2])

# Download file

time.sleep(5)
browser.find_element_by_xpath('//*[@title="View / Print the latest demand note"]').click()
time.sleep(5)


# Logout
getHandle = browser.window_handles
browser.switch_to_window(getHandle[1])
elem = browser.find_element_by_css_selector('#menu_logout_text')
elem.click()

# Create a text/plain message

msg = email.mime.multipart.MIMEMultipart()
msg['Subject'] = 'School loan!'
msg['From'] = 'clementchan0401@gmail.com'
msg['To'] = 'clementchan0401@gmail.com'

# The main body is just another attachment

body = email.mime.text.MIMEText("""Attached is the Government Loan document! \n\n Regards, \n Clem""")
msg.attach(body)

# PDF attachment

keyword = "NLSFT"
for fname in os.listdir("C:\\Users\\user\Downloads"):
    if keyword in fname:
        fullpath = os.path.join("C:\\Users\\user\Downloads", fname)
        filename = fullpath
        fp=open(filename,'rb')
        att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)


# Send via Gmail server

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login('clementchan0401@gmail.com','***password***')
s.sendmail('clementchan0401@gmail.com',['clementchan0401@gmail.com'], msg.as_string())
s.quit()

# Exit browsers

browser.quit()





















