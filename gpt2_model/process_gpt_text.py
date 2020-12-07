# processing the large block of JSON text that is generated from gpt_gen_text.py
# unnecessary to run after running test test_duplicates.py


import json

data = json.load(open("Surrealist_Text_unique.json"))

for line in data:
    sentences = line.split("\n")

    for s in sentences:
        print(s)
        print("----")

json.dump(sentences, open("Surrealist_tweets_unique_processed.json", "w"), indent=2)
