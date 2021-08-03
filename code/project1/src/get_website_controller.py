import numpy as np
import os
import time
import pickle

from .Website_controller import Website_controller

# from .ask_user_input import ask_user_choices
from .ask_user_input import ask_two_factor_code
from getpass import getpass
from .helper import get_browser_drivers

from .helper import read_creds
from .helper import source_contains

from .control_website import open_url
from .control_website import login
from .control_website import two_factor_login

from selenium.webdriver.common.action_chains import ActionChains
import sys


def get_website_controller(hc):
    """USED
    Monitors the subscription availabilities of the Radboud University Sports Centre.
    Gets the desired user schedule and enrolls the user for the desired schedule when
    available.

    :param hc: An object containing all the hardcoded settings used in this program.

    """
    # get browser drivers
    get_browser_drivers(hc)

    # login GitHub
    website_controller = login_github(hc)
    return website_controller


def login_github(hardcoded):
    """USED
    Gets the issues from a github repo. Opens a separate browser instance and then
    closes it again.
    Returns the rsc_data object that contains the parsed availability of the relevant activities.

    TODO: determine and document how get_next_activity manages the difference between primary and secondary
    choice.

    :param hardcoded: An object containing all the hardcoded settings used in this program.
    :param user_choices: Object that contains the choices/schedule that user wants to follow.

    """
    # check if pickle session works
    has_pickled, website_controller = check_pickle_website_controller(hardcoded)
    # exit()
    if not has_pickled:
        # login
        website_controller = login(hardcoded)

        # check if 2factor
        if source_contains(website_controller, "<h1>Two-factor authentication</h1>"):

            # if 2 factor ask code from user
            two_factor_code = ask_two_factor_code()

            # enter code
            two_factor_login(two_factor_code, website_controller)

        # Go to source repository
        website_controller.driver = open_url(
            website_controller.driver, hardcoded.source_repo_url
        )

        # pickle browser session to prevent having to login 2fac each test run
        # TypeError: cannot pickle '_io.TextIOWrapper' object
        # pickle_store_website_controller(hardcoded, website_controller)

    # close website controller
    # website_controller.driver.close()

    return website_controller


def check_pickle_website_controller(hardcoded):
    """USED

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    # check if pickle exists
    if os.path.isfile(hardcoded.pickle_website_controller_filename):
        # get website controller
        website_controller = pickle_load_website_controller(hardcoded)

        # check if session is accessible
        website_controller.driver = open_url(
            website_controller.driver, hardcoded.source_repo_url
        )
        if source_contains(
            website_controller, '<span class="d-none d-md-block">New issue</span>'
        ):
            return True, website_controller
        else:
            return False, None
    else:
        return False, None


def pickle_store_website_controller(hardcoded, website_controller):
    """

    :param hardcoded: An object containing all the hardcoded settings used in this program.
    :param website_controller: Object controlling the browser.

    """
    # Save a dictionary into a pickle file.
    pickle.dump(
        website_controller, open(hardcoded.pickle_website_controller_filename, "wb")
    )


def pickle_load_website_controller(hardcoded):
    """

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    # Save a dictionary into a pickle file.
    website_controller = pickle.load(
        open(hardcoded.pickle_website_controller_filename, "wb")
    )
    return website_controller
