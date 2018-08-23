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

    n_jobs = int(len(os.listdir(paths.trimmomatic_outputs)) / 5 * 2)
    job_arr = "-t 1-" + str(n_jobs)

    command1 = "qsub star_sub.sh indexing"
    os.system(command1)

    command2 = "qsub -hod_jid STAR_indexing_job {} star_sub.sh mapping".format(job_arr)
    os.system(command2)

    cleaning = "qsub -hold_jid STAR_mapping_job clean_temp.sh"
    os.system(cleaning)


if __name__ == "__main__":
    star_qsub()