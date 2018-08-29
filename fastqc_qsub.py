import os, sys
from utils import generate_bash_file, qsub

sh_file = generate_bash_file(
    filename_base="fastqc",
    job_name="rnaSeqFastqc",
    commands=[
        "module load fastqc",
        "module load python/3.6.4",
        "python3 fastqc.py $1"
    ]
)
for t in range(5):
    qsub(sh_file, [t])
