from tda.auth import easy_client
from tda.auth import client_from_login_flow
import json
import atexit
import discord


API_KEY = 'YOUR_API_KEY@AMER.OAUTHAP'
REDIRECT_URI = 'YOUR_REDIRECT_URI'
TOKEN_PATH = '/YOUR/TOKEN/PATH'
account_id = 0

def make_webdriver():
    # Import selenium here because it's slow to import
    from selenium import webdriver

    driver = webdriver.Chrome()
    atexit.register(lambda: driver.quit())
    return driver

c = client_from_login_flow(
    make_webdriver(),
    API_KEY,
    REDIRECT_URI,
    TOKEN_PATH,
    )
global c

user_statistics = {
    "Margaritas" :(0.1609, 4375),
    "Red Snapper" : (0.1850, 5030),
    "PorkChop": (0.4557, 12393),
    "Oxaal": (0.1663, 4523),
    "Steve 'big guy' Sheridan": (0.0322, 875)
}

def getPayouts():
    account = c.get_account(account_id=account_id).json()
    value =  float(account['securitiesAccount']['initialBalances']['accountValue'])
    msg = "Name, Percent, init, profit"
    for name in user_statistics.items():
        msg += "{0}: {1}, {2}, {3}\n".format(name, user_statistics[name][0] * 100, user_statistics[name][1], value*user_statistics[name][0] - user_statistics[name][1])
    msg += "XAIPE Dipshits!\n"
    return msg
