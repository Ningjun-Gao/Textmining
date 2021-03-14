import spacy
import neuralcoref
nlp = spacy.load('en')
neuralcoref.add_to_pipe(nlp)

doc = nlp(u'My sister has a dog. She loves him')

doc._.coref_clusters
doc._.coref_clusters[1].mentions
doc._.coref_clusters[1].mentions[-1]
doc._.coref_clusters[1].mentions[-1]._.coref_cluster.main

token = doc[-1]
token._.in_coref
token._.coref_clusters

span = doc[-1:]
span._.is_coref
span._.coref_cluster.main
span._.coref_cluster.main._.coref_cluster