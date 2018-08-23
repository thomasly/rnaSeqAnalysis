import os, sys
from paths import RnaSeqPath

def trimmomatic_qsub():
    """
    qsub trimmomatic mission through trimmomatic_sub.sh
    """

    paths = RnaSeqPath()

    try:
        os.mkdir(paths.trimmomatic_outputs)
    except IOError:
        pass

    n_jobs = int(len(os.listdir(paths.fastq)) / 2)
    job_arr = "-t 1-" + str(n_jobs)

    command = "qsub {} trimmomatic_sub.sh {}".format(job_arr, paths.adapterfa)
    os.system(command)

    cleaning = "qsub -hold_jid rnaSeqTimmomatic clean_temp.sh"
    os.system(cleaning)


if __name__ == "__main__":
    trimmomatic_qsub()
