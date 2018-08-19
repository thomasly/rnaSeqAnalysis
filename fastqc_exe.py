import os, logging
from glob import glob
import multiprocessing as mp
from datetime import datetime

def execute(command):
    pid = os.getpid()
    logging.info("pid: {}".format(pid))
    os.system(command)

start = datetime.now()
data_path = os.path.abspath("/ifs/data/proteomics/projects/L1_rnaseq/fastq")
home_path = os.path.abspath("..")

outputs_path = os.path.join(home_path, "fastqcOutputs")
try:
    os.mkdir(outputs_path)
except IOError:
    pass

fastq_ext = os.path.join(data_path, "*.fastq.gz")
file_names = glob(fastq_ext)

pool = mp.Pool(mp.cpu_count()*8)

tasks = []
for f in file_names:
    command = "fastqc -o " + outputs_path + " " + f
    tasks.append(command)

pool.map(execute, tasks)
pool.close()
pool.join()

end = datetime.now()
logging.info("Time consumed: {}".format(end - start))
