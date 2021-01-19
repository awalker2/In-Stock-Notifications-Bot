from abc import ABC, abstractmethod
from selenium import webdriver
from modules.sms import SMS

class SiteBase(ABC):
    @abstractmethod
    def __init__(self, url: str, sms: SMS, browser_profile: str, polling_time: int):
        self.sms = sms

        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={browser_profile}")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(polling_time)
        
        self.url = url
        self.driver.get(url)

    @abstractmethod
    def try_buy_item(self) -> bool:
        pass