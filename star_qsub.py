import os, sys
from paths import RnaSeqPath
from utils import generate_bash_file, qsub
from time import sleep


def star_qsub(job):
    """
    qsub star mission through star_sub.sh
    """

    if job == "indexing":
        shell_file = generate_bash_file(job_name="star_indexing", 
                        threads=4, 
                        out_log="star_indexing.out", 
                        err_log="star_indexing.err", 
                        commands = ["module load star/2.4.5a", 
                            "module load python/3.6.4", 
                            "python3 star.py indexing"])
        qsub(shell_file)
        

    if job == "mapping":
        paths = RnaSeqPath()

        try:
            os.mkdir(paths.star_outputs)
        except IOError:
            pass

        commands = []
        commands.append("module load star/2.4.5a")
        commands.append("module load python/3.6.4")
        commands.append("python3 star.py mapping $SGE_TASK_ID")
        n_jobs = int(len(os.listdir(paths.trimmomatic_outputs)) / 5 * 2)
        shell_file = generate_bash_file(job_name="star_mapping",
                        threads=4,
                        job_arr=n_jobs,
                        commands=commands)
        qsub(shell_file)

        commands = ["module load star/2.4.5a", 
                "rm {}".format(os.path.join(paths.temp, 'star_temp')),
                "STAR --genomeLoad Remove"]
        shell_file = generate_bash_file(hold_jid='star_mapping', commands=commands)
        qsub(shell_file)


if __name__ == "__main__":
    option = input("Pleas choose the job you want to run (1 - indexing, 2 - mapping): ")
    if option == "1":
        star_qsub("indexing")
    elif option == "2":
        star_qsub("mapping")
    else:
        print("Option does not exist.")
