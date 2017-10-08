#!/usr/bin/env python

import subprocess


procs = [
    # grab data from EBI
    ["curl"
        , "ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/json/hgnc_complete_set.json"]

    # extract names
    , ["jq"
        , "'.response.docs[]'"]

    # load into MongoDB
    , ["mongoimport"
        , "-d", "vte"
        , "-c", "hgnc_names"
        , "--drop"]
]

subprocs = []

for i in range(len(procs)):

    if i == 0:
        subprocs.append(
                subprocess.Popen(procs[i]
                    , stdout=subprocess.PIPE))
    else:
        subprocs.append(
                subprocess.Popen(procs[i]
                    , stdin=subprocs[i-1].stdout
                    , stdout=subprocess.PIPE))




p1.stdout.close()
output, exitCode = p2.communicate()

print(output)


