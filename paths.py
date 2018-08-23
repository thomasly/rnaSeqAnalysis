import os

class RnaSeqPath:
    """
    provide all the necessary paths
    """

    def __init__(self):
        # path to YL
        self.current = os.path.abspath(os.curdir)
        self.home = os.path.dirname(self.current)

        # path to Sunny
        self.sunny_home = os.path.dirname(self.home)
        self.projects = os.path.dirname(self.sunny_home)

        # paths to RNA-seq fastq data
        self.l1_rnaseq = os.path.join(self.projects, "L1_rnaseq")
        self.fastq = os.path.join(self.l1_rnaseq, "fastq")
        self.annotation = os.path.join(self.l1_rnaseq, "annotation")

        # paths to roots
        self.proteomics = os.path.dirname(self.projects)
        self.data = os.path.dirname(self.proteomics)
        self.ifs = os.path.dirname(self.data)
        self.xs338 = os.path.join(self.ifs, "home", "xs338")

        # paths to trimmomatic java package and adapters
        self.trimmomatic = os.path.join(self.xs338, "Trimmomatic-0.36", "trimmomatic-0.36.jar")
        self.adapterfa = os.path.join(self.xs338, "Trimmomatic-0.36", "adapters", "TruSeq-adapters.fa")

        # paths to genome files
        self.genome = os.path.join(self.home, "genome")
        self.hg38_root = os.path.join(self.genome, "hg38")
        self.genome_fasta = os.path.join(self.hg38_root, "hg38.fa")

        # paths to outputs folders
        self.outputs_home = os.path.join(self.home, "rnaSeqAnalysisOutputs")
        self.fastqc_outputs = os.path.join(self.outputs_home, "fastqc_outputs")
        self.trimmomatic_outputs = os.path.join(self.outputs_home, "trimmomatic_outputs")
        self.star_output = os.path.join(self.outputs_home, "star_outputs")
        
