import pickle
# import matplotlib.pyplot as plt
import numpy as np

def tokenizer(sentence: str, word2int_mapping: dict) -> list[int]:
    """Tokenizer
    Replace words, punctuations, characters with assigend int based on word2int dictionary.
    If a charecter is not exist, replace it with -1

    Arguments:

    Returns:
    """
    tokenized = list()
    for word in sentence.lower().split(" "):
        try:
            tokenized.append(word2int_mapping[word])
        except KeyError:
            tokenized.append(-1)
    
    return tokenized

def embed(tokenized_sequence: list[int], embeddings: np.array) -> np.array:
    """
    Arguments:

    Returns:
    """
    embed_size = embeddings.shape[1]
    output = np.empty((len(tokenized_sequence), embed_size))
    for i, e in enumerate(tokenized_sequence):
        if e == -1:
            output = np.zeros((1, embed_size))
        else:
            output[i] = embeddings[e]
    return output

def softmax(x, axis):
    """
    """
    x_exp = np.exp(x)
    return x_exp / np.expand_dims(np.sum(x_exp, axis=1), axis=1)

def attention(q, k, v):
    """
    """
    def calculate_weights(q, k):
        """
        """
        return softmax(np.matmul(q, np.transpose(k)) / np.sqrt(k.shape[1]), axis=1)
    
    return np.matmul(calculate_weights(q, k), v)





