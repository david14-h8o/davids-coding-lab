# word_frequency.py
from collections import Counter

def analyze_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower().split()
    counts = Counter(text)
    for word, freq in counts.most_common(10):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    fname = input("Enter filename: ")
    analyze_file(fname)
