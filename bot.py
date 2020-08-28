from selenium import webdriver
from time import sleep
class InstaBot:
    def __init__(self, username_email, password):
        limit = int(input("Number of Follows (result will be x2): "))
        repeats = 0
        while repeats < limit:
            # calls webdriver from folder called "drivers", code can be changed based on location of webdriver
            self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
            # opens url, url can be substituted based on preference
            self.driver.get("https://www.instagram.com/")
            sleep(2)

            # enters username and password that was inputed whie calling the class; clicks "login" button
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username_email)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
            sleep(4)

            # finds and clicks "not now" buttons when prompted about notifications and location settings
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
            sleep(2)

            # scrolls down instagram feed to "suggested" section and follows first two accounts available
            sugs = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[3]/div/div/div[1]/span")
            self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[3]/div/div/div[2]/div/div/div/ul/li[3]/div/div/div/div/button[2]").click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[3]/div/div/div[2]/div/div/div/ul/li[4]/div/div/div/div/button[2]").click()
            sleep(2)

            # closes browser and adds 1 to repeat in order to refresh the page and loop function
            self.driver.close()
            repeats = repeats + 1
            sleep(1)

# Calls InstaBot, substitute examples for your own username and password
InstaBot(username_email="", password="")