#!/bin/bash

#$ -N STAR_mapping_job
#$ -cwd -V
#$ -pe openmpi 1-32 -l mem_free=16G
#$ -o /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.out
#$ -e /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.err


module load python/3.6.4
module load star/2.4.5a
module load samtools/1.3

python3 star.py $1 $SGE_TASK_ID