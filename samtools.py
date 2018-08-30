from paths import RnaSeqPath
import os, sys
import pickle as pk
from glob import glob

def get_file_name(index):
    """
    """
    paths = RnaSeqPath()
    try:
        f = open("sam_temp", "br")
    except OSError:
        pass
    else:
        with f:
            files = pk.load(f)
        return files[index]

    files = glob(os.path.join(paths.star_outputs, "*.bam"))
    try:
        f = open("sam_temp", "bw")
    except OSError:
        raise
    else:
        with f:
            pk.dump(files, f)
    
    return files[index]

    
def samtools_filtering():
    """
    """

    paths = RnaSeqPath()
    try:
        os.mkdir(paths.samtools_outputs)
    except OSError:
        pass

    bam_file = get_file_name(int(sys.argv[1]) - 1)
    output_file = os.path.basename(bam_file).split(".")[0] + "_mapped.bam"
    output_file = os.path.join(paths.samtools_outputs, output_file)
    command = "samtools view -b -F 4 {} > {}".format(bam_file, output_file)
    os.system(command)

def samtools_sorting():
    """
    """
    paths = RnaSeqPath()
    try:
        os.mkdir(paths.samtools_sorted)
    except OSError:
        pass
    
    if os.path.exists("samtools_sort_temp"):
        with open("samtools_sort_temp", "br") as f:
            files = pk.load(f)
    else:
        files = glob(os.path.join(paths.samtools_outputs, "*mapped.bam"))
        with open("samtools_sort_temp", "bw") as f:
            pk.dump(files, f)

    bam_file = files[int(sys.argv[1]) - 1]
    output_file = os.path.basename(bam_file).split(".")[0] + "_sorted.bam"
    output_file = os.path.join(paths.samtools_sorted, output_file)

    command = "samtools sort -n {} {}".format(
        bam_file,
        output_file 
    )
    os.system(command)


if __name__ == "__main__":
    if sys.argv[2] == "filtering":
        samtools_filtering()
    elif sys.argv[2] == "sorting":
        samtools_sorting()
    else:
        print("Option ({}) not valid.".format(sys.argv[2]))

