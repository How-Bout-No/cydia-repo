# What are you doing trying to look through these files? ;)
# Haha, just kidding, but if you're wondering why this is here, fear not. I'll tell you.
# Currently, this file is going to help in an experiment that I am running. And since I'm
# a very inefficient young lad, I'm debugging the public product instead of the internal...
# (Cause it's easier and I'm dumb)
# Actually, the only experiment is the xml...
# Trying to get an auto-update for the Hosted Packages, ya feel me?
# Now idk **** about JS, as I'm wayyyy more experienced in Python (which is why this is a py script)
# But... I'll see how this goes.

# If this works, it'll help me push projects out faster :)

# Now scram!

import subprocess
from shutil import copyfile
from xml.dom.minidom import Document

subprocess.call("7z a -tbzip2 Packages.bz2 Packages")


class DictToXML(object):
    default_list_item_name = "item"

    def __init__(self, structure, list_mappings={}):
        self.doc = Document()

        if len(structure) == 1:
            rootName = str(list(structure.keys())[0])
            self.root = self.doc.createElement(rootName)

            self.list_mappings = list_mappings

            self.doc.appendChild(self.root)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])
        elif type(structure) == list:
            tag_name = self.default_list_item_name

            if father.tagName in self.list_mappings:
                tag_name = self.list_mappings[father.tagName]

            for l in structure:
                tag = self.doc.createElement(tag_name)
                self.build(tag, l)
                father.appendChild(tag)
        else:
            data = str(structure)
            tag = self.doc.createTextNode(data)
            father.appendChild(tag)

    def display(self):
        print(self.doc.toprettyxml(indent="  "))

    def get_string(self):
        return self.doc.toprettyxml(indent="  ")


with open('Packages', 'r') as file:
   Packages = file.read()
   file.close()

PackagesSorted = Packages.split('\n\n')
PackageListFinal = []
for x in PackagesSorted:
    PackageList = {}
    data = x.replace(': ', '\n').split('\n')
    for i,k in zip(data[0::2], data[1::2]):
        PackageList[i] = k.replace('https://how-bout-no.github.io/', '')
    PackageListFinal.append(PackageList)
AllPackages = {"package": PackageListFinal}
xml = DictToXML(AllPackages)
with open('Packages.xml', 'w') as file:
    file.write(xml.get_string())
    file.close()
