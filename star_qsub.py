import os, sys
from glob import glob
from paths import RnaSeqPath
from utils import generate_bash_file, qsub, clean
from time import sleep


def star_qsub(job):
    """
    qsub star mission through star_sub.sh

    input:
    job - string, "indexing" or "mapping". choose the job you want to run.

    outputs:
    indexing - genome index files in the genome folder
    mapping - sam and log files in star_outputs folder
    """

    paths = RnaSeqPath()
    # STAR genome indexing job
    if job == "indexing":
        # create the shell file
        shell_file = generate_bash_file(job_name="star_indexing", 
            threads=4, 
            out_log="star_indexing.out", 
            err_log="star_indexing.err", 
            commands = ["module load star", 
                "module load python/3.6.4", 
                "python3 {} indexing".format(
                                        os.path.join(paths.scripts, 
                                        'star.py'))])
        # submit the shell file to hpc
        qsub(shell_file)
        
    # STAR RNA-seq alignment job
    if job == "mapping":

        try:
            os.mkdir(paths.star_outputs)
        except IOError:
            pass

        # shell commands
        commands = [
            "module load star",
            "module load python/3.6.4",
            "python3 {} mapping $SGE_TASK_ID".format(
                                os.path.join(
                                    paths.scripts, 
                                    'star.py'))
        ]

        # calculate job number based on the trimmomatic outputs
        n_jobs = int(len(glob(os.path.join(
                                paths.trimmomatic_outputs, 
                                "*.cleaned.fastq"))) / 2)

        # create shell file
        shell_file = generate_bash_file(job_name="star_mapping",
                        mem_free="35G",
                        threads=8,
                        job_arr=n_jobs,
                        commands=commands)
        # submit shell file to hpc
        qsub(shell_file)

        # clean temp files
        qsub(clean(after="star_mapping"))


if __name__ == "__main__":
    # choose indexing or mapping job
    option = input(
        "Pleas choose the job you want to run (1 - indexing, 2 - mapping): ")
    if option == "1":
        star_qsub("indexing")
    elif option == "2":
        star_qsub("mapping")
    else:
        print("Option does not exist.")
