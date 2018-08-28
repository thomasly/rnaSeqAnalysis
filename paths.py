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
        self.hg38_fasta = os.path.join(self.hg38_root, "hg38.fa")
        self.hg38_l1_root = os.path.join(self.genome, "hg38_l1")
        self.hg38_l1_fasta = os.path.join(self.hg38_l1_root, "hg38_l1.fa")
        self.hg38_l1_annotation = os.path.join(self.hg38_l1_root, "annotation", "hg38_genes_l1.gtf")

        # paths to outputs folders
        self.qsub_outputs = os.path.join(self.home, "qsuboutputs")
        self.outputs_home = os.path.join(self.home, "rnaSeqAnalysisOutputs")
        self.fastqc_outputs = os.path.join(self.outputs_home, "fastqc_outputs")
        self.trimmomatic_outputs = os.path.join(self.outputs_home, "trimmomatic_outputs")
        self.star_outputs = os.path.join(self.outputs_home, "star_outputs")

        # temp folder
        self.temp = os.path.join(self.home, "temp")
        
