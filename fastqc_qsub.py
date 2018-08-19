import os, sys

comm_list = ["qsub", 
"-pe openmid 4-8", 
"-t 1-4"]

comm_list.append(sys.argv[1])

command = " ".join(comm_list)
os.system(command)
