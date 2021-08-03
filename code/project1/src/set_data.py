import time

from .control_website import open_url
from .get_data import get_issues
from .helper import click_element_by_xpath
from selenium.webdriver.common.keys import Keys

# get labels
def set_labels(labels, target_reponame, target_username, website_controller):
    """

    :param labels: :param labels: [List] of label objects representing the content and colour of a label.
    :param target_reponame: The repository name to which you want to copy the issues.
    :param target_username: The GitHub username that contains the repo to which you want to copy the issues.
    :param website_controller: Object controlling the browser.

    """
    for label in labels:
        # Go to: https://github.com/<username>/<repo name>/labels
        website_controller.driver = open_url(
            website_controller.driver,
            f"https://github.com/{target_username}/{target_reponame}/labels",
        )

        # click xpath:
        website_controller = click_element_by_xpath(
            website_controller,
            "/html/body/div[4]/div/main/div[2]/div/div/div/div[1]/div[3]/button",
        )

        # select entry field xpath
        # //*[@id="label-name-"]
        # click_element_by_xpath(website_controller, '//*[@id="label-name-"]')
        website_controller.driver.implicitly_wait(6)
        label_input = website_controller.driver.find_element_by_id("label-name-")

        label_input.send_keys(label)
        website_controller.driver.implicitly_wait(6)

        # and submit label text
        # id="label-name-

        # click create label xpath
        #
        website_controller = click_element_by_xpath(
            website_controller,
            "/html/body/div[4]/div/main/div[2]/div/div/div/form/div[2]/div/button[2]",
        )
        print(f"DONE")


# get milestones
def get_milestones():
    """ """

    def get_milestone_names():
        """ """
        pass

    def get_milestone_descriptions():
        """ """
        pass

    def get_milestone_open_issues():
        """ """
        pass

    def get_milestone_closed_issues():
        """ """
        pass


# get issues
def set_issues(
    issues,
    source_reponame,
    source_username,
    target_reponame,
    target_username,
    website_controller,
):
    """

    :param issues: [List] of Issue objects containing the data (e.g. title, comments) of an issue.
    :param source_reponame: The repository name of the issues you want to copy. The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param target_reponame: The repository name to which you want to copy the issues.
    :param target_username: The GitHub username that contains the repo to which you want to copy the issues.
    :param website_controller: Object controlling the browser.

    """
    adding_issues = get_list_of_new_issues_to_add(
        issues, target_reponame, target_username, website_controller
    )

    # Only keep open issues
    adding_issues = filter_open_issues(issues)

    # goto issue page
    print(f"len issues={len(adding_issues)}")
    for issue in adding_issues:
        print(f"ADDING TITLE:{issue.title}")
        # Go to: https://github.com/a-t-0/testrepo/labels
        website_controller.driver = open_url(
            website_controller.driver,
            f"https://github.com/{target_username}/{target_reponame}/issues",
        )
        website_controller.driver.implicitly_wait(6)

        set_comments(issue, website_controller)
        add_label_to_issue(issue, website_controller)


def filter_open_issues(issues):
    """

    :param issues: [List] of Issue objects containing the data (e.g. title, comments) of an issue.

    """
    open_issues = []
    print(f"len(issues)={len(issues)}")
    for issue in issues:
        if issue.status == "open":
            open_issues.append(issue)
        else:
            print(f"issue.status={issue.status}")
    print(f"len(open_issues)={len(open_issues)}")
    return open_issues


