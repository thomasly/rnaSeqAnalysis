#!/bin/bash

#$ -N STAR_job
#$ -cwd -V
#$ -pe openmpi 1-2
#$ -o /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.out
#$ -e /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.err
#$ -m ea
#$ -M liuy08@nyumc.org

module load python/3.6.4
module load star

python3 trimmo.py $SGE_TASK_ID
# python3 fastqc_exe.py $1