import json
import time
from modules.sms import SMS
from modules.sites.bestbuy import BestBuy

with open('config.json', 'r') as f:
    config_json = json.load(f)

# Twilio config
twilio_config = config_json["twilio"]
account_sid = twilio_config["accountSID"]
auth_token = twilio_config["authToken"]
phone_to = twilio_config["phoneTo"]
phone_from = twilio_config["phoneFrom"]
# Chrome config
sites = config_json["sites"]
browser_profile = sites["chromeProfile"]
# Best Buy config
url = sites["bestBuy"]["urls"][0]
polling_delay = sites["bestBuy"]["pollingDelay"]

sms = SMS(account_sid, auth_token, phone_to, phone_from)

best_buy = BestBuy(url, sms, browser_profile, polling_delay)
while(True):
    best_buy.try_buy_item()
    time.sleep(polling_delay)