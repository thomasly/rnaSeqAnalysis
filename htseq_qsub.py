import os
from glob import glob
from utils import generate_bash_file, qsub
from paths import RnaSeqPath

def htseq_count():
    """
    """

    paths = RnaSeqPath()

    try:
        os.mkdir(paths.htseq_outputs)
    except OSError:
        pass
    
    bam_files = glob(os.path.join(paths.samtools_sorted, "*sorted.bam"))
    alignment_files = " ".join(bam_files)
    gff_file = paths.hg38_l1_annotation
    output_file = os.path.join(paths.htseq_outputs, "htseq.out")

    shell_file = generate_bash_file(
        filename_base="htseq",
        job_name="htseq_job",
        commands=[
            "module load anaconda3",
            "source activate htseq",
            "htseq-count -f bam -r name {} {} > {}".format(
                alignment_files,
                gff_file,
                output_file
            )
        ]
    )
    qsub(shell_file)

if __name__ == "__main__":
    htseq_count()
