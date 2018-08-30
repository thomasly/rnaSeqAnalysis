from utils import generate_bash_file, clean, qsub
import os
from paths import RnaSeqPath
from glob import glob

def samtools_qsub():
    """
    """

    paths = RnaSeqPath()
    bam_files = os.path.join(paths.star_outputs, "*.bam")
    n_jobs = len(glob(bam_files))
    shell_file = generate_bash_file(
        filename_base="samtools",
        job_name="samtools_filtering",
        job_arr=n_jobs,
        commands=[
            "module load samtools",
            "module load python/3.6.4",
            "python3 {} $SGE_TASK_ID".format(
                os.path.join(
                    paths.scripts,
                    "samtools.py"
                )
            )
        ]
    )
    qsub(shell_file)
    qsub(clean(after="samtools_filtering"))


if __name__ == "__main__":
    samtools_qsub()
