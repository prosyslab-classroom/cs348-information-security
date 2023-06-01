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

# 2023 수정사항:
# 1. github issue 에 그림을 올리면, 2022년처럼 *.png 로 링크가 나오지 않고, aws 에 있는 곳으로 전달됨.
# 2. 위 이유 때문에 확장자가 없어져서, 그림에 이슈 링크를 달아놓아도 그림만 나오고 이슈로 가지 않음. 따라서 제목을 누르면 이슈로 가도록 수정했음.
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
        # markdown
        image_url = re.search(r"\(https://github.com/.+\)", issue.body)
        if image_url == None:
            # html
            image_url = re.search(r"\"https://github.com/.+\"", issue.body)
        image_url = image_url.group(0)[1:-1]
        user = issue.user.login
        user_url = f"https://github.com/{user}"
        (gold, silver, bronze) = (False, False, False)
        for label in issue.labels:
            if label.name == "gold":
                gold = True
            elif label.name == "silver":
                silver = True
            elif label.name == "bronze":
                bronze = True
        medal = ":1st_place_medal:" if gold else ":2nd_place_medal:" if silver else ":3rd_place_medal:" if bronze else ""
        line += f"[![{title}]({image_url})]({issue_url})[{title}]({issue_url}) {medal}<br>by [{user}]({user_url})|"
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
