import os
import subprocess


files = os.listdir("Source")

os.mkdir("Result")

for f in files:
    cmdstr ="convert " + " source\\" + f + " -resize 200 " + "result\\" + f
    subprocess.run(cmdstr)


