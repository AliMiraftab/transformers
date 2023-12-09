"""Tokinizer with Python
1. Define word2int dictionary
2. Make generatore over your input data
3. Build your preprocessing function with yield over your generatore
4. Consider special definitions ([EOS], [SOS], [PAD], ...) in your preprocessing function
"""

from pprint import pprint


data = [{'text': 'Consider special definitions ([EOS], [SOS], [PAD], ...) in your preprocessing function', 'summary': 'step 4'},
        {'text': 'Build your preprocessing function with yield over your generatore', 'summary': 'step 3'}]

example = 'Consider special definitions ([EOS], [SOS], [PAD], ...) in your preprocessing function'
split_characters = ['(', ')', ',', '?', '!', ':', '.']

list_tokenized_s = list()

def tokenized_sequence(sequence):
    for c in split_characters:
        sequence = sequence.replace(c, " "+c+" ")
    tokenized_s = [w.strip() for w in sequence.split() if sequence != ""]
    pprint(
        {'sequence': sequence,
         'token': tokenized_s}
    )
    return tokenized_s

# tokenized_data = list()
# for e in data:
#     tokenized_k = tokenized_sequence(e['text'])
#     tokenized_v = tokenized_sequence(e['summary'])
#     tokenized_data.append({'text_token': tokenized_k, 'summary_token': tokenized_v})

# print(">>> Generator")
# def data_gen(data):
#     for e_gen in data:
#         yield e_gen

# for e in data_gen(data):
#     tokenized_k = tokenized_sequence(e['text'])
#     tokenized_v = tokenized_sequence(e['summary'])
#     tokenized_data.append({'text_token': tokenized_k, 'summary_token': tokenized_v})   

tokenized_data = list()
def tokenizer_data(e):
    tokenized_k = tokenized_sequence(e['text'])
    tokenized_v = tokenized_sequence(e['summary'])
    tokenized_data.append({'text_token': tokenized_k, 'summary_token': tokenized_v})

iter_data = iter(data) 
while True:
    try:
        tokenizer_data(next(iter_data))
    except StopIteration:
        break
