#!/usr/bin/env python3

import getpass
import requests
import re

cols = 5


def print_line():
    line = "|"
    for i in range(cols):
        line += ":-:|"
    return line

# 2025 수정사항
# 1. GitHub Discussions API (GitHub GraphQL API)를 사용하여 Art competition 작품을 가져오도록 수정
def get_art_competition_discussions(token, year):
    headers = {"Authorization": f"Bearer {token}"}
    query = """
    {
      repository(owner: "prosyslab-classroom", name: "cs348-information-security") {
        discussions(first: 100) {
          nodes {
            title
            url
            body
            publishedAt
            author {
              login
              url
            }
            category {
              name
            }
            labels(first: 10) {
              nodes {
                name
              }
            }
          }
        }
      }
    }
    """
    response = requests.post(
        "https://api.github.com/graphql", json={"query": query}, headers=headers
    )
    response.raise_for_status()
    data = response.json()
    all_discussions = data["data"]["repository"]["discussions"]["nodes"]
    return [
        d for d in all_discussions
        if d["category"]["name"] == "Art competition" 
        and d["publishedAt"].startswith(year)
    ]


def main():
    username = input("Username: ")
    password = getpass.getpass("Token or Password: ")
    discussions = get_art_competition_discussions(password, "2025")
    # 특정 년도 작품만 가져오도록 수정
    index = 0
    line = "|"
    line_printed = False

    for d in discussions:
      title = d["title"]
      discussion_url = d["url"]
      body = d["body"]
      user = d["author"]["login"]
      user_url = d["author"]["url"]
      labels = [label["name"].lower() for label in d.get("labels", {}).get("nodes", [])]
      medal = ""
      if "gold" in labels:
          medal = ":1st_place_medal:"
      elif "silver" in labels:
          medal = ":2nd_place_medal:"
      elif "bronze" in labels:
          medal = ":3rd_place_medal:"

      image_url_match = re.search(r"\(https://github.com/.+\)", body)
      if image_url_match is None:
          image_url_match = re.search(r"\"https://github.com/.+\"", body)

      if image_url_match:
          image_url = image_url_match.group(0)[1:-1]
          content = f"[![{title}]({image_url})]({discussion_url})[{title}]({discussion_url}) {medal}<br>by [{user}]({user_url})"
      else: # 시와 같이 이미지가 없는 경우, 이미지 없이 표시
          content = f"[{title}]({discussion_url}) {medal}<br>by [{user}]({user_url})"

      line += content + "|"
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
