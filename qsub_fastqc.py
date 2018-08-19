import os
from glob import glob
import multiprocessing as mp

batch_size = mp.cpu_count()

data_path = os.path.abspath("/ifs/data/proteomics/projects/L1_rnaseq/fastq")
home_path = os.path.abspath("..")

fastq_ext = os.path.join(data_path, "*.fastq.gz")
file_names = glob(fastq_ext)
n_file = len(file_names)
n_nodes = max(n_file // batch_size, 16)

inputs = ""
for indx, f in enumerate(file_names):
    inputs += " " + f
    if indx % batch_size == 0 and indx != 0:
        command = "qsub -pe openmid " + str(n_nodes) + " " + inputs
        os.system(command)
