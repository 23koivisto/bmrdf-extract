#!/usr/bin/python
import requests
import os
import sys

values = []
resource = []
res = 0
ids = sys.argv[1]

##change file name to a specific file for future usage##
##Files incoming should be lists of URIS from British Museum. Text file, one URI per line##
##the -1 in the append is to remove /n at the end of liens I haven't been able to shake##

f = open(ids,'r')
for line in f:
    if line[46].isdigit():
        values.append(line[:-1])
    else:
        continue
f.close()

for i in values:
    resource.append(i[46:])
    for i in resource:
        var = i
        res = "http://collection.britishmuseum.org/resource?uri=http%3A%2F%2Fcollection.britishmuseum.org%2Fid%2Fobject%2F" + i + "&format=rdf"
        f = open('bmrdf/temp','w')
        r = requests.get(res)
        rt = r.text
        f.write(rt.encode('utf8'))
        f.close()
       ## print var
        os.rename("bmrdf/temp", "bmrdf/" + var)
