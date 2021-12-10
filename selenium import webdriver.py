from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time


wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wd.get("https://www.thesparksfoundationsingapore.org/")
os.system('cls' if os.name == 'nt' else 'clear')

print(wd.title)
print(wd.current_url)

print("\nTest Cases")

# TestCase 1: Title
print("\nTestCase 1:")
if wd.title:
    print("\nTitle Verified Successfully: ", wd.title)
else:
    print("\nTitle Verification Failed!\n")

# TestCase 2: To find logo of the webpage
print("\nTestCase 2:")
try:
    wd.find_element(By.XPATH, '//[@id="home"]/div/div[1]/h1/a/').click()
    print('Success! The logo is present\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo is present!\n')

# TestCase 3: Check if navbar appears
print("TestCase 3:")
try:
    wd.find_element(By.CLASS_NAME, "navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

# TestCase 4: Home button
print("TestCase 4:")
try:
    wd.find_element(By.PARTIAL_LINK_TEXT,"The Sparks Foundation").click()
    print("Home link is working!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

# TestCase 5: About Us Page
print("TestCase 5:")
try:
    wd.find_element(By.LINK_TEXT, 'About Us').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, 'Corporate Partners').click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

# TestCase 6: Policy page
print('TestCase 6:')
try:
    wd.find_element(By.LINK_TEXT, 'Policies and Code').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, "Policies").click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, 'Code of Ethics and Conduct').click()
    time.sleep(3)
    print('Policy Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 7: Programs page
print('TestCase 7:')
try:
    wd.find_element(By.LINK_TEXT, 'Student Scholarship Program').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, "Student Mentorship Program").click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, 'Student SOS Program').click()
    time.sleep(3)
    print('Programs Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 8: Check the Contact us Page
print("TestCase 8:")
try:
    wd.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(3)
    info = wd.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    # print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Information is Correct!')
    else:
        print('Contact Information is Incorrect!')
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")

# TestCase 9: Links Page
print("TestCase 9:")
try:
    wd.find_element(By.LINK_TEXT, 'LINKS').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, 'Software & App').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, 'AI in Education').click()
    time.sleep(3)
    print('LINKS Verfication Successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# TestCase 10: Check the Form
print("TestCase 10:")
try:
    wd.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, 'Why Join Us').click()
    time.sleep(3)
    wd.find_element(By.NAME, 'Name').send_keys('Harsh Patel')
    time.sleep(3)
    wd.find_element(By.NAME, 'Email').send_keys('180303105211@paruluniversity.ac.in')
    time.sleep(3)
    select = Select(wd.find_element(By.CLASS_NAME, 'form-control'))
    time.sleep(3)
    select.select_by_visible_text('Intern')
    time.sleep(3)
    wd.find_element(By.CLASS_NAME, 'button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

# TestCase 11: Programs Page
print("TestCase 11:")
try:
    wd.find_element(By.LINK_TEXT, 'Programs').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT, 'Workshops').click()
    time.sleep(3)
    print('Programs Page Verfication Successful!\n')
except NoSuchElementException:
    print("Programs Page Verification Failed!\n")

# TestCase 12: Links Page
print("TestCase 12:")
try:
    wd.find_element(By.CLASS_NAME, "button-w3layouts")
    print("Know More Button Verification Successful!\n")
except NoSuchElementException:
    print("Know More Button Verification Failed!\n")
cls=wd.close()