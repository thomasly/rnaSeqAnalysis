import os, sys
from paths import RnaSeqPath

def trimmomatic_qsub():
    """
    qsub trimmomatic mission through trimmomatic_sub.sh
    """

    paths = RnaSeqPath()

    try:
        os.mkdir(os.path.join(paths.home, "trimmomatic_outputs"))
    except IOError:
        pass

    n_jobs = len(os.listdir(paths.fastq)) / 2
    job_arr = "-t 1-" + str(n_jobs)
    adapterfa = sys.argv[1]

    command = "qsub {} trimmomatic_sub.sh {}".format(job_arr, adapterfa)
    os.system(command)


if __name__ == "__mian__":
    trimmomatic_qsub()