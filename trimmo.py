import os, sys
from glob import glob
from multiprocessing import cpu_count

trimmomaticpath = "/ifs/home/xs338/Trimmomatic-0.36"

infq1 = sys.argv[1]
infq2 = sys.argv[2]
adapterfa = sys.argv[3]
outfq1 = infq1 + ".cleaned.fastq"
outfq2 = infq2 + ".cleaned.fastq"
outrmfq1 = infq1 + ".removed.fastq"
outrmfq2 = infq2 + ".removed.fastq"
logfile = infq1 + ".log"
n_threads = cpu_count()
print("infq1: {}".format(infq1))
print("infq2: {}". format(infq2))
print("adapterfa: {}".format(adapterfa))

command = "java -jar {0}/trimmomatic-0.36.jar PE -threads {1} -phread33 -trimlog \
{2} {3} {4} {5} {6} {7} {8} ILLUMINACLIP:{9}:3:30:7:1:TRUE LEADING:2 TRAILING:2 \
SLIDINGWINDOW:4:10 MINLEN:36".format(trimmomaticpath, n_threads, logfile, infq1, infq2, 
outfq1, outrmfq1, outfq2, outrmfq2, adapterfa)

os.system(command)
