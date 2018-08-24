import os, sys
from paths import RnaSeqPath

def star_qsub(job):
    """
    qsub star mission through star_sub.sh
    """

    if job == "indexing":
        command = "qsub star_indexing_sub.sh"
        os.system(command)

    if job == "mapping":
        paths = RnaSeqPath()

        try:
            os.mkdir(paths.star_outputs)
        except IOError:
            pass

        n_jobs = int(len(os.listdir(paths.trimmomatic_outputs)) / 5 )
        job_arr = "-t 1-" + str(n_jobs)

        command = "qsub -hold_jid STAR_indexing_job {} star_mapping_sub.sh".format(job_arr)
        os.system(command)

        cleaning_memory = "qsub star_clean_memory.sh"
        os.system(cleaning_memory)


if __name__ == "__main__":
    option = input("Pleas choose the job you want to run (1 - indexing, 2 - mapping): ")
    if option == "1":
        star_qsub("indexing")
    if option == "2":
        star_qsub("mapping")
    else:
        print("Option does not exist.")
