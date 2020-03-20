#!/usr/bin/env python3
import json
import requests
import datetime

demo_commit_url = "https://api.github.com/repos/githubtraining/hellogitworld/commits"
r = requests.get(demo_commit_url)
commit_dict = json.loads(r.content)
authors = []
commit_details = {}
date = ""

# Adding all authors names in list
for i in range(len(commit_dict)):
    # Checking for new authors and adding new ones in authors list
    if not commit_dict[i]["commit"]["author"]["name"] in authors:
        authors.append(commit_dict[i]["commit"]["author"]["name"])

# Adding key and value pairs into dict, (Author and date of their commits)
for i in range(len(commit_dict)):
    for j in range(len(authors)):
        # If author exists in authors list, then add the time/date value to dictionary as list
        if commit_dict[i]["commit"]["author"]["name"] == authors[j]:
            date = commit_dict[i]["commit"]["author"]["date"]
            date = date.replace('T', ', ')
            date = date.replace('Z', '')
            commit_details.setdefault(authors[j], []).append(date)

# Used for sorting
def key(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d, %H:%M:%S')


# Sorting the dates and times list, from newest to oldest
commit_details = {k: sorted(v, key=key) for k, v in commit_details.items()}

# Printing the author name and the time of each commit made by them
for name in commit_details:
    print("\nAuthor Name:", name, "")
    print("Date and time of commits:")
    for i in range(len(commit_details[name])):
        print(commit_details[name][i])

