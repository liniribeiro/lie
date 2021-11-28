

import spacy
from spacy import displacy


def name_extraction():

    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(u'meu nomee é Astolfo')
    return doc.ents[0]
    displacy.serve(doc, style="ent")


name_extraction()