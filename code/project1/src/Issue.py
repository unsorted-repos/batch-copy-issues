from .Milestone import Milestone
from .Comment import Comment


class Issue:
    """Object representing a GitHub issue."""

    def __init__(
        self,
        title=None,
        status=None,
        comments=None,
        assignees=None,
        labels=None,
        projects=None,
        milestones=None,
    ):
        """
        Constructs an object that represents an issue.
        """
        self.title = title
        self.status = status
        self.comments = comments
        self.assignees = assignees
        self.labels = labels
        self.projects = projects
        self.milestones = milestones

    def set_title(self, title):
        """

        :param title:

        """
        self.title = title

    def set_status(self, status):
        """

        :param status:

        """
        self.status = status

    def set_comments(self, comments):
        """

        :param comments:

        """
        self.comments = comments

    def set_assignees(self, assignees):
        """

        :param assignees:

        """
        self.assignees = assignees

    def set_labels(self, labels):
        """

        :param labels: :param labels: [List] of label objects representing the content and colour of a label.

        """
        self.labels = labels

    def set_projects(self, projects):
        """

        :param projects:

        """
        self.projects = projects

    def set_milestones(self, milestones):
        """

        :param milestones:

        """
        self.milestones = milestones