def add_label_to_issue(issue, website_controller):
    """

    :param issue: Objects containing the data (e.g. title, comments) of an issue.
    :param website_controller: Object controlling the browser.

    """

    # and submit label text
    # id="label-name-
    print(f"len={len(issue.labels)}")
    for label in issue.labels:
        # click xpath for new label:
        # website_controller = click_element_by_xpath(
        #    website_controller,
        #    "/html/body/div[4]/div/main/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/details/summary"
        # )

        website_controller.driver.refresh()
        # label-filter-field
        # click add label
        # website_controller.driver.find_element_by_css_selector(".#labels-select-menu > summary:nth-child(1)").click()
        website_controller.driver.find_element_by_css_selector(
            "#labels-select-menu > summary:nth-child(1)"
        ).click()
        website_controller.driver.implicitly_wait(6)

        label_input = website_controller.driver.find_element_by_id("label-filter-field")
        label_input.send_keys(label)
        print(f"SUBMITTING LABEL:{label}")
        time.sleep(5)
        # import org.openqa.selenium.Keys

        label_input.send_keys(Keys.RETURN)
        print(f"adding label:{label}")
        website_controller.driver.implicitly_wait(4)

        label_input.send_keys(Keys.ESCAPE)
        print(f"adding label:{label}")
        website_controller.driver.implicitly_wait(5)
        time.sleep(2)
    time.sleep(4)


def set_comments(issue, website_controller):
    """

    :param issue: Objects containing the data (e.g. title, comments) of an issue.
    :param website_controller: Object controlling the browser.

    """
    # click xpath for new issue:
    website_controller = click_element_by_xpath(
        website_controller,
        # "/html/body/div[4]/div/main/div[2]/div/div/div[1]/div[2]/a/span[1]",
        "/html/body/div[4]/div/main/div[2]/div/div/div[1]/div[2]/a",
    )
    website_controller.driver.implicitly_wait(6)

    # select entry field xpath
    label_input = website_controller.driver.find_element_by_id("issue_title")
    label_input.send_keys(issue.title)
    website_controller.driver.implicitly_wait(6)

    # and submit label text
    # id="label-name-
    print(f"len={len(issue.comments)}")
    time.sleep(4)
    # for comment in issue.comments:
    for i in range(0, len(issue.comments)):
        comment = issue.comments[i]
        if not comment.content is None:
            if i == 0:
                comment_input = website_controller.driver.find_element_by_id(
                    "issue_body"
                )
                comment_input.send_keys(comment.content)
                print(f"adding comment:{comment.content}")
                website_controller.driver.implicitly_wait(6)

                # click create issue xpath
                time.sleep(4)
                website_controller = click_element_by_xpath(
                    website_controller,
                    "/html/body/div[4]/div/main/div[2]/div/div/form/div/div/div[1]/div/div[1]/div/div[2]/button",
                )
                time.sleep(6)
            else:
                # add comment for beyond description
                comment_input = website_controller.driver.find_element_by_id(
                    "new_comment_field"
                )
                comment_input.send_keys(comment.content)
                print(f"adding comment:{comment.content}")
                website_controller.driver.implicitly_wait(6)
                # click create issue xpath
                time.sleep(4)
                website_controller = click_element_by_xpath(
                    website_controller,
                    "/html/body/div[4]/div/main/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/form/div/div/div/div[2]/button",
                )
                time.sleep(6)


def get_list_of_new_issues_to_add(
    issues, target_reponame, target_username, website_controller
):
    """

    :param issues: [List] of Issue objects containing the data (e.g. title, comments) of an issue.
    :param target_reponame: The repository name to which you want to copy the issues.
    :param target_username: The GitHub username that contains the repo to which you want to copy the issues.
    :param website_controller: Object controlling the browser.

    """
    # get the list of issues in the target repo
    existing_issues = get_issues(target_reponame, target_username, website_controller)

    existing_issue_titles = list(map(lambda x: x.title, existing_issues))
    print(f"existing_issue_titles={existing_issue_titles}")
    adding_issues = []

    # see if some issues already exist:
    for source_issue in issues:
        print(f"source_issue.title={source_issue.title}")
        if source_issue.title not in existing_issue_titles:
            adding_issues.append(source_issue)

    for add in adding_issues:
        print(f"add={add.title}")
    return adding_issues
