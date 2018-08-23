import os
from paths import RnaSeqPath

def generate_bash_file(filename,
job_name=None,
threads=None,
mem_free=None,
job_arr=None,
out_log=None,
err_log=None,
commands=[]):
    """
    automatically generate bash file for qsub
    """
    paths = RnaSeqPath()
    with open(filename, "w") as f:
        f.write("#!/bin/bash\n")

        if job_name:
            string = "#$ -N {}\n".format(job_name)
            f.write(string)
        if threads:
            string = "#$ -pe openmpi {}\n".format(threads)
            f.write(string)
        if mem_free:
            string = "#$ -l mem_free={}\n".format(mem_free)
            f.write(string)
        if job_arr:
            string = "#$ -t 1-{}\n".format(job_arr)
            f.write(string)

        if out_log:
            string = "#$ -o {}\n".format(os.path.join(paths.qsub_outputs, out_log))
        else:
            string = "#$ -o {}\n".format(os.path.join(paths.qsub_outputs, "$JOB_NAME_$JOB_ID.out"))
        f.write(string)

        if err_log:
            string = "#$ -e {}\n".format(os.path.join(paths.qsub_outputs, out_log))
        else:
            string = "#$ -e {}\n".format(os.path.join(paths.qsub_outputs, "$JOB_NAME_$JOB_ID.err"))
        f.write(string)

        f.writelines(commands)


