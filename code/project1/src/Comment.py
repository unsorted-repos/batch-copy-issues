class Comments:
    """Represents the comments of/in a GitHub issue."""

    # https://github.com/HiveMinds-EU/Taskwarrior-installation-original/issues/92
    def __init__(self, comments):
        """
        Constructs an object that represents all the comments in an issue.
        """
        self.comments = comments


class Comment:
    """Represents a single comment of/in a GitHub issue."""

    # https://github.com/HiveMinds-EU/Taskwarrior-installation-original/issues/92
    def __init__(self, author, content):
        """
        Constructs an object that represents an issue.
        """
        self.author = author
        self.content = content
