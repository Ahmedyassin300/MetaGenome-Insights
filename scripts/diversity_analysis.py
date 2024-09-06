from itertools import count

from scipy.special import result
from scipy.stats import alpha
from skbio.diversity import alpha_diversity, beta_diversity
from skbio.stats.distance import permanova
import pandas as pd

def calculate_alpha_diversity(counts, metric='shannon'):
    return alpha_diversity(metric, counts)

def calculate_beta_diversity(distance_matrix, sample_ids):
    dm = beta_diversity('braycurtis', distance_matrix)
    result = permanova(dm, sample_ids)
    return result

if __name__ == "__main__":
    counts = pd.DataFrame([[5, 3, 0], [4, 1, 2], [3, 2, 1]], columns=['species1', 'species2', 'species3'])
    sample_ids = ['Sample1', 'Sample2', 'Sample3']

    alpha = calculate_alpha_diversity(counts)
    print(f"Alpha Diversity: {alpha}")

    beta = calculate_beta_diversity(counts, sample_ids)
    print(f"Beta Diversity: {beta}")