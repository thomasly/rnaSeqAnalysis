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
    n_jobs = int(len(glob(os.path.join(paths.fastq, "*.fastq.gz"))) / 2)
    shell_file = generate_bash_file(
        filename_base="trim",
        job_name="rnaSeqTrimmomatic",
        threads=2,
        job_arr=n_jobs,
        commands=[
            "module load python/3.6.4",
            "python3 trimmomatic.py $1 $SGE_TASK_ID"
        ]   
    )
    qsub(shell_file, [paths.adapterfa])
    qsub(clean(after="rnaSeqTrimmomatic"))


if __name__ == "__main__":
    trimmomatic_qsub()
