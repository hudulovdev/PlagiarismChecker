from collections import Counter
import re

def get_word_frequencies(text):
    # Remove special characters and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Split the text into individual words
    words = text.split()
    # Count the frequency of each word
    word_frequencies = Counter(words)
    return word_frequencies

def calculate_similarity(doc1, doc2):
    freq1 = get_word_frequencies(doc1)
    freq2 = get_word_frequencies(doc2)

    # Calculate the similarity between the two documents using cosine similarity
    intersection = set(freq1.keys()) & set(freq2.keys())
    dot_product = sum(freq1[word] * freq2[word] for word in intersection)

    magnitude1 = sum(freq1[word] ** 2 for word in freq1.keys())
    magnitude2 = sum(freq2[word] ** 2 for word in freq2.keys())

    similarity = dot_product / (magnitude1 ** 0.5 * magnitude2 ** 0.5)
    return similarity

def check_plagiarism(doc1, doc2, threshold=0.8):
    similarity = calculate_similarity(doc1, doc2)
    if similarity >= threshold:
        return "Plagiarism detected."
    else:
        return "No plagiarism detected."

# Example usage
document1 = "Enter 1st document: "
document2 = input("Enter 2nd document: ")
result = check_plagiarism(document1, document2)
print(result)
