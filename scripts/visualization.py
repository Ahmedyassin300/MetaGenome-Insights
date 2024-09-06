import matplotlib.pyplot as plt
import seaborn as sns
from skbio.diversity import alpha_diversity


def plot_alpha_diversity(diversity_scores, samples):
    sns.barplot(x=samples, y=diversity_scores)
    plt.title('Alpha Diversity')
    plt.xlabel('Samples')
    plt.ylabel('Shannon Diversity Index')
    plt.show()

def plot_species_distribution(species_counts, species_labels):
    plt.pie(species_counts, labels=species_labels, autopct='%1.1f%', startangle=90)
    plt.title('Species Distribution')
    plt.show()

if __name__== "__main__":
    alpha_diversity_scores = [0.8, 0.6, 0.9]
    samples = ['Sample1', 'Sample2', 'Sample3']

    plot_alpha_diversity(alpha_diversity_scores, samples)

    species_counts = [50, 30, 20]
    species_label = ['Species1', 'Species2', 'Species3']

    plot_species_distribution(species_counts, species_label)




