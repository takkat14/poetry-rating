from string import punctuation

def preprocess_text_tf_idf(text):
    text = text.lower()
    text = text.replace(r"\n", " ")
    for p in punctuation:
        text = text.replace(p, " ")
    text = text.replace(r" {2,}", " ")
    return text