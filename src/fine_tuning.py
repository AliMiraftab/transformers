from datasets import load_dataset
from pprint import pprint
from transformers import AutoTokenizer

import pandas as pd

import datasets


finetuning_dataset_path = "lamini/lamini_docs"
finetuning_dataset = datasets.load_dataset(finetuning_dataset_path)

MODEL = "EleutherAI/pythia-70m"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
tokenizer.pad_token = tokenizer.eos_token

def tokenize_function(example):
    return tokenizer(example['question'], return_tensors="np", padding="max_length", truncate=True, )

tokenized_data = finetuning_dataset.map(tokenize_function, batch=True, batch_size=1, )

prompt_template_q = """ ### Question:
{question}

### Answer:
"""

print((finetuning_dataset['question']))