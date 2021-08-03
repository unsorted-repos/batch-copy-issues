from .control_website import open_url
from .Issue import Issue
from .Milestone import Milestone
from .Comment import Comment
from .helper import source_contains


def get_labels():
    """Gets the labels directly from the source repository.
    (Currently only the used labels are accumulated per issue.)
    """

    def get_label_names():
        """ """
        pass

    def get_label_descriptions():
        """ """
        pass

    def get_label_colour():
        """ """
        pass


# get milestones
def get_milestones():
    """Gets the milestones directly from the source repository.
    (Currently the milestones are not copied.)
    """

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
def get_issues(source_reponame, source_username, website_controller):
    """

    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    # get nr of issues
    nr_of_issues = get_nr_of_issues(
        source_reponame, source_username, website_controller
    )

    issues = []

    # loop through issues
    for i in range(1, nr_of_issues):
    #for i in range(1, 3):
        issue = Issue()
        issue.set_title(
            get_issue_title(i, source_reponame, source_username, website_controller)
        )
        issue.set_comments(
            get_issue_comments(i, source_reponame, source_username, website_controller)
        )
        issue.set_assignees(
            get_issue_assignees(i, source_reponame, source_username, website_controller)
        )
        issue.set_labels(
            get_issue_labels(i, source_reponame, source_username, website_controller)
        )
        issue.set_projects(
            get_issue_projects(i, source_reponame, source_username, website_controller)
        )
        issue.set_milestones(
            get_issue_milestones(
                i, source_reponame, source_username, website_controller
            )
        )
        issue.set_status(
            get_issue_status(i, source_reponame, source_username, website_controller)
        )
        issues.append(issue)
    return issues


def get_nr_of_issues(source_reponame, source_username, website_controller):
    """

    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    # get max issue nr
    website_controller.driver = open_url(
        website_controller.driver,
        f"https://github.com/{source_username}/{source_reponame}/issues?page={1}&q=is%3Aissue+is%3Aopen",
    )
    # source
    source = website_controller.driver.page_source
    # extract indicator string of first issue
    nr_of_issues = get_nr_from_html_source(source, 'aria-labelledby="issue_', "_")
    return nr_of_issues


def loop_through_issue_pages(source_reponame, source_username, website_controller):
    """

    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    # loop through pages
    for i in range(1, nr_of_issue_pages):
    #for i in range(1, 3):
        # visit issue page
        # visit issue page
        website_controller.driver = open_url(
            website_controller.driver,
            f"https://github.com/{source_username}/{source_reponame}/issues?page={i}&q=is%3Aissue+is%3Aopen",
        )


def get_nr_of_issue_pages():
    """ """
    if not source_contains(website_controller, "data-total-pages="):
        return 1
    else:
        nr_of_issue_pages = get_nr_from_html_source(
            website_controller.driver.page_source, 'data-total-pages="', '"'
        )
        return nr_of_issue_pages


def get_value_from_html_source(source, substring, closing_substring):
    """

    :param source: Source code of website that is being controlled.
    :param substring::param substring: A substring that is sought.
    :param closing_substring: A substring that indicates the end of text that is searched.

    """
    nr_of_pages_index = source.find(substring) + len(substring)
    # print(f'nr_of_pages_index={nr_of_pages_index}')
    closing_quotation = source.find(closing_substring, nr_of_pages_index)
    # print(f'closing_quotation={closing_quotation}')
    # print(f'nr={source[nr_of_pages_index:closing_quotation]}')
    value = source[nr_of_pages_index:closing_quotation]
    return value


def get_nr_from_html_source(source, substring, closing_substring):
    """

    :param source: Source code of website that is being controlled.
    :param substring::param substring: A substring that is sought.
    :param closing_substring: A substring that indicates the end of text that is searched.

    """
    try:
        nr_of_issue_pages = int(
            get_value_from_html_source(source, substring, closing_substring)
        )
    except:
        nr_of_issue_pages = 0
    return nr_of_issue_pages


def get_issue_nr():
    """ """
    pass


def get_issue_title(issue_nr, source_reponame, source_username, website_controller):
    """

    :param issue_nr: The number of the issue in the GitHub repository.
    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    # https://github.com/HiveMinds-EU/Taskwarrior-installation-original/issues/126
    website_controller.driver = open_url(
        website_controller.driver,
        f"https://github.com/{source_username}/{source_reponame}/issues/{issue_nr}",
    )

    # Get the issue title
    # <title>Clean up the installation code.  · Issue #121 · HiveMinds-EU/Taskwarrior-installation-original</title>
    title = get_value_from_html_source(
        website_controller.driver.page_source, "<title>", " · Issue #"
    )
    title_slash = get_value_from_html_source(
        website_controller.driver.page_source, "<title>", "</title>"
    )
    if len(title_slash) < len(title):
        title = title_slash

    print(f"title={title}")
    return title


