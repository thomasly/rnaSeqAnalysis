import os, sys
from paths import RnaSeqPath
from glob import glob
import pickle as pk

def dic_to_string(dic={}):
    """
    transform dic to a command line string.
    """
    opt_string = ""
    for key, value in dic.items():
        opt_string += key + " " + str(value) + " "
    return opt_string
    

def generate_genome_index():
    """
    Run genome index generation
    """

    n_threads = os.cpu_count()
    paths = RnaSeqPath()

    option_dic = { "--runThreadN" : n_threads,
                "--runMode" : "genomeGenerate",
                "--genomeDir" :  paths.genome,
                "--genomeFastaFiles" : paths.genome_fasta,
                "--sjdbGTFfile" : paths.annotation,
                "--sjdbOverhang" : 150}

    option = dic_to_string(option_dic)

    command = "STAR {option}".format(option = option)
    os.system(command)


def get_paired_reads(path=None):
    """
    find the paired end RNAseq forward and reverse reading pair

    arguments:
    path - folder contains input .fastq files

    return:
    array contains all inputs paired in tuples
    """

    try:
        f = open("star_temp", "rb")
    except OSError:
        pass
    else:
        with f:
            paired_files = pk.load(f)
        return paired_files

    # all fastq files
    if path:
        files = glob(path)
    else:
        paths = RnaSeqPath()
        files = glob(os.path.join(paths.trimmomatic_outputs, "*.cleaned.fastq"))

    paired_files = []
    # find paired files
    while files:
        # find the forward file, save file name, remove it from files array
        f1 = None
        for idx, f in enumerate(files):
            if "R1" in f:
                f1 = f
                files.pop(idx)
                break
        # get file name
        f1_base = os.path.basename(f1)
        # the indentical part in the file names of the paired files
        pair_id = f1_base.split(".")[0][:-7]
        for idx, f2 in enumerate(files):
            if pair_id in f2:
                paired_files.append(tuple((f1, f2)))
                files.pop(idx)
                break

    try:
        f = open("star_temp", "wb")
    except IOError:
        raise
    else:
        with f:
            pk.dump(paired_files, f)

    return paired_files


def mapping():
    """
    Run mapping job
    """

    n_threads = os.cpu_count()
    paths = RnaSeqPath()
    reads = get_paired_reads(paths.trimmomatic_outputs)[int(sys.argv[2]) - 1]
    option_dic = { "--runThreadN" : n_threads,
                "--genomeDir" :  paths.genome,
                "--greadFilesIn" : reads,
                }

    option = dic_to_string(option_dic)
    value = ""

    command = "STAR {option} {value}".format(option=option, value=value)
    os.system(command)


def main(opt="indexing"):
    """
    run STAR
    """

    if opt == "indexing":
        generate_genome_index()
    if opt == "mapping":
        mapping()
    else:
        print("not a valid option.")


if __name__ == "__main__":
    main(sys.argv[1])