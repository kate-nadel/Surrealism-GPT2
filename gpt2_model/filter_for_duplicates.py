import json

# load the out put from the generator
data = json.load(open("GPT2_Surrealist_Text_200new.json"))
# when I run this for both files GPT2_Surrealist_Text0 (which was generated at 356 steps) and GPT2_Surrealist_Text_new (1000 steps),
# I generated a new list but when I copy/paste some to the old dataset, it still seems like there are duplicates


orginal_titles = []

# load the input from your file, change the file name here
with open('Met_Surrealist_Titles.txt') as infile:
	for line in infile:
		# lets remove the line break at the end of the sentence and add it to the list
		orginal_titles.append(line.strip())

# make a new home for ones that pass the non-dupe test
non_dupes = []

for line in data:
	sentences = line.split("\n")

	for s in sentences:

		# lets check that it is not in the orginal file AND not a duplicate of a generated title
		if s not in orginal_titles and s not in non_dupes:
			# this one is not in the orginal file
			non_dupes.append(s)
		else:
			print("This is a dupe:",s)

json.dump(non_dupes, open("Surrealist_Text_unique_200new.json", "w"), indent=2)
