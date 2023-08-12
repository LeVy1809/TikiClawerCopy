## Model của app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller 
from unidecode import unidecode

class TikiClawer:
	def __init__(self) -> object:
		self.hello = "Welcome to our Training"
		