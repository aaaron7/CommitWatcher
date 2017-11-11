# -*- coding: utf-8 -*-
import sys
import json
import commands
import os
from os import listdir
from os.path import isfile, join
from os.path import expanduser

def main(argc, argv):
    """check all folder's"""
    try:
        fo =  open(expanduser("~/.cwrc"),"r")
    except IOError as e:
        print e
        return

    lines = fo.readlines()
    for line in lines:
        handle_folder(line)
    fo.close()

def handle_folder(path):
    """handle single folders"""
    os.chdir(expanduser(path))
    current_branch = commands.getoutput("git branch").split(' ')[1].strip()
    content = commands.getoutput("git status")
    if content.find("nothing to commit") >= 0:
        return
    else:
        result = commands.getoutput("git commit -am \"automatically commit\"")
        commands.getoutput("git push origin %s" % current_branch)
        print "automatically commmit for %s" % (path)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
