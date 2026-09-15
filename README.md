# 📧 Spam Email Classifier

A small practice project to learn scikit-learn — classifies email text as Spam or Not Spam using CountVectorizer + a Naive Bayes model, served through a simple Flask app.

# Project Structure
├── models/        # cv.pkl (vectorizer) and clf.pkl (trained classifier)
├── templates/      # HTML for the web form
├── app.py          # Flask routes
├── utils.py         # Loads the model and runs predictions
└── requirements.txt

# Process to Run
Run it
bash
git clone https://github.com/khyati999/Spam-Email-Classifier.git
cd Spam-Email-Classifier
pip install -r requirements.txt
python app.py

Then open http://localhost:8080, paste in some email text, and see the prediction.

There's also a JSON API at /api/predict (POST with {"content": "..."}).
