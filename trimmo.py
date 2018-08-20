import os, sys
from glob import glob
from multiprocessing import cpu_count
from paths import RnaSeqPath

def find_inputs(path):
    """
    find the inputs pair for trimmomatic

    arguments:
    path - folder contains input .fastqc files

    return:
    array contains all inputs paired in tuples
    """

    paths = RnaSeqPath()

    # all fastq files
    files = glob(os.path.join(paths.fastq, "*.fastq.gz"))

    paired_files = []
    # find paired files
    while files:
        # save the path
        f1 = files[0]
        # get file name
        f1_base = os.path.basename(f1)
        # the indentical part in the file names of the paired files
        pair_id = f1_base.split(".")[0][:-7]
        # remove f1 to avoid duplicate
        files.pop(0)
        for idx, f2 in enumerate(files):
            if pair_id in f2:
                paired_files.append(tuple((f1, f2)))
                files.pop(idx)
                break

    return paired_files


def trim_extention(path):
    """
    remove the extension from file name, keep path
    """
    return os.path.join(os.path.dirname(path), 
                    os.path.basename(path).split(".")[0])


def main(path=None):
    """
    Run trimmomatic
    """
    paths = RnaSeqPath()
    trimmomaticpath = paths.trimmomatic
    if path:
        paired_files_arr = find_inputs(path)
    else:
        paired_files_arr = find_inputs(paths.fastq)
    
    adapterfa = sys.argv[1]
    n_threads = cpu_count()
    idx = int(sys.argv[2]) - 1
    file_pair = paired_files_arr[idx]
    infq1 = file_pair[0]
    infq2 = file_pair[1]
    outfq1 = trim_extention(infq1) + ".cleaned.fastq"
    outfq2 = trim_extention(infq2) + ".cleaned.fastq"
    outrmfq1 = trim_extention(infq1) + ".removed.fastq"
    outrmfq2 = trim_extention(infq2) + ".removed.fastq"
    logfile = trim_extention(infq1) + ".log"
    print("infq1: {}".format(infq1))
    print("infq2: {}".format(infq2))
    print("adapterfa: {}".format(adapterfa))

    command = "java -jar {0} PE -threads {1} -phred33 -trimlog \
    {2} {3} {4} {5} {6} {7} {8} ILLUMINACLIP:{9}:3:30:7:1:TRUE LEADING:2 \
    TRAILING:2 SLIDINGWINDOW:4:10 MINLEN:36".format(trimmomaticpath, 
    n_threads, logfile, infq1, infq2, outfq1, outrmfq1, outfq2, outrmfq2, 
    adapterfa)

    os.system(command)


if __name__ == "__main__":
    main()
