from .Website_controller import Website_controller
from getpass import getpass
from .helper import read_creds
import sys


def open_url(driver, url):
    """USED
    Makes the browser open an url through the driver object in the webcontroller.

    :param driver: object within website_controller that can controll the driver.
    :param url: A link to a website.

    """
    driver.get(url)
    return driver


def login(hardcoded):
    """Performs login of user into Radboud Sports Center website.
    Returns the website_controller  object.

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    username, pswd = get_credentials(hardcoded)

    website_controller = Website_controller()
    website_controller.driver = open_url(website_controller.driver, hardcoded.login_url)
    website_controller.driver.implicitly_wait(6)
    username_input = website_controller.driver.find_element_by_id("login_field")
    password_input = website_controller.driver.find_element_by_id("password")

    username_input.send_keys(username)
    password_input.send_keys(pswd)
    website_controller.driver.implicitly_wait(6)

    website_controller.driver.find_element_by_css_selector(".btn-primary").click()
    return website_controller


def two_factor_login(two_factor_code, website_controller):
    """USED
    Performs login of user into Radboud Sports Center website.
    Returns the website_controller  object.

    :param hardcoded: An object containing all the hardcoded settings used in this program.
    :param two_factor_code: param website_controller:
    :param website_controller: Object controlling the browser. 

    """
    two_factor_input = website_controller.driver.find_element_by_id("otp")

    two_factor_input.send_keys(two_factor_code)
    website_controller.driver.implicitly_wait(6)

    website_controller.driver.find_element_by_css_selector(".btn-primary").click()
    return website_controller


def get_credentials(hardcoded):
    """Gets the Radboud Sports Center credentials from a hardcoded file and asks the user for
    them if they are not found.
    
    # TODO: export the credentials of the user if the user grants permission for that.

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    if hardcoded.use_cred_file:
        username, pswd = read_creds(hardcoded)
    else:
        username = get_username()
        pswd = get_pswd()
    return username, pswd


def get_username():
    """Gets the username for the Radboud Sports Center login and returns it."""
    username = getpass("Website Username:")

    return username


def get_pswd():
    """Gets the password for the Radboud Sports Center login and returns it."""
    pswd = getpass("Website Password:")
    return pswd


def click_element_by_xpath(website_controller, xpath):
    """Clicks an html element based on its xpath.

    :param website_controller: Object controlling the browser. Object that controls the browser.
    :param xpath: A direct link to an object in an html page.

    """
    source_element = website_controller.driver.find_element_by_xpath(xpath)
    if "firefox" in website_controller.driver.capabilities["browserName"]:
        scroll_shim(website_controller.driver, source_element)

    # scroll_shim is just scrolling it into view, you still need to hover over it to click using an action chain.
    actions = ActionChains(website_controller.driver)
    actions.move_to_element(source_element)
    actions.click()
    actions.perform()
    return website_controller
