import joblib
from nltk.stem import WordNetLemmatizer
import nltk
import re
import warnings
warnings.filterwarnings('ignore')
lm = WordNetLemmatizer()
stopwords =nltk.corpus.stopwords.words("english")
def text_process_tf(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [lm.lemmatize(word) for word in review if not word in stopwords]
    review = ' '.join(review)
    return review
def predict(sentence):
    # Load the Multinomial Naive Bayes model and CountVectorizer model
    mnb = joblib.load('models/mnbtf_model.sav')
    cv_tfidf = joblib.load('models/mnbtf_vectorizer.pkl')

    new_text = sentence
    processed_text = text_process_tf(new_text)

    # Transform the new text data using the loaded CountVectorizer
    new_text_vectorized = cv_tfidf.transform([processed_text]).toarray()

    predicted_class = mnb.predict(new_text_vectorized)
    if(predicted_class[0]==1):
        return f"The \"{sentence}\" is spam"
    else:
        return f"The \"{sentence}\" is ham"