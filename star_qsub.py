import os, sys
from paths import RnaSeqPath

def star_qsub():
    """
    qsub star mission through star_sub.sh
    """

    paths = RnaSeqPath()

    try:
        os.mkdir(paths.star_output)
    except IOError:
        pass

    n_jobs = int(len(os.listdir(paths.fastq)) / 2)
    job_arr = "-t 1-" + str(n_jobs)

    command = "qsub {} star_sub.sh".format(job_arr)
    os.system(command)

    cleaning = "qsub -hold_jid STAR_job clean_temp.sh"
    os.system(cleaning)


if __name__ == "__main__":
    star_qsub()