from selenium import webdriver
from time import sleep
from secrets import creds

config = {
    'insta_url': "https://www.instagram.com/",
}

class InstaBot:
        def __init__(self, uname, pw):
            self.username = uname;

            self.driver = webdriver.Firefox()

            self.driver.get(config['insta_url'])
            sleep(4)
            self.driver.find_element_by_xpath("//input[@name='username']").send_keys(uname)
            sleep(5)
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys(pw)
            sleep(5)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
            sleep(5)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
            sleep(5)
        
        def get_following_list(self):
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a").click()
            sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
            sleep(3)
            # sugs = self.driver.find_element_by_xpath("//h4[contains(text(),Suggestions)]")
            # sleep(3)
            # self.driver.execute_script("arguments.scrollIntoView();")
            # sleep(3)
            scroll_box = self.driver.find_element_by_xpath("//div[@role='tablist']")
            last_ht,ht=0,1
            while last_ht!=ht:
                last_ht=ht
                sleep(1)
                ht = self.driver.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
                return arguments[0].scrollHeight;""", scroll_box)
            sleep(3)
            links = scroll_box.find_elements_by_tag_name('a')
            following_list = [name.text for name in links if name != '']
            print(following_list)


myBot = InstaBot(creds['username'],creds['password'])
myBot.get_following_list()

