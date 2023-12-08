import joblib
import warnings
warnings.filterwarnings('ignore')
def predict(sentence):
    loaded_model = joblib.load('models/svm_model.sav')
    loaded_tfidf = joblib.load('models/svm_vectorizer.pkl')

    input_text = sentence
    is_spam = loaded_model.predict(loaded_tfidf.transform([input_text]))
    if is_spam == 1:
        return f"The \"{input_text}\" is spam"
    else:
        return f"The \"{input_text}\" is ham"