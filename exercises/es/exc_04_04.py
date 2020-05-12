import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# Crea un objeto Doc para cada texto en TEXTS
for ____ in ____:
    # Encuentra en el doc y crea una lista de los spans resultantes
    spans = [____[____:____] for match_id, start, end in matcher(doc)]
    # Obtén los tuples (carácter de inicio, carácter del final, label) resultantes
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # Da formato a los resultados como tuples con (doc.text, entidades)
    training_example = (____, {"entities": ____})
    # Añade el ejemplo a los datos de entrenamiento
    ____.____(____)

print(*TRAINING_DATA, sep="\n")