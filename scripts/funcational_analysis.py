import pandas as pd
from patsy.eval import annotated_tokens


def annotate_genes(gene_list, database):
    annotate_genes = []
    for gene in gene_list:
        if gene in database:
            annotate_genes.append(database[gene])
        else:
            annotated_genes_append("Unknown")
    return annotated_genes

def load_kegg_database(file_path):
    kegg_db = pd.read_csv(file_path)
    return dict(zip(kegg_db['gene'], kegg_db['function']))

if __name__ == "__main__":
    gene_list = ['gene1', 'gene2', 'gene3']
    kegg_db = load_kegg_database("data/kegg_database.csv")

    annotated_genes = annotate_genes(gene_list, kegg_db)
    print(annotated_genes)
