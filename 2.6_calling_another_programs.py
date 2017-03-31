import os
import subprocess


files = os.listdir("Source")

try:
    os.mkdir("Result")
except FileExistsError: pass

for f in files:
    cmdstr = "convert " + os.path.join(" source", f) + " -resize 200 " + os.path.join("result", f)
    subprocess.run(cmdstr)

