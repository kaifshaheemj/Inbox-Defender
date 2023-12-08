import pickle 
import re
import nltk
from nltk.stem.porter import PorterStemmer
import warnings
warnings.filterwarnings('ignore')
#nltk.download('stopwords')
stopwords =nltk.corpus.stopwords.words("english")
ps = PorterStemmer()
def text_process(i):
    review = re.sub('[^a-zA-Z]', ' ',i)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if  word not in stopwords]
    review = ' '.join(review)
    return review 
def predict(sentence):
    new_messages =sentence
    # Preprocess the new messages

    mnb=pickle.load(open('models/mnb_model.sav','rb'))
    count_vec=pickle.load(open('models/mnb_vectorizer.sav','rb'))
    message=text_process(new_messages)
    predictions = mnb.predict(count_vec.transform([message]).toarray())
    if predictions == 1:
        return f"The \"{sentence}\" is spam"
    else:
        return f"The \"{sentence}\" is ham"