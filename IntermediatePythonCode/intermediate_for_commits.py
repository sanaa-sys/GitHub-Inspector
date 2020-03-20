import json
import requests
demo_commit_url = "https://api.github.com/repos/Parchive/par2cmdline/commits"

r = requests.get(demo_commit_url)
commit_data = json.loads(r.content)
print(r.content)
author_Data = {}
authors=[]
bail = 5
for item in commit_data:
    #print(item["commit"]["author"]["name"])
    #print(item["url"])
    if bail > 0:
        bail -= 1
    else:
        break
    sub_request = requests.get(item["url"])
    specific_data = json.loads(sub_request.content)
    additions = specific_data["stats"]["additions"]
    deletions = specific_data["stats"]["deletions"]
    print("Author: {0}, lines added: {1}, lines deleted: {2}".format(item["commit"]["author"]["name"], additions, deletions))

    if item["commit"]["author"]["name"] in author_Data:
        author_Data[item["commit"]["author"]["name"]] += 1
    else:
        author_Data[item["commit"]["author"]["name"]] = 1
    #Adding all authors names in list

for i in range(len(commit_data)):
        # Checking for new authors and adding new ones in authors list
    if not commit_data[i]["commit"]["author"]["name"] in authors:
        authors.append(commit_data[i]["commit"]["author"]["name"])

    # Adding key and value pairs into dict, (Author and date of their commits)
for i in range(len(commit_data)):
    for j in range(len(authors)):
            #If author exists in authors list, then add the time/date value to dictionary as list
        if commit_data[i]["commit"]["author"]["name"] == authors[j]:
            adds = specific_data["stats"]["additions"]
            print(author_Data)




#
#
# for key in commit_dict:
# 	print("Key is {0}, data is {1}".format(key, commit_dict[key]))
# 	if key == "stats":
# 		print(commit_data[key])
# 		additions = commit_data[key]["additions"]
# 		deletions = commit_data[key]["deletions"]
# 		print("Lines added: {0}, lines deleted: {1}".format(additions, deletions))
#
# if "stats" in commit_dict:
#     print(commit_data["stats"])
