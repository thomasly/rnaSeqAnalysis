import os
from paths import RnaSeqPath
from datetime import datetime


def generate_bash_file(filename_base="_qsub_temp.sh",
job_name=None,
threads=None,
mem_free=None,
job_arr=None,
out_log=None,
err_log=None,
hold_jid=None,
commands=[]):
    """
    automatically generate bash file for qsub

    retrun:
    full path to the file.
    """
    paths = RnaSeqPath()
    temp = paths.temp
    try:
        os.mkdir(temp)
    except IOError:
        pass
    
    timestamp = str(datetime.now().day) + \
                str(datetime.now().hour) + \
                str(datetime.now().minute) + \
                str(datetime.now().microsecond)
    filename = filename_base + "_" + timestamp + ".sh"
    file_path = os.path.join(temp, filename)
    with open(file_path, "w") as f:
        f.write("#!/bin/bash\n")

        if job_name:
            string = "#$ -N {}\n".format(job_name)
            f.write(string)
        if threads:
            string = "#$ -pe openmpi 1-{}\n".format(threads)
            f.write(string)
        if mem_free:
            string = "#$ -l mem_free={}\n".format(mem_free)
            f.write(string)
        if job_arr:
            string = "#$ -t 1-{}\n".format(job_arr)
            f.write(string)

        if out_log:
            string = "#$ -o {}\n".format(os.path.join(paths.qsub_outputs, 
                                        out_log))
        else:
            string = "#$ -o {}\n".format(os.path.join(paths.qsub_outputs, 
                                        "$JOB_NAME_$JOB_ID.out"))
        f.write(string)

        if err_log:
            string = "#$ -e {}\n".format(os.path.join(paths.qsub_outputs, 
                                        out_log))
        else:
            string = "#$ -e {}\n".format(os.path.join(paths.qsub_outputs, 
                                        "$JOB_NAME_$JOB_ID.err"))
        f.write(string)

        if hold_jid:
            string = "#$ -hold_jid {}\n".format(hold_jid)

        f.write('\n'.join(commands))

    return file_path


def qsub(file_name, args=None):
    """
    qsub the file to hpc
    """
    if args:
        args_str = ' '.join(args)
        command = "qsub {} {}".format(file_name, args_str)
        os.system(command)
    else:
        command = "qsub {}".format(file_name)
        os.system(command)


def dic_to_string(dic={}):
    """
    transform dic to a command line string.
    """
    opt_string = ""
    for key, value in dic.items():
        opt_string += key + " " + str(value) + " "
    return opt_string


if __name__ == "__main__":
    generate_bash_file("test.sh", 
                    job_name="test_job", 
                    threads=8, 
                    mem_free='8G', 
                    job_arr=4, 
                    out_log="test.out", 
                    err_log="test.err", 
                    commands=["python3"])
