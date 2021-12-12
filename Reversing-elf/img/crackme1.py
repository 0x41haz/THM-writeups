#!/usr/bin/pyhton3
import os, sys, stat
cmd='sudo ./crackme1 --option --otheroption' #give your file location
os.chmod("crackme1", 777) #give file name with location
os.system(cmd)