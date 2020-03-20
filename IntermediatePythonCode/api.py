#!/usr/bin/env python3
import json
import requests

demo_commit_url = "https://api.github.com/repos/Parchive/par2cmdline/commits"
r = requests.get(demo_commit_url)  ##gets all info
commit_dict = json.loads(r.content)  # organisse data in dictionary
filename = []
authors = []
commitid = []
#for commit_detail in commit_dict:  # each section in dict
    #print(commit_detail)
    #if commit_detail == "files":  # section to search for file name
        #print(commit_dict[commit_detail])
        #if len(commit_dict[commit_detail]) > 0:
            #for i in range(len("files")):
                #if "filename" in commit_dict[commit_detail][i]:
                    #print(commit_dict[commit_detail][i]["filename"])  # print file name
for i in range(len(commit_dict)):
    # Checking for new authors and adding new ones in authors list
    if not commit_dict[i]["commit"]["author"]["name"] in authors:
        authors.append(commit_dict[i]["commit"]["author"]["name"])
        commitid.append(commit_dict[i].get("sha"))
for i in range(len(authors)):
    url = "https://api.github.com/repos/Parchive/par2cmdline/commits/" + commitid[i]
    info = requests.get(url)
    commitinfo = json.loads(info.content)
    print(authors[i])
    for commit in commitinfo:
        if commit == "files":
            if len(commitinfo[commit]) > 0:
                for j in range(len("files")):
                    if "filename" in commitinfo[commit][j]:
                        print(commitinfo[commit][j]["filename"])



