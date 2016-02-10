import urllib2
import os
import json
import sys
j_data=urllib2.urlopen("https://api.github.com/users/{}/repos".format(sys.argv[1]))
data=json.load(j_data)
for node in data:
    c_u=node["clone_url"]
    print c_u
    if not os.path.exists(node["name"]):
        os.system("git clone {}".format(c_u))