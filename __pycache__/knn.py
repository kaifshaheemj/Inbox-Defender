import joblib
import warnings
warnings.filterwarnings('ignore')

def predict(sentence):
    model_filename = 'models/knn_model.pkl'
    vectorizer_filename = 'models/knn_vectorizer.pkl'
    # Load the trained model and vectorizer from the files (for testing or later use)
    loaded_model = joblib.load(model_filename)
    loaded_vectorizer = joblib.load(vectorizer_filename)

    # Test the loaded model on a new dataset
    text_to_test = [sentence]
    X_new = loaded_vectorizer.transform(text_to_test)
    prediction = loaded_model.predict(X_new)

    # Convert prediction (0 for not spam, 1 for spam) to human-readable label
    if prediction[0] == 0:
        return f"The \"{sentence}\" is ham"
    else:
        return f"The \"{sentence}\" is spam"
