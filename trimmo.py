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
n_slots = cpu_count()
print("infq1: ".format(infq1))
print("infq2: ". format(infq2))
print("adapterfa: ".format(adapterfa))

command = "java -jar {}/trimmomatic-0.36.jar PE -threads {} -phread33 -trimlog {} {} {} {} {} {} {} ILLUMINACLIP:{}:3:30:7:1:TRUE LEADING:2 TRAILING:2 SLIDINGWINDOW:4:10 MINLEN:36".format(params)

java -jar ${trimmomaticpath}/trimmomatic-0.36.jar PE -threads $NSLOTS -phred33 -trimlog $logfile $infq1 $infq2 $outfq1 $out\
rmfq1 $outfq2 $outrmfq2 ILLUMINACLIP:${adapterfa}:3:30:7:1:TRUE LEADING:2 TRAILING:2 SLIDINGWINDOW:4:10 MINLEN:36

command = java -jar trimmomatic-0.33.jar PE -phred33 input_forward.fq.gz input_reverse.fq.gz output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

os.system(command)
