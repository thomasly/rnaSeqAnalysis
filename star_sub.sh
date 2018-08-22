#!/bin/bash

#$ -N STAR_job
#$ -cwd -V
#$ -pe openmpi 32
#$ -o /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.out
#$ -e /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.err


module load python/3.6.4
module load star

python3 star.py $SGE_TASK_ID