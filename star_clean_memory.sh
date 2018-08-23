#!/bin/bash

#$ -hold_jid STAR_mapping_job
#$ -N STAR_cleaning_memory
#$ -cwd -V
#$ -o /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.out
#$ -e /ifs/data/proteomics/projects/Sunny/YL/qsuboutputs/$JOB_NAME_$JOB_ID.err


module load star/2.4.5a

rm ./*temp
STAR --genomeLoad Remove