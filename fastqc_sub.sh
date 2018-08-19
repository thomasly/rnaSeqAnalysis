#!/bin/bash

#$ -N rnaSeqFastqc
#$ -cwd -V
#$ -o /ifs/data/proteomics/project/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.out
#$ -s /ifs/data/proteomics/project/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.err

module load fastqc
module load python/3.6.4

python3 fastqc_exe.py $SGE_TASK_ID