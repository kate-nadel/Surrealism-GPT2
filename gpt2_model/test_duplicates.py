import json

# load the out put from the generator
data = json.load(open("GPT2_Surrealist_Text0.json"))
# when I run this for both files GPT2_Surrealist_Text0 (which was generated at 356 steps) and GPT2_Surrealist_Text_new (1000 steps),
# I generated a new list but when I copy/paste some to the old dataset, it still seems like there are duplicates


orginal_titles = []

# load the input from your file, change the file name here
with open('Met_Surrealist_Titles.txt') as infile:
	for line in infile:
		orginal_titles.append(line)





for line in data:
    sentences = line.split("\n")

    for s in sentences:

    	if s not in orginal_titles:
        	# this one is not in the orginal file
        	print(s)
        	print("----")

json.dump(sentences, open("Surrealist_Text_unique0.json", "w"), indent=2)
