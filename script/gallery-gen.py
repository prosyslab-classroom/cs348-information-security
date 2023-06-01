#!/usr/bin/env python3

import getpass
import re

from github import Github

cols = 5


def print_line():
    line = "|"
    for i in range(cols):
        line += ":-:|"
    return line


def main():
    username = input("Username: ")
    password = getpass.getpass()
    g = Github(username, password)
    org = g.get_organization("prosyslab-classroom")
    repo = org.get_repo("cs348-information-security")
    issues = repo.get_issues(labels=["art competition"])
    index = 0
    line = "|"
    line_printed = False
    for issue in issues:
        title = issue.title.split("] ")[1]
        issue_url = issue.url.replace("api.", "").replace("/repos/", "/")
        print(issue.body)
        # markdown
        image_url = re.search(r"\(https://github.com/.+\)", issue.body)
        if image_url == None:
            # html
            image_url = re.search(r"\"https://github.com/.+\"", issue.body)
        image_url = image_url.group(0)[1:-1]
        user = issue.user.login
        user_url = issue.user.url
        (gold, silver, bronze) = (False, False, False)
        for label in issue.labels:
            if label.name == "gold":
                gold = True
            elif label.name == "silver":
                silver = True
            elif label.name == "bronze":
                bronze = True
        medal = ":1st_place_medal:" if gold else ":2nd_place_medal:" if silver else ":3rd_place_medal:" if bronze else ""
        line += f"[![{title}]({image_url})]({issue_url}){title} {medal}<br>by [{user}]({user_url})|"
        index += 1
        if index % cols == 0:
            if not line_printed:
                line += "\n"
                line_printed = True
                line += print_line()
            line += "\n|"
    print(line)


if __name__ == "__main__":
    main()
