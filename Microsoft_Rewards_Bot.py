from selenium import webdriver
from selenium.webdriver.edge.service import Service
import google.generativeai as genai
from selenium.webdriver.common.keys import Keys
import os, sys, threading, google.generativeai as genai, time
from selenium.webdriver.edge.options import Options as EdgeOptions

genai.configure(api_key="AIzaSyBFvev9GtvNMiTyXluAJ-kDNnUGdEgwwPY")
model = genai.GenerativeModel('gemini-2.0-flash')

prompt = """
Generate one example of text which can be used to search microsoft bing, in order to get Microsoft reward points.
It can be abotu anything, related to science, politics, countries, etc.(just make it random and it should lead to me getting points)
P.S: JUST GIVE ME THE TEXT, NOTHING ELSE!!!!!!!!!!!!!!!!
Example Output: Population of Iceland
"""


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # For development, use the current working directory
        base_path = os.path.abspath(".")

    # Construct the full path to the resource
    return os.path.join(base_path, relative_path)




options = EdgeOptions()
options.add_argument("--headless=new")
edge_driver_path = resource_path("msedgedriver.exe")
service = Service(edge_driver_path)
service.creation_flags = 0x08000000
web = webdriver.Edge(options=options, service=service)




for c in range(1):
    web.get("https://www.bing.com")

    answer = model.generate_content([prompt], stream=False)
    response = answer.text.strip()

    search = web.find_element('xpath', '//*[@id="sb_form_q"]')
    search.send_keys(f'{response}')
    time.sleep(2)
    search.send_keys(Keys.ENTER)

