import os
from paths import RnaSeqPath
from datetime import datetime


def generate_bash_file(filename_base="_qsub_temp",
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

    inputs:
    possible qsub options
    commands - list of shell commands

    retrun:
    full path to the file.
    """
    paths = RnaSeqPath()
    temp = paths.temp
    try:
        os.mkdir(temp)
    except IOError:
        pass
    
    # add unique timestamp to shell file name
    timestamp = str(datetime.now().day) + \
                str(datetime.now().hour) + \
                str(datetime.now().minute) + \
                str(datetime.now().microsecond)
    filename = filename_base + "_" + timestamp + ".sh"
    file_path = os.path.join(temp, filename)

    # create file
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
            f.write(string)

        f.write('\n'.join(commands))

    return file_path


def qsub(file_name, args=None):
    """
    qsub the file to hpc
    
    inputs:
    file_name - the full path to the file needed to be submitted
    args - list of required args
    """

    if args:
        args_str = ' '.join(map(str, args))
        command = "qsub {} {}".format(file_name, args_str)
        os.system(command)
    else:
        command = "qsub {}".format(file_name)
        os.system(command)


def dic_to_string(dic={}):
    """
    transform dic to a command line string.

    input
    dic - commands as a dict

    output
    string contains all commands

    example:
    command_dic = {
        "-a": "b",
        "--c": "d"
    }

    dic_to_string(command_dic)
    -> "-a b --c d " (notice the space at the end of the string)
    """
    opt_string = ""
    for key, value in dic.items():
        opt_string += key + " " + str(value) + " "
    return opt_string


def clean(after=None):
    """
    generate the shell commands to clean up temp files

    input:
    after - job name. Cleaning starts after this job is done

    output:
    shell file path containing cleaning commands
    """

    paths = RnaSeqPath()
    shell_file = generate_bash_file(
        hold_jid=after,
        commands=[
            "rm -f ./*temp",
            "rm -f {}/*".format(paths.temp)
        ]
    )

    return shell_file





if __name__ == "__main__":
    generate_bash_file("test.sh", 
                    job_name="test_job", 
                    threads=8, 
                    mem_free='8G', 
                    job_arr=4, 
                    out_log="test.out", 
                    err_log="test.err", 
                    commands=["python3"])
