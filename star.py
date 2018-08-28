import os, sys
from paths import RnaSeqPath
from glob import glob
import pickle as pk
from utils import dic_to_string

    
def generate_genome_index():
    """
    Run genome index generation
    """

    n_threads = os.cpu_count()
    paths = RnaSeqPath()

    option_dic = { "--runThreadN" : n_threads,
                "--runMode" : "genomeGenerate",
                "--genomeDir" :  paths.hg38_l1_root,
                "--genomeFastaFiles" : paths.hg38_l1_fasta,
                "--sjdbGTFfile" : paths.hg38_l1_annotation,
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

    paths = RnaSeqPath()
    try:
        f = open(os.path.join(paths.temp, 'star_temp'), 'rb')
    except OSError:
        pass
    else:
        with f:
            paired_files = pk.load(f)
        return paired_files

    # all fastq files
    if path:
        files = glob(os.path.join(path, "*.cleaned.fastq"))
    else:
        files = glob(os.path.join(paths.trimmomatic_outputs, "*.cleaned.fastq"))

    paired_files = []
    # find paired files
    while files:
        # find the forward file, save file name, remove it from files array
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
            if pair_id in f2 and "cleaned" in f2:
                paired_files.append(tuple((f1, f2)))
                files.pop(idx)
                break

    try:
        f = open(os.path.join(paths.temp, "star_temp"), "wb")
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

    paths = RnaSeqPath()
    try:
        os.mkdir(paths.star_outputs)
    except IOError:
        pass

    n_threads = os.cpu_count()
    reads = get_paired_reads()[int(sys.argv[2]) - 1]
    out_put_prefix = "{}_".format(os.path.basename(reads[0]).split(".")[0])
    option_dic = { "--runThreadN" : n_threads,
                "--genomeDir" :  paths.hg38_l1_root,
                "--readFilesIn" : "{} {}".format(reads[0], reads[1]),
                "--outFileNamePrefix" : os.path.join(paths.star_outputs, out_put_prefix)
                }

    option = dic_to_string(option_dic)

    command = "STAR {option}".format(option=option)
    os.system(command)


def main(opt):
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