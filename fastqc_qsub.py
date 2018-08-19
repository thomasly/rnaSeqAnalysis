import os, sys

comm_list = ["qsub", 
"-pe openmpi 4-8", 
"-t 1-5"]

comm_list.append(sys.argv[1])

command = " ".join(comm_list)
os.system(command)