def get_issue_status(issue_nr, source_reponame, source_username, website_controller):
    """

    :param issue_nr: The number of the issue in the GitHub repository.
    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    website_controller.driver = open_url(
        website_controller.driver,
        f"https://github.com/{source_username}/{source_reponame}/issues/{issue_nr}",
    )
    remainder = website_controller.driver.page_source
    substring = 'class="State State--'
    status = get_value_from_html_source(remainder, substring, '"')
    return status


def get_issue_comments(issue_nr, source_reponame, source_username, website_controller):
    """

    :param issue_nr: The number of the issue in the GitHub repository.
    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    comments = []
    website_controller.driver = open_url(
        website_controller.driver,
        f"https://github.com/{source_username}/{source_reponame}/issues/{issue_nr}",
    )
    remainder = website_controller.driver.page_source
    substring = '<td class="d-block comment-body markdown-body  js-comment-body">'
    while substring in remainder:

        comment_html_td = get_value_from_html_source(remainder, substring, "</td>")
        comment_html_button = get_value_from_html_source(
            remainder, substring, "<button"
        )
        if len(comment_html_td) < len(comment_html_button):
            comment_html = comment_html_td
        else:
            comment_html = comment_html_button
        index = remainder.index(substring)
        # print(f'comment_html={comment_html}\n\n')
        remainder = remainder[index + len(substring) :]

        if "<em>No description provided.</em>" in comment_html:
            comment_html = None

        comment = Comment(None, comment_html)
        comments.append(comment)
    return comments


def get_issue_assignees(issue_nr, source_reponame, source_username, website_controller):
    """

    :param issue_nr: The number of the issue in the GitHub repository.
    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    pass


def get_issue_labels(issue_nr, source_reponame, source_username, website_controller):
    """

    :param issue_nr: The number of the issue in the GitHub repository.
    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    # "/HiveMinds-EU/Taskwarrior-installation-original/labels/Quality"
    labels = []
    website_controller.driver = open_url(
        website_controller.driver,
        f"https://github.com/{source_username}/{source_reponame}/issues/{issue_nr}",
    )
    remainder = website_controller.driver.page_source
    substring = f"/{source_username}/{source_reponame}/labels/"
    while substring in remainder:
        # label = get_value_from_html_source(remainder, substring, '" title=')
        label = get_value_from_html_source(remainder, substring, '"')
        print(f"label={label}")
        labels.append(label.replace("%20", " "))

        # remove parsed segments from remaining source
        index = remainder.index(substring)
        # print(f'comment_html={comment_html}\n\n')
        remainder = remainder[index + len(substring) :]
    return list(set(labels))


def get_issue_projects(issue_nr, source_reponame, source_username, website_controller):
    """

    :param issue_nr: The number of the issue in the GitHub repository.
    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    pass


def get_issue_milestones(
    issue_nr, source_reponame, source_username, website_controller
):
    """

    :param issue_nr: The number of the issue in the GitHub repository.
    :param source_reponame: The repository name of the issues you want to copy.
    :param source_username: The GitHub username that contains the repo containing the issues you want to copy.
    :param website_controller: Object controlling the browser.

    """
    pass