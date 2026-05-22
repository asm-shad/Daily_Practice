# Action Plam
# Convert Description to Vectors with TF-IDF
# - Remove common Eng stop words like the, a, in
# - Dark code: Hacking, cybercrime and dark web secrets {"hacking": 0.6, "Cybercrime": 0.7}
# - Every book becomes a vector of word scores |||| used for comparison
# Compute similarity between books [0.21, 1.0, 0.05, 0.78, 0.08]
# Create Mapping from Title to index 
# Define the Recommendation Function
# Find index, title = "Dark Code" => idx = 1
# Create a list of tuples: (book_index, similarity_score) [(0, 0.21), (1,1.0),(2, 0.05), (3, 0.78)]
# Sorts by similarity score(highest first), Skips the first one (which is the book itself)
# Extract the book indices and return these books titles and authors

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("books.csv")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['title'])

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]