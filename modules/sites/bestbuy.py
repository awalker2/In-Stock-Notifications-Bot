from modules.site_base import SiteBase
from modules.sms import SMS

class BestBuy(SiteBase):
    def __init__(self, url: str, sms: SMS, browser_profile: str, polling_time: int):
        super().__init__(url, sms, browser_profile, polling_time)

    def try_buy_item(self) -> bool:
        try:
            # Refresh and check for add button
            self.driver.refresh()
            cart_button = self.driver.find_element_by_xpath("//button[text()='Add to Cart']")
            cart_button.click()
            
            # Notify and maximize cart window
            self.sms.send_alert(f'BEST BUY ITEM ADDED TO CART: {self.url}')
            self.driver.get('https://www.bestbuy.com/cart')
            self.driver.maximize_window()
            
            # Checkout click
            checkout_button = self.driver.find_element_by_xpath("//button[text()='Checkout']")
            checkout_button.click()
            return True
        except Exception as e:
            print(e)
            return False

