import subprocess

# Just calling 7zip to build Packages.bz2 for us :)
subprocess.call("7z a -tbzip2 Packages.bz2 Packages")
