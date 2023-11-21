import platform
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def identify_system():
    os_name = platform.system()
    architecture = platform.machine()

    if os_name == 'Darwin':
        if architecture == 'x86_64':
            return 'MacOS amd64'
        elif architecture == 'arm64':
            return 'MacOS arm64'
        else:
            return 'MacOS (Unknown Architecture)'

    elif os_name == 'Windows':
        if architecture == 'AMD64':
            return 'Windows amd64'
        else:
            return 'Windows (Unknown Architecture)'

    elif os_name == 'Linux':
        if architecture == 'x86_64':
            return 'Linux amd64'
        else:
            return 'Linux (Unknown Architecture)'

    else:
        return 'Unknown OS and Architecture'


def detect_arch_webdriver():
    system_info = identify_system()
    if system_info == 'MacOS arm64':
        return webdriver.Chrome(service=Service('./selenium/chromedriver-mac-arm64/chromedriver'))
    elif system_info == 'MacOS amd64':
        return webdriver.Chrome(service=Service('./selenium/chromedriver-mac-x64/chromedriver'))
    elif system_info == 'Windows amd64':
        return webdriver.Chrome(service=Service('./selenium/chromedriver-win64/chromedriver.exe'))
    elif system_info == 'Linux amd64':
        return webdriver.Chrome(service=Service('./selenium/chromedriver-linux64/chromedriver'))

    raise RuntimeError("Could not detect OS")