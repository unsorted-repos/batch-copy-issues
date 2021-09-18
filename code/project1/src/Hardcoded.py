class Hardcoded:
    """Runs jupyter notebooks, converts them to pdf,
    exports the notebook pdfs to latex and compiles the
    latex report of the incoming project nr


    """

    def __init__(self):
        """
        Constructs an object that contains all the hardcoded values that are used in this script.
        TODO: adjust browser drivers based on the detected device type.
        """
        self.script_dir = 5
        self.firefox_driver_folder = "firefox_driver"
        self.firefox_driver_tarname = "firefox_driver.tar.gz"
        self.firefox_driver_filename = "geckodriver"
        self.firefox_driver_link = "https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz"

        self.chromium_driver_folder = "chrome_driver"
        self.chromium_driver_tarname = "chrome_driver.zip"
        self.chromium_driver_link = "https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip"
        self.chromium_driver_unmodified_filename = "chromedriver"
        self.chromium_driver_filename = "chromedriver90"

        # specify source repository
        self.source_username = "a-t-2"
        self.target_username = "one-line-deploy"
        self.source_reponame = "Setup-Raspberry-Pi-4b-tor-GitLab-website-SSH"
        self.target_reponame = "Self-host-GitLab-CI"
        self.source_repo_url = (
            f"https://github.com/{self.source_username}/{self.source_reponame}/issues"
        )

        self.pickle_website_controller_filename = "website_controller.p"

        self.use_cred_file = True
        self.cred_path = "code/project1/src/creds.txt"
        # website properties
        self.login_url = "https://github.com/login"

    def set_source_repo(self, username, reponame):
        self.source_username = username
        self.source_reponame = reponame
        self.source_repo_url = (
            f"https://github.com/{self.source_username}/{self.source_reponame}/issues"
        )

    def set_target_repo(self, username, reponame):
        self.target_username = username
        self.target_reponame = reponame
        self.target_repo_url = (
            f"https://github.com/{self.target_username}/{self.target_reponame}/issues"
        )
