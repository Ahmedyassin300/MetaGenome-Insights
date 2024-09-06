from Bio import SeqIO
from skbio.io.format.fastq import fastq


def read_fastq(file_path):
    sequence = list(SeqIO.parse(file_path, "fastq"))
    print(f"Loaded {len(sequences)} sequences from {file_path}.")
    return sequences

def read_fastq(file_path):
    sequence = list(SeqIO.parse(file_path, "fastq"))
    print(f"Loaded {len(sequences)} sequences from {file_path}.")
    return sequences

if __name__ == "__main__":
    fastq_file = "data/sample_sequences.fastq"
    fastq_file = "data/sample_sequences.fastq"

    sequences_fastq = read_fastq(fastq_file)
    sequences_fastq = read_fastq(fastq_file)

    for seq_record in sequences_fastq[:5]:
        print(f"ID {seq_record.id}, Length: {len(seq_record.seq)}")


