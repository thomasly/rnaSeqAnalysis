import os

class RnaSeqPath:

    def __init__(self):
        self.current = os.path.abspath(os.curdir)
        self.home = os.path.dirname(self.current)
        self.sunny_home = os.path.dirname(self.home)
        self.projects = os.path.dirname(self.sunny_home)
        self.l1_rnaseq = os.path.join(self.projects, "L1_rnaseq")
        self.fastq = os.path.join(self.l1_rnaseq, "fastq")
        self.annotation = os.path.join(self.l1_rnaseq, "annotation")
        self.proteomics = os.path.dirname(self.projects)
        self.data = os.path.dirname(self.proteomics)
        self.ifs = os.path.dirname(self.data)
        self.xs338 = os.path.join(self.ifs, "home", "xs338")
        self.trimmomatic = os.path.join(self.xs338, "Trimmomatic-0.36", "trimmomatic-0.36.jar")
        self.adapterfa = os.path.join(self.xs338, "Trimmomatic-0.36", "adapters", "TruSeq-adapters.fa")
        self.genome = os.path.join(self.sunny_home, "genome")
        self.genome_fasta = os.path.join(self.genome, "hg38.fa")
        self.trimmed = os.path.join(self.home, "trimmomatic_outputs")

        