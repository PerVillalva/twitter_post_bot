from selenium import webdriver
from time import sleep
from bot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

bot.twitter_at_provider()

sleep(10)

bot.driver.quit()