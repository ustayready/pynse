from setuptools import setup
import sys, os, shutil

# Check to see if we have access
if not os.getuid() == 0:
    sys.exit("pyNSE error: must be ran as root.")

# Set variables
cwd = os.getcwd()
nse = "/usr/share/nmap/scripts/"

# Write local shell script
with open("scripts/pynse","w") as fh:
    fh.write("#!/bin/sh\ncd {}\nchmod +x pynse.py\n./pynse.py \"$@\"".format(cwd))

# Copy nse into nmap directory
# TODO: allow configurable nmap path
shutil.copy("{}/pynse.nse".format(cwd), nse)

# Configuration for setup
setup(
        name = "pyNSE",
        version="0.0.1",
        zip_safe = False,
 
        description = "An nmap python extender.",
        long_description = "Python scriptability tin nmap, simply create a plugin in the ./plugins directory. (Use the Test.py plugin as a template)",
        author = "Mike Felch",
        author_email = "mike@linux.edu",
 
        license = "GPLv2",
        keywords = ("demo", "python", "egg"),
        platforms = "independent",
        url = "https://stayready.github.io/",

        scripts = [
            'scripts/pynse'
        ]
)
