import os, logging, sys
from glob import glob
import multiprocessing as mp
from datetime import datetime
from paths import RnaSeqPath


def main():
    start = datetime.now()
    paths = RnaSeqPath()
    data_path = paths.fastq

    outputs_path = paths.fastqc_outputs
    try:
        os.mkdir(outputs_path)
    except IOError:
        pass

    fastq_ext = os.path.join(data_path, "*.fastq.gz")
    file_names = glob(fastq_ext)
    batch_size = mp.cpu_count()
    n_batch = int(sys.argv[1])
    f_start = batch_size * n_batch
    f_end = min(batch_size * (n_batch + 1), len(file_names))
    try:
        batch_files = file_names[f_start:f_end]
    except IndexError:
        print("IndexError raised!")
        return

    pool = mp.Pool(mp.cpu_count())

    tasks = []
    for f in batch_files:
        command = "fastqc -o " + outputs_path + " " + f
        tasks.append(command)

    pool.map(lambda x: os.system(x), tasks)
    pool.close()
    pool.join()

    end = datetime.now()
    print("Time consumed: {}".format(end - start))

if __name__ == "__main__":
    main()
