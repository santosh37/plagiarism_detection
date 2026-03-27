import os
from plagiarism_model import compute_similarity, overall_similarity, highlight_matches

def read_files(folder):
    docs = {}
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                docs[file] = f.read()
    return docs

docs = read_files("data")
names = list(docs.keys())

for i in range(len(names)):
    for j in range(i+1, len(names)):
        print(f"\nComparing {names[i]} and {names[j]}")

        s1, s2, sim = compute_similarity(docs[names[i]], docs[names[j]])
        score = overall_similarity(sim)
	percentage = round(score * 100, 2)

	print(f"Similarity Score: {percentage}%")

        matches = highlight_matches(s1, s2, sim)

        for m in matches:
            print("\nMatch:")
            print(m[0])
            print("↔")
            print(m[1])
            print(f"Score: {m[2]:.2f}")