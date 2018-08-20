#!/bin/bash

#$ -N rnaSeqFastqc
#$ -cwd -V
## -pe openmpi 4-8
#$ -o /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.out
#$ -e /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.err

module load python/3.6.4

python3 trimmo.py $1 $SGE_TASK_ID
# python3 fastqc_exe.py $1