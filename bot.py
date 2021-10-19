from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_PASSWORD = os.getenv("USER_PASSWORD")
TWITTER_EMAIL = os.getenv("USER_EMAIL")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/results")
        sleep(2)
        consent_btn = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        consent_btn.click()

        go_btn = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()

        sleep(40)

        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up, self.down)

    def twitter_at_provider(self):
        self.driver.get('https://twitter.com/')
        sleep(5)

        self.have_account = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/div[4]/span')
        self.have_account.click()

        self.twitter_log_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a')
        self.twitter_log_in.click()
        sleep(6)
        self.email = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        self.email.send_keys(f"{TWITTER_EMAIL}")
        self.next_email = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[2]/div/div')
        self.next_email.click()
        sleep(6)
        self.password = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
        self.password.send_keys(f"{TWITTER_PASSWORD}")

        self.log_in_btn = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span')
        self.log_in_btn.click()

        sleep(3)

        self.text_twitter = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        self.text_twitter.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 150down/10up")

        self.tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        self.tweet.click()
