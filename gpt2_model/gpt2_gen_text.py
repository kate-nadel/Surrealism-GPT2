# saving the text generated when run at 200 steps

import gpt_2_simple as gpt2
import json

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

# gpt2.generate(sess)


text = gpt2.generate(sess, return_as_list=True, batch_size=5, nsamples=5)

with open ("GPT2_Surrealist_Text_200new.json", "w") as output:
    json.dump(text, output, indent=2)
