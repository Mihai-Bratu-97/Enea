from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import socket


class YoutubeScript:
    def __init__(self):
        self.chrome = self.create_chrome() # this one saves the browser that we'll use it
        self.open_site() # open the specific website
        self.wait = WebDriverWait(self.chrome, 10) # this one wait a specific time to do something, and if that thing is not done in that time, raises an error
        self.cookies() # accepts the cookies button, if there is one
        self.youtube_searching_bar() # search videos by a specific input
        self.random_clip()
        self.open_random_clip()
        self.start_random_clip()
        self.ads()
        self.checking_youtube_premium()

    # this function test if there is connection on internet, on a specific site, based on a port of internet
    def test_internet(self):
        try:
            socket.create_connection(("youtube.com", 80))
            return True
        except OSError:
            return False

    # this function adds an option to chrome, that keeps itopen
    def create_option(self):
        options = Options()
        options.add_experimental_option("detach", True)
        return options

    # this function initialise the chrome browser, and adds the option I created above
    def create_chrome(self):
        return webdriver.Chrome(chrome_options=self.create_option())

    # this function checks if there is internet connection, and how long there isn't, tries to open youtube, an if it's, opens youtube successfully
    def open_site(self):
        self.chrome.maximize_window()
        while not self.test_internet():
            continue
        self.chrome.get("https://www.youtube.com/")
        time.sleep(1.5)

    # this function checks the cookies button, by waitting 10 seconds, and if cannot find, print a specific message
    def cookies(self):
        try:
            self.chrome.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()
        except:
            print("There is no cookie button")

    # this function tries to find the youtube search-bar, and types in a specific input, by pressing "RETURN" key after input. If cannpt do that, will print a specific message
    def youtube_searching_bar(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="search-input"]'))).click()
            self.chrome.find_element(By.XPATH, '//input[@id="search"]').send_keys("trailer 4k" + Keys.RETURN)
        except:
            print("The search-bar couldn't be accesed")

    """this function checks the internet connection at first, and if there is, will try to select a random clip from the others that appear.
    The random clips are stored into a variable, by their common "XPATH", and then their href are stored into a list, and finally, by a library called 'random', 
    selects a random clip from the list"""
    def random_clip(self):
        while not self.test_internet():
            continue
        try:
            self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@id="video-title"]')))
            searching_urls = self.chrome.find_elements(By.XPATH, '//a[@id="video-title"]')
            total_urls = []
            for searching_url in searching_urls:
                total_urls.append(searching_url.get_attribute("href"))
            random_number = random.randint(0, len(total_urls))
            get_link = total_urls[random_number]
            return get_link
        except:
            print("Couldn't find any videos!")

    """this checks the internet connection, and how long there isn't, will try to open that random clip, and if there is, will open that clip successfully
    if something will work wrong, such as the video cannot be open, a specific message will appear"""
    def open_random_clip(self):
        try:
            while not self.test_internet():
                continue
            self.chrome.get(self.random_clip())
        except:
            print("The video couldn't be open")

    # this function checks the play button, and tries to click it, and if something worked wrong, a message will appear
    def start_random_clip(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-play-button"))).click()
        except:
            print("The play button couldn't be found!")

    """this function check if there is ads, and if there is, will click on it. Otherwise, a specific message will raise. I used a 'for' to check twice, because sometimes,
    the ads is displayed twice"""
    def ads(self):
        while not self.test_internet():
            continue
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div')))
            for i in range(2):
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div'))).click()
        except:
            print("There wasn't any ads button, or just one was displayed, or there were ads that can't be skipped!")

    # this function, checks the youtube premium button, and if there is, clicks on it
    def checking_youtube_premium(self):
        while not self.test_internet():
            continue
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/tp-yt-paper-button/yt-formatted-string")))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/tp-yt-paper-button/yt-formatted-string"))).click()
        except:
            print("Youtube premium button wasn't displayed!")
