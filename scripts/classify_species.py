import os

def run_kraken(input_file, db_path, output_file):
    os.system(f"kraken2 --db {db_path} {input_file} --output {output_file}")
    print(f"Classification complete. Results saved to {output_file}.")

def run_blast(input_file, db_path, output_file):
    os.system(f"blast -query {input_file} -db {db_path} -out {output_file} -outfmt 6")
    print(f"BLAST completed. Results saved to {output_file}.")

if __name__ == "__main__":
    input_file = "data/sample_sequences.fasta"
    kraken_db = "/path/to/kraken/db"
    blast_db = "/path/to/blast/db"
    output_kraken = "results/kraken_output.txt"
    output_blast = "results/blast_output.txt"

    run_kraken(input_file, kraken_db, output_kraken)
    run_blast(input_file, blast_db, output_blast)

