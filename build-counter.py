import re
import sys
import os

if len(sys.argv) < 4:
    print ("Not enough arguments.")
    print ("ex: " + sys.argv[0] + " file_path major|minor|patch commit_hash")
    sys.exit(1)

if os.path.isfile(sys.argv[1]) == False:
    print ("File (" + sys.argv[1] + ") not found.")
    sys.exit(1)

f = open(sys.argv[1], "r")
content = f.readlines()

re_patch = r"\s*patch: ([0-9]+)"
re_minor = r"\s*minor: ([0-9]+)"
re_major = r"\s*major: ([0-9]+)"
re_hash = r"(\s*commit_hash: )[a-z0-9]{0,40}"

modifiers = ["*1","*1","*1"]

arg = sys.argv[2].lower()
if arg == "major":
    modifiers = ["+1","*0","*0"]
elif arg == "minor":
    modifiers = ["*1","+1","*0"]
elif arg == "patch":
    modifiers = ["*1","*1","+1"]
else:
    print ("Argument is not valid.")
    print ("ex: " + sys.argv[0] + " major|minor|patch commit_hash")
    sys.exit(1)

commit_hash = sys.argv[3]
if re.match(r"[a-z0-9]{7,40}", commit_hash) is None:
    print ("Commit hash is not valid.")
    print ("7 to 40 characters expected.")
    sys.exit(1)
    
for i in range(0,len(content)):
    l = content[i]
    m_patch = re.match(re_patch, l)
    m_minor = re.match(re_minor, l)
    m_major = re.match(re_major, l)
    m_hash = re.match(re_hash, l)
    if m_patch is not None:
        exec("new_val=" + m_patch.group(1) + modifiers[2])
        content[i] = l.replace(m_patch.group(1), str(new_val))
    if m_minor is not None:
        exec("new_val=" + m_minor.group(1) + modifiers[1])
        content[i] = l.replace(m_minor.group(1), str(new_val))
    if m_major is not None:
        exec("new_val=" + m_major.group(1) + modifiers[0])
        content[i] = l.replace(m_major.group(1), str(new_val))
    if m_hash is not None:
        content[i] = m_hash.group(1) + commit_hash
        

f = open(sys.argv[1], "w")
f.writelines(content)
f.close()
