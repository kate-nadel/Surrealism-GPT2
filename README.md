# Surrealism-GPT2
Final project for Programming for Cultural Heritage @ Pratt Institute. Fall 2020 with Matt Miller.


## Motivation and purpose
Blah :)

Please see my notes on the art history aspect of this project in the ArtHistNotes file.

## Workflow

1. Download the <a href="https://github.com/metmuseum/openaccess">MetObject CSV</a>, and run the data.py script to write out a CSV of only the titles of works of art by artists who are considered Surrealist (see the ArtHistNotes file for my process for selecting artists and issues with the methodology)

This new file is called Met_Surrealist_Titles.txt - I train the GPT-simple model on this file

2. Install <a href="https://brew.sh/">Homebrew</a> and <a href="https://github.com/pyenv/pyenv#locating-the-python-installation">pyenv</a>. GPT2 works with older version of tensorflow which requires an older version of python. I had issues with pyenv because I have another python environment manager installed, but found that adding ```eval "$(pyenv init -)"``` manually after setting the python version to 3.5.10 using ```pyenv global 3.5.10``` worked fine. You can check which version of python is running by running ```python -V```

3. GPT2
https://github.com/openai/gpt-2
https://github.com/minimaxir/gpt-2-simple

Using the gpt2_test.py script, run the model on the training data. I did this multiple times to see how many steps would generate the best results. Ultimately 200 steps generated the longest list of unique titles. While 1000 steps overfitted the model and result in the fewest unique generations. This training data was fairly small, ~825 samples to train from, and the text lengths are quite small (because they're titles rather than speech, tweets, etc). So 200 steps worked best.

Generated text will appear in the terminal screen.

Run gpt2_gen_text.py script to write out the text to a JSON file.

This file is saved as GPT2_Surrealist_Text_200new.JSON

Every time I ran the model, some of the original titles were included in the new generated dataset. If this is okay, run the process_gpt_text.py which generates a clean JSON list of titles. If you want to remove duplicates and create a list of only generated titles, run filter_for_duplicates.py script. While I ultimately decided to create a bot that would post both real and generated titles, I wanted to have a reference of all of the titles that were generated using GPT2. The unique titles of all generated titles are in the folder GPT2_generated_titles

What I did was duplicate this file, and then throw as many real titles from the original dataset as there were generated titles. I randomly interspersed them, and intentionally didn't include any that were redundant, boring, or could be triggering. Who needs redundant, boring, or triggering?

4. Twitterbot
Make an account for your bot and sign up for developer account on Twitter.

Make an account on AWS to use their Lambda to run your code server-less. In Lambda you'll be able to set an "event" which which trigger your code to run as often as you'd like, at specific recurring times.

Plug in your keys from your developer account into the lambda_function_generic.py script and zip that file and the JSON with all of the tweets to be posted.

Upload to AWS, test, and set event trigger.
