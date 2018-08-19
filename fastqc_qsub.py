import os, sys

for t in range(5):
    command = "qsub " + sys.argv[1].strip() + " " + str(t)
    
# comm_list = ["qsub", "-t 1-5"]

# comm_list.append(sys.argv[1].strip())

# command = " ".join(comm_list)
    os.system(command)
