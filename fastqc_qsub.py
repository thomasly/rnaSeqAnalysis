import os, sys
from utils import generate_bash_file, qsub, clean
from paths import RnaSeqPath
from glob import glob
from math import ceil

paths = RnaSeqPath()

# create the shell file for qsub
sh_file = generate_bash_file(
    filename_base="fastqc",
    job_name="rnaSeqFastqc",
    commands=[
        "module load fastqc",
        "module load python/3.6.4",
        "python3 fastqc.py $1"
    ]
)

# calculate how many qsub to run
threads = os.cpu_count()
m = int(ceil(len(glob(os.path.join(paths.fastq, "*.fastq"))) / threads))

# submit jobs to hpc
for t in range(m):
    qsub(sh_file, [t])

# cleaning the temporary shell files after main job is done
qsub(clean(after="rnaSeqFastqc"))
