# Surrealism-GPT2
Final project for Programming for Cultural Heritage @ Pratt Institute. Fall 2020 with Matt Miller

## Motivation and purpose
Blah :)

### Workflow

1. Download the <a href="https://github.com/metmuseum/openaccess">MetObject CSV</a>, and run the data.py script to write out a CSV of only the titles of works of art by artists who are considered Surrealist (see the ArtHistNotes file for my process for selecting artists and issues with the methodology)

This new file is called Met_Surrealist_Titles.txt - I train the GPT-simple model on this file

2. Install <a href="https://brew.sh/">Homebrew</a> and <a href="https://github.com/pyenv/pyenv#locating-the-python-installation">pyenv</a>. GPT2 works with older version of tensorflow which requires an older version of python. I had issues with pyenv because I have another python environment manager installed, but found that adding ```eval "$(pyenv init -)"``` manually after setting the python version to 3.5.10 using ```pyenv global 3.5.10``` worked fine. You can check which version of python is running by running ```python -V```

3. GPT2
https://github.com/openai/gpt-2
https://github.com/minimaxir/gpt-2-simple

Using the gpt2_test.py script, run the model on the training data.

Generated text will appear in the terminal screen.

Run gpt2_gen_text.py script to write out the text to a JSON file.

This file is saved as GPT2_Surrealist_Text.JSON

I processed this JSON file by running the process_gpt_text.py script which generates in the terminal screen the list of titles.



4. Twitterbot

Sign up for developer account, install tweepy.
