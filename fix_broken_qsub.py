import os
from glob import glob
from paths import RnaSeqPath
from utils import generate_bash_file, qsub, clean

def trimmomatic_qsub():
    """
    qsub trimmomatic mission through trimmomatic_sub.sh
    """

    paths = RnaSeqPath()
    # make the dir for outputs
    try:
        os.mkdir(paths.trimmomatic_outputs)
    except IOError:
        pass
    # calculate job number based on fastq files number
    shell_file = generate_bash_file(
        filename_base="trim",
        job_name="fix_Trimmomatic4",
        threads=2,
        commands=[
            "module load python/3.6.4",
            "python3 {} $1".format(os.path.join(paths.scripts, "fix_broken_trimmo.py"))
        ]   
    )
    qsub(shell_file, [paths.adapterfa])
    qsub(clean(after="fix_Trimmomatic4"))


if __name__ == "__main__":
    trimmomatic_qsub()
