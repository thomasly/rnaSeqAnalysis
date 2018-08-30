from utils import generate_bash_file, clean, qsub
import os, sys
from paths import RnaSeqPath
from glob import glob

def samtools_qsub(opt):
    """
    """

    paths = RnaSeqPath()
    if opt == "filtering":
        bam_files = os.path.join(paths.star_outputs, "*.bam")
    elif opt == "sorting":
        bam_files = os.path.join(paths.samtools_outputs, "*.bam")
    n_jobs = len(glob(bam_files))
    
    shell_file = generate_bash_file(
        filename_base="samtools",
        job_name="samtools_{}".format(opt),
        job_arr=n_jobs,
        commands=[
            "module load samtools/0.1.19",
            "module load python/3.6.4",
            "python3 {} $SGE_TASK_ID {}".format(
                os.path.join(
                    paths.scripts,
                    "samtools.py"
                ),
                opt
            )
        ]
    )
    qsub(shell_file)
    qsub(clean(after="samtools_{}".format(opt)))


if __name__ == "__main__":
    samtools_qsub(sys.argv[1])
