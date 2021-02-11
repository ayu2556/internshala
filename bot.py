from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass
import sys
import msvcrt
 
 
LOGIN_URL = 'https://www.facebook.com/login.php'

 
class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            # Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=option)
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load
 
 
 
    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too
 
        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up
 
 
if __name__ == '__main__':
    # Enter your login credentials here
    user=input("enter number or email: ")
    passwd=getpass.getpass()
    fb_login = FacebookLogin(email=user, password=passwd, browser='Chrome')
    fb_login.login()
    graph = facebook.GraphAPI(access_token)
    friends = graph.get_object("me/friends")
    for friend in friends['data']:
        
        
        print("{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id']))
