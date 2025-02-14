import numpy as np
import os
from get_data import data_extract, get_data, stopword_file
from numba_plsa.corpus import CorpusBuilder
from numba_plsa.plsa import PLSAModel

np.random.seed(1701)


def get_stopwords(fname):
    with open(fname, "r", encoding="latin-1") as f:
        return set(
            line.split(" ", 1)[0].strip() for line in f if line[0] not in [" ", "|"]
        )


def get_article_text(fname):
    text = ""
    with open(fname, "r", encoding="latin-1") as f:
        for line in f:
            if "Lines:" in line:
                break
        for line in f:
            text += line.replace("\n", " ")
    return text


def print_title(txt):
    print("\n{0}\n{1}".format(txt, "=" * len(txt)))


def plsa_example(data_extract, stopwords):
    print_title("Building corpus")
    CB = CorpusBuilder(stopwords=stopwords, min_len=3, max_len=8)
    doc_count = 0
    for root, directories, fnames in os.walk(data_extract):
        for fname in fnames:
            n = os.path.join(root, fname)
            CB.add_document(name=n, text=get_article_text(n))
            doc_count += 1
            print("Processed {0} documents\r".format(doc_count))
    doc_term = CB.get_doc_term()

    print_title("\nRunning pLSA")
    P = PLSAModel()
    n_topics = 10
    P.train(doc_term, n_topics=n_topics, n_iter=20, min_count=15, method="numba")

    print_title("\nTop topic terms")
    top_topic_words = P.top_topic_terms(5, normalized=True)
    for i in range(n_topics):
        print(
            "Topic {0}: {1}".format(
                i + 1, ", ".join(CB.get_term(j) for j in top_topic_words[i])
            )
        )


if __name__ == "__main__":

    print_title("Fetching data")
    get_data()
    stops = get_stopwords(stopword_file)

    plsa_example(data_extract, stops)
