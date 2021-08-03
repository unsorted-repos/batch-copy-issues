from .Hardcoded import Hardcoded
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


class Website_controller:
    """Controls/commands website using selenium."""

    def __init__(self):
        """Constructs object that controlls a firefox browser.
            TODO: Allow user to switch between running browser
        in background or foreground.
        """
        self.hardcoded = Hardcoded()
        # To run Firefox browser in foreground
        self.driver = webdriver.Firefox(executable_path=r"firefox_driver/geckodriver")

        # To run Firefox browser in background
        # os.environ["MOZ_HEADLESS"] = "1"
        # self.driver = webdriver.Firefox(executable_path=r"firefox_driver/geckodriver")

        # To run Chrome browser in background
        # options = webdriver.ChromeOptions();
        # options.add_argument('headless');
        # options.add_argument('window-size=1200x600'); // optional
