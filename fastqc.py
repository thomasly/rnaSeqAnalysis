import os, logging, sys
from glob import glob
import multiprocessing as mp
from datetime import datetime
from paths import RnaSeqPath


def main():
    """
    run fastqc with multithreads
    """
    start = datetime.now()
    paths = RnaSeqPath()
    data_path = paths.fastq

    # create output folder
    outputs_path = paths.fastqc_outputs
    try:
        os.mkdir(outputs_path)
    except IOError:
        pass

    # get the file paths
    fastq_ext = os.path.join(data_path, "*.fastq.gz")
    file_names = glob(fastq_ext)
    # get the files to run in parallel
    batch_size = mp.cpu_count()
    n_batch = int(sys.argv[1]) # argn[1]th batch
    # get the indeces of the start and end of this batch
    f_start = batch_size * n_batch
    f_end = min(batch_size * (n_batch + 1), len(file_names))
    # get file paths in this batch
    try:
        batch_files = file_names[f_start:f_end]
    except IndexError:
        print("IndexError raised!")
        return

    # initialize multiprocessing pool
    pool = mp.Pool(mp.cpu_count())
    # create tasks for multiprocessing
    tasks = []
    for f in batch_files:
        command = "fastqc -o {} {}".format(outputs_path, f)
        tasks.append(command)

    # run multiprocessing
    pool.map(lambda x: os.system(x), tasks)
    pool.close()
    pool.join()

    # print time consumed
    end = datetime.now()
    print("Time consumed: {}".format(end - start))

if __name__ == "__main__":
    main()
