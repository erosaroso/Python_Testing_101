from selenium import webdriver #BusinessAutomation
import time


url_tutorialsninja = "http://www.tutorialsninja.com/demo/"

#initialize webdriver
tutorialsninja = webdriver.Chrome()
tutorialsninja.maximize_window()
#URL/Website
tutorialsninja.get(url_tutorialsninja)
time.sleep(5)

#Register Account 

if tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a"):
    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a").click() 
    print("My Account......")
    time.sleep(2)
    if tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a"):
        tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a").click()
        print("Welcome to Registration Page.....")
        time.sleep(3)
        #Create Account
        

    else:
        print("Error 101...")

else:
    print("Error 101...")




#Phone and PDAs
if tutorialsninja.find_element_by_css_selector("#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a"):
    tutorialsninja.find_element_by_css_selector("#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a").click()
    print('Successfully Clicked the Phone and PDAs.........')
    time.sleep(2)
    if tutorialsninja.find_element_by_css_selector("#content > h2"):
        tutorialsninja.find_element_by_css_selector("#content > h2").click()
        print("Phone and PDAs Header were showed.....")
        time.sleep(2)
    
    else:
        print("Phone and PDAs Header were not recognized.... ")

else:
    print("Unsucessfully Click the Phone and PDAs...... Error 101")


#Choosing an iPhone

if tutorialsninja.find_element_by_css_selector("#content > div:nth-child(3) > div:nth-child(2) > div > div.image > a > img"):
    tutorialsninja.find_element_by_css_selector("#content > div:nth-child(3) > div:nth-child(2) > div > div.image > a > img").click()
    print("Successfully Clicked the iphone..... ")
    time.sleep(2)

else:
    print("Unsuccessfully click the iphone.... .Error 101")


#find id
#find name 
#find xpath 
#find css selector