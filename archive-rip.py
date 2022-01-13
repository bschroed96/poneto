import os
import sys
import re

if len(sys.argv <= 1):
    print("Usage: archive-rip.py /directory/of/website/ myfake@email.com(optional)")
    exit

directory = sys.argv[1]
email = '@us.gmail.com'
if len(sys.argv) == 3:
    email = sys.argv[2]
for f in os.listdir(directory):
    f = directory + f
    # Read in the file
    with open(f, 'r') as file :
        filedata = file.read()

    # Replace the target strings
        # remove singlefile
        filedata = re.sub(r'<!--(?s).*?-->', '', filedata)

        # remove wayback reference
        filedata = re.sub(r'<div id=wm-ipp-print class=sf-hidden>The Wayback(?s).*?<\/div>','',filedata)

        # # Update with relative links
        filedata = re.sub(r'href=https:\/\/web.archive.org\/web\/(?s).*?.com\/','href=./',filedata)

        # # Incase of ./ empty relative links, replace with ./index.html
        filedata = re.sub(r'href=.\/ ', 'href=./index.html ', filedata)

        # # Remove plain web archive links
        filedata = re.sub(r'https:\/\/web.archive.org\/web\/.+?\/', '', filedata)

        # # remove email addresses and replace with specified email address. Default is @us.gmail.com
        filedata = re.sub(r'@.+?.com', email, filedata)

        # find more references to web archive
        arch_refs = len(re.findall(r"wayback", filedata))
        if arch_refs > 0:
            print("===================================")
            print(f'There are still web.archive references in {f} : {arch_refs}')
            print("===================================")

        # check for wayback refs
        wayback_refs = len(re.findall(r"wayback", filedata))
        if arch_refs > 0:
            print("===================================")
            print(f'There are still wayback references in {f} : {wayback_refs}')
            print("===================================")

    # Write the file out again
    with open(f, 'w') as file:
        file.write(filedata)