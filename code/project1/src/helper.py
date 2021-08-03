import getpass
import os
from selenium.webdriver.common.action_chains import ActionChains


def add_two(x):
    """Adds two to an incoming integer.

    :param x: 

    """
    return x + 2


def do_browser():
    """Creates a browser object."""
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Firefox(executable_path=r"firefox_driver/geckodriver")


def read_creds(hardcoded):
    """Reads username and password for Radboud University Sports Center from credentials file,
    if the file exists, asks the user to manually enter them if the file is not found.
    Returns two strings representing the username and password for the Radboud University Sports Center login.
    
    TODO: verify this is not a duplicate method.

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    get_creds_if_not_exist(hardcoded)
    with open(hardcoded.cred_path, "r") as f:
        lines = []
        for line in f:
            lines.append(line)
    username = lines[0][:-1]
    pswd = lines[1]
    return username, pswd


def get_creds_if_not_exist(hardcoded):
    """Asks the user to enter the username and password for the login to the
    Radboud Universitiy Sports Center login.
    
    TODO: ask user to include 'read' before username and password,
    to indicate that they read the source code before entering their username
    and password (and verified that it is not shared). Give them a warning about
    security otherwise.

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    if not os.path.isfile(hardcoded.cred_path):
        username = getpass.getpass(prompt="What is your username for GitHub?")
        pwd = getpass.getpass(prompt="What is your password for GitHub?")

        f = open(hardcoded.cred_path, "a")
        f.write(f"{username}\n")
        f.write(pwd)
        f.close()


def get_labels_from_issues(issues):
    """

    :param issues: [List] of Issue objects containing the data (e.g. title, comments) of an issue. 

    """
    labels = []
    for issue in issues:
        for label in issue.labels:
            labels.append(label.replace("%20", " "))
    unique_labels = list(set(labels))
    print(f"unique_labels={unique_labels}")
    return unique_labels


def source_contains(website_controller, string):
    """USED
    Evaluates complete html source of the website that is being controlled, to determine
    if it contains the incoming string.
    Returns true if the string is found in the html source of the website, false if it is not found.

    :param website_controller: Object controlling the browser. Object that controls the browser.
    :param string: Set of characters that is searched for in the html code.

    """
    source = website_controller.driver.page_source
    source_contains_string = string in source
    return source_contains_string


def get_browser_drivers(hardcoded):
    """USED
    Installs wget and then uses that to download the firefox and chromium browser controller drivers.

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    os.system("yes | sudo apt install wget")
    if not file_is_found(
        f"{hardcoded.firefox_driver_folder}/{hardcoded.firefox_driver_filename}",
        hardcoded,
    ):
        get_firefox_browser_driver(hardcoded)
        install_firefox_browser()
    if not file_is_found(
        f"{hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_filename}",
        hardcoded,
    ):
        get_chromium_browser_driver(hardcoded)


def file_is_found(filepath, hardcoded):
    """

    :param filepath: 
    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    if os.path.isfile(filepath):
        return True
    else:
        return False


def get_firefox_browser_driver(hardcoded):
    """USED
    Creates a folder to store the firefox browser controller downloader and then downloads it into that.

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    # TODO: include os identifier and select accompanying file
    os.system(f"mkdir {hardcoded.firefox_driver_folder}")
    curl_firefox_drive = f"wget -O {hardcoded.firefox_driver_folder}/{hardcoded.firefox_driver_tarname} {hardcoded.firefox_driver_link}"
    os.system(curl_firefox_drive)
    # unpack_firefox_driver = (
    #    f"tar -xf {hardcoded.firefox_driver_folder}/{hardcoded.firefox_driver_tarname}"
    # )
    unpack_firefox_driver = f"tar -xf {hardcoded.firefox_driver_folder}/{hardcoded.firefox_driver_tarname} -C {hardcoded.firefox_driver_folder}/"
    print(f"unpacking with:{unpack_firefox_driver}")
    os.system(unpack_firefox_driver)


def install_firefox_browser():
    """USED"""
    install_firefox_browser = f"yes | sudo apt install firefox"
    print(f"install_firefox_browser:{install_firefox_browser}")
    os.system(install_firefox_browser)


def get_chromium_browser_driver(hardcoded):
    """USED
    Creates a folder to store the chromium browser controller downloader and then downloads it into that.
    TODO: include os identifier and select accompanying file

    :param hardcoded: An object containing all the hardcoded settings used in this program.

    """
    # mak dir
    os.system(f"mkdir {hardcoded.chromium_driver_folder}")
    # get the zip
    curl_chromium_drive = f"wget -O {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_tarname} {hardcoded.chromium_driver_link}"
    os.system(curl_chromium_drive)
    # unpak the zip
    unpack_chromium_driver = f"unzip -d  {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_filename} {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_tarname}"
    os.system(unpack_chromium_driver)

    # move file one dir up
    move_chromium_driver = f"mv  {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_filename}/{hardcoded.chromium_driver_unmodified_filename} {hardcoded.chromium_driver_folder}"
    print(move_chromium_driver)
    os.system(move_chromium_driver)
    # remove unpacked dir
    cleanup = (
        f"rm -r {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_filename}"
    )
    print(cleanup)
    os.system(cleanup)

    # remove zip file
    cleanup = (
        f"rm -r {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_tarname}"
    )
    print(cleanup)
    os.system(cleanup)

    # rename driver file name to include hardcoded version name
    rename_chromium_driver = f"mv  {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_unmodified_filename} {hardcoded.chromium_driver_folder}/{hardcoded.chromium_driver_filename}"
    print(rename_chromium_driver)
    os.system(rename_chromium_driver)


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


def scroll_shim(passed_in_driver, object):
    """Scrolls down till object is found.

    :param passed_in_driver: An object within the object that controls an internet browser.
    :param object: Unknown, most likely an arbitrary html object..

    """
    x = object.location["x"]
    y = object.location["y"]
    scroll_by_coord = "window.scrollTo(%s,%s);" % (x, y)
    scroll_nav_out_of_way = "window.scrollBy(0, -120);"
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)
