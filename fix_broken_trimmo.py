import os, sys
from glob import glob
from multiprocessing import cpu_count
from paths import RnaSeqPath
import pickle as pk


def make_output_name(path):
    """
    remove the extension from file name
    """

    paths = RnaSeqPath()
    output_dir = paths.trimmomatic_outputs
    return os.path.join(output_dir, os.path.basename(path).split(".")[0])


def main(path=None):
    """
    Run trimmomatic
    """
    paths = RnaSeqPath()
    trimmomaticpath = paths.trimmomatic

    adapterfa = sys.argv[1]
    n_threads = cpu_count()
    infq1 = os.path.join(paths.fastq, "LD207-12_2_S40_L005_R1_001.fastq.gz")
    infq2 = os.path.join(paths.fastq, "LD207-12_2_S40_L005_R2_001.fastq.gz")
    outfq1 = make_output_name(infq1) + ".cleaned.fastq"
    outfq2 = make_output_name(infq2) + ".cleaned.fastq"
    outrmfq1 = make_output_name(infq1) + ".removed.fastq"
    outrmfq2 = make_output_name(infq2) + ".removed.fastq"
    logfile = make_output_name(infq1) + ".log"
    print("infq1: {}".format(infq1))
    print("infq2: {}".format(infq2))
    print("adapterfa: {}".format(adapterfa))
    sys.stdout.flush()

    command = "java -jar {0} PE -threads {1} -phred33 -trimlog \
    {2} {3} {4} {5} {6} {7} {8} ILLUMINACLIP:{9}:3:30:7:1:TRUE LEADING:2 \
    TRAILING:2 SLIDINGWINDOW:4:10 MINLEN:36".format(trimmomaticpath, 
    n_threads, logfile, infq1, infq2, outfq1, outrmfq1, outfq2, outrmfq2, 
    adapterfa)

    os.system(command)


if __name__ == "__main__":
    main()