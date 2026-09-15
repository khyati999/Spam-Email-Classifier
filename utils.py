import pickle
from pathlib import Path

MODEL_DIR = Path(__file__).resolve().parent / 'models'

with (MODEL_DIR / 'cv.pkl').open('rb') as model_file:
    cv = pickle.load(model_file)

with (MODEL_DIR / 'clf.pkl').open('rb') as model_file:
    clf = pickle.load(model_file)

def make_prediction(email):
    tokenized_email = cv.transform([email])
    return 1 if int(clf.predict(tokenized_email)[0]) == 1 else -1