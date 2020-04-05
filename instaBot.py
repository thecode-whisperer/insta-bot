from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import random


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.login()

    def random_number_generator(self, x, y):
        random_number = random.randrange((x * 100), (y * 100)) / 100
        return random_number

    def login(self):
        self.driver.get('https://instagram.com/accounts/login')
        sleep(self.random_number_generator(2, 4))
        self.driver.find_element_by_name('username').send_keys(self.username)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        sleep(self.random_number_generator(2, 5))

    def nav_user(self, user):
        sleep(self.random_number_generator(2, 6))
        self.driver.get('https://instagram.com/' + user)

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

    def unfollow_user(self, user):
        try:
            self.nav_user(user)
            sleep(self.random_number_generator(3, 5))
            following_btn = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
            following_btn.click()
            sleep(self.random_number_generator(2, 4))
            unfollow_btn = self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")[0]
            unfollow_btn.click()
        except:
            pass

    def like_user_post(self, user, limit=3):
        try:
            self.nav_user(user)
            photo = self.driver.find_element_by_class_name('eLAPa')
            photo.click()
            sleep(self.random_number_generator(2, 7))
            for _ in range(limit):
                like_btn = self.driver.find_elements_by_class_name('wpO6b ')[1]
                sleep(self.random_number_generator(2, 5))
                like_btn.click()
                next_btn = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")
                sleep(self.random_number_generator(1, 3))
                next_btn.click()
                sleep(self.random_number_generator(3, 6))
        except:
            pass
        
    def like_tag_post(self, tag, limit=10):
        self.driver.get('https://instagram.com/explore/tags/' + tag)
        sleep(self.random_number_generator(2, 4))
        photo = self.driver.find_element_by_class_name('eLAPa')
        photo.click()
        sleep(self.random_number_generator(3, 5))
        for _ in range(limit):
            like_btn = self.driver.find_elements_by_class_name('_8-yf5 ')[4]
            like_btn.click()
            sleep(self.random_number_generator(2, 4))
            next_btn = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")
            next_btn.click()
            sleep(self.random_number_generator(3, 7))

    def user_followers(self, user, limit=30):
        self.nav_user(user)
        sleep(self.random_number_generator(2, 4))
        followers_btn = self.driver.find_element_by_xpath(f"//a[contains(@href, '/{user}/followers/')]")
        followers_btn.click()
        sleep(self.random_number_generator(2, 4))
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

    def follow_users(self, users):
        for user in users:
            self.smart_follow(user)
    
    def like_users_posts(self, users):
        for user in users:
            self.like_user_post(user)

    def unfollow_users(self, users):
        for user in users:
            self.unfollow_user(user)
    
    def smart_follow_check(self, user):
        try:
            self.nav_user(user)
            followers = self.driver.find_element_by_xpath(f'//a[contains(@href, "{user}/followers")]/span')
            string = followers.text
            string = string.replace(',', '')
            followers_num = int(string)
            following = self.driver.find_element_by_xpath(f'//a[contains(@href, "{user}/following")]/span')
            string1 = following.text
            string1 = string1.replace(',', '')
            following_num = int(string1)
            if following_num > followers_num:
                return True
            return False
        except:
            pass

    # Follows a user if they are following more people than they have followers
    def smart_follow(self, user):
        if self.smart_follow_check(user) == True:
            self.follow_user(user)

    # Comments on the first photo with a specified hastag
    def comment_tag_post(self, tag, comment):
        self.driver.get(f'https://www.instagram.com/explore/tags/{tag}/')
        sleep(self.random_number_generator(2, 4))
        photo = self.driver.find_element_by_class_name('eLAPa')
        photo.click()
        sleep(2)
        comment_button = self.driver.find_elements_by_class_name('_8-yf5 ')[5]
        comment_button.click()
        sleep(2)
        comment_field = self.driver.find_element_by_class_name('Ypffh')
        comment_field.send_keys(comment)
        sleep(2)
        post = self.driver.find_element_by_xpath('//button[contains(text(), "Post")]')
        post.click()

    #Comments on the first photo of a user    
    def comment_user_post(self, user, comment):
        try:
            self.nav_user(user)
            sleep(self.random_number_generator(2, 4))
            photo = self.driver.find_element_by_class_name('eLAPa')
            photo.click()
            sleep(2)
            comment_button = bot.driver.find_element_by_class_name('_JgwE')
            comment_button.click()
            sleep(2)
            comment_field = self.driver.find_element_by_class_name('Ypffh')
            sleep(2)
            comment_field.send_keys(comment)
            sleep(2)
            post = self.driver.find_element_by_xpath('//button[contains(text(), "Post")]')
            post.click()
        except:
            pass
    
    # Comments on the first photo of mulitple users
    def comment_users_posts(self, users, comment):
        for user in users:
            self.comment_user_post(user, comment)

    # Likes the first 3 posts of the newest followers of a specified user 
    def like_user_followers(self, user, limit=30):
        users = self.user_followers(user, limit=limit)
        self.like_users_posts(users)

    # Comments on the first post of the newsest followers of a specified user
    def comment_user_followers(self, user, comment, limit=30):
        users = self.user_followers(user, limit=limit)
        self.comment_users_posts(users, comment)

    # Follow the newest followers of a specified user
    def follow_user_followers(self, user, limit=30):
        users = self.user_followers(user, limit=limit)
        self.follow_users(users)
    
    def user_photo_likers(self, user, limit=30):
        self.nav_user(user)
        sleep(self.random_number_generator(2, 4))
        photo = self.driver.find_element_by_class_name('eLAPa')
        photo.click()
        sleep(self.random_number_generator(2, 5))
        button = self.driver.find_elements_by_class_name('_8A5w5')[1]
        sleep(1)
        button.click()
        sleep(self.random_number_generator(2, 4))
        fBody = self.driver.find_element_by_xpath('//div[@style="height: 356px; overflow: hidden auto;"]')
        sleep(2)
        likers_list = []
        for i in range(3):
            scroll = 0
            while scroll < 10:
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                scroll += 1
                sleep(1)
            sleep(1)
            for i in range(limit):
                liker = self.driver.find_elements_by_class_name('KV-D4')[i+1]
                if liker.text not in likers_list:
                    likers_list.append(liker.text)
        print(likers_list)
        return likers_list
    
if __name__ == "__main__":
    
    bot = InstagramBot(YourUsername, YourPassword)
