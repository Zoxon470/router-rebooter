import os
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

env = os.environ

ROUTER_URL = env.get("ROUTER_URL", "http://192.168.0.1/")
ROUTER_LOGIN = env.get("ROUTER_LOGIN", "admin")
ROUTER_PASSWORD = env.get("ROUTER_PASSWORD", "admin")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)
browser.get(ROUTER_URL)

username_input = browser.find_element_by_id("userName")
password_input = browser.find_element_by_id("pcPassword")
login_button = browser.find_element_by_id("loginBtn")

username_input.send_keys(ROUTER_LOGIN)
password_input.send_keys(ROUTER_PASSWORD)

login_button.click()

reboot_form = """
    <form action="SysRebootRpm.htm" enctype="multipart/form-data" method="get" onsubmit="return doSubmit();">
        <input name="Reboot" type="submit" class="buttonBig" value="Перезагрузить" id="reboot">
    </form>
"""

browser.execute_script("document.write('%s')" % json.dumps(reboot_form))
browser.find_element_by_id("reboot").click()

browser.quit()
print("\x1b[6;30;42m" + "The router has been successfully restarted!" + "\x1b[0m")
