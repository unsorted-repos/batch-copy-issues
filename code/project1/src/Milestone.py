class Milestones:
    """Represents the Milestones of/in a GitHub issue."""

    # https://github.com/HiveMinds-EU/Taskwarrior-installation-original/issues/92
    def __init__(self, Milestones):
        """
        Constructs an object that represents all the Milestones in an issue.
        """
        self.Milestones = Milestones


class Milestone:
    """Object representing a GitHub milestone.
    https://github.com/HiveMinds-EU/Productivity-phone/milestones


    """

    def __init__(self, title=None, description=None, due_date=None, issues=None):
        """
        Constructs an object that represents an issue.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.issues = issues
