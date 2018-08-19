import os, logging, sys
from glob import glob
import multiprocessing as mp
from datetime import datetime

def execute(command):
    pid = os.getpid()
    logging.info("pid: {}".format(pid))
    os.system(command)

def main():
    start = datetime.now()
    data_path = os.path.abspath("/ifs/data/proteomics/projects\
    /L1_rnaseq/fastq")
    home_path = os.path.abspath("..")

    outputs_path = os.path.join(home_path, "fastqcOutputs")
    try:
        os.mkdir(outputs_path)
    except IOError:
        pass

    fastq_ext = os.path.join(data_path, "*.fastq.gz")
    file_names = glob(fastq_ext)
    batch_size = mp.cpu_count()
    n_batch = int(sys.argv[1]) - 1
    f_start = batch_size * n_batch
    f_end = max(batch_size * (n_batch + 1), len(file_names))
    try:
        batch_files = file_names[f_start:f_end]
    except IndexError:
        return

    pool = mp.Pool(mp.cpu_count()*8)

    tasks = []
    for f in batch_files:
        command = "fastqc -o " + outputs_path + " " + f
        tasks.append(command)

    pool.map(execute, tasks)
    pool.close()
    pool.join()

    end = datetime.now()
    logging.info("Time consumed: {}".format(end - start))

if __name__ == "__main__":
    main()
