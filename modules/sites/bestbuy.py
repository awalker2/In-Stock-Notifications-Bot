from modules.site_base import SiteBase
from modules.sms import SMS

class BestBuy(SiteBase):
    def __init__(self, url: str, sms: SMS, browser_profile: str, polling_time: int):
        super().__init__(url, sms, browser_profile, polling_time)

    def try_buy_item(self) -> bool:
        try:
            self.driver.refresh()
            cart_button = self.driver.find_element_by_xpath("//button[text()='Add to Cart']")
            cart_button.click()
            self.sms.send_alert(f'BEST BUY ITEM ADDED TO CART: {self.url}')
            # cart_button = self.driver.find_element_by_xpath("//button[text()='Go to Cart']")
            # cart_button.click()
            return True
        except Exception as e:
            print(e)
            return False

