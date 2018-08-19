import os, sys

comm_list = ["qsub",
"-t 1-5"]

comm_list.append(sys.argv[1])

command = " ".join(comm_list)
os.system(command)
