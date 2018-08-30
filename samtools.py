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
    out_put_file = os.path.basename(bam_file).split(".")[0] + "_mapped.bam"
    out_put_file = os.path.join(paths.samtools_outputs, out_put_file)
    command = "samtools view -b -F 4 {} > {}".format(bam_file, out_put_file)
    os.system(command)

if __name__ == "__main__":
    samtools_filtering()
