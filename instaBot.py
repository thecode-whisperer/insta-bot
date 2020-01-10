from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.login()
    
    //LOGIN TO INSTAGRAM
    def login(self):
        self.driver.get('https://instagram.com/accounts/login')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        sleep(3)
        
    //NAVIGATE TO USER
    def nav_user(self, user):
        sleep(1)
        self.driver.get('https://instagram.com/' + user)

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

    def unfollow_user(self, user):
        try:
            self.nav_user(user)
            sleep(2)
            following_btn = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
            following_btn.click()
            sleep(2)
            unfollow_btn = self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")[0]
            unfollow_btn.click()
        except:
            pass

    //LIKE A USERS POSTS
    def like_user_post(self, user, limit=3):
        try:
            self.nav_user(user)
            photo = self.driver.find_element_by_class_name('eLAPa')
            photo.click()
            sleep(2)
            for i in range(limit):
                like_btn = self.driver.find_elements_by_class_name('afkep')[1]
                like_btn.click()
                next_btn = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")
                next_btn.click()
                sleep(1)
        except:
            pass
        
    //LIKE POSTS WITH A CERTAIN HASHTAG    
    def like_tag_post(self, tag, limit=10):
        self.driver.get('https://instagram.com/explore/tags/' + tag)
        sleep(2)
        photo = self.driver.find_element_by_class_name('eLAPa')
        photo.click()
        sleep(2)
        for i in range(limit):
            like_btn = self.driver.find_element_by_class_name('afkep')
            like_btn.click()
            next_btn = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")
            next_btn.click()
            sleep(1)

    //PRINTS AND RETURNS A LIST OF A PERSONS FOLLOWERS
    def user_followers(self, user, limit=10):
        self.nav_user(user)
        sleep(2)
        followers_btn = self.driver.find_element_by_xpath(f"//a[contains(@href, '/{user}/followers/')]")
        followers_btn.click()
        sleep(2)
        fBody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < 5:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            scroll += 1
            sleep(1)
        followers_list = []
        for i in range(limit):
            follower = self.driver.find_elements_by_class_name('FPmhX')[i]
            followers_list.append(follower.text)
        print(followers_list)
        return followers_list

    //FOLLOW MULTIPLE USERS
    def follow_users(self, users):
        for user in users:
            self.follow_user(user)
    
    //LIKES POSTS OF MULTIPLE USERS
    def like_users_posts(self, users):
        for user in users:
            self.like_user_post(user)
    
    //UNFOLLOW MULTIPLE USERS
    def unfollow_users(self, users):
        for user in users:
            self.unfollow_user(user)

    

bot = InstagramBot('YourUsername', 'YourPassword')
bot.like_user_post('therock')




