from flask import Flask, render_template, request
import knn
import log_reg
import mnbbow
import mnbtfidf
import svm
# Initialize Flask app
app = Flask(__name__)

# Define a route to render the input form
@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        input_sentence = request.form['sentence']
        results = classify_sentence(input_sentence)
    return render_template('index.html', results=results)

@app.route('/contact_us',methods=['GET','POST'])
def contact_us():
    if request.method=="POST":
        pass
    return render_template('contact_us.html') 

# Function to classify a sentence using all five models
def classify_sentence(sentence):
    results = []
    # Use each of the five pre-trained models to classify the sentence
    prediction1 = mnbbow.predict(sentence)
    prediction2 = mnbtfidf.predict(sentence)
    prediction3 = svm.predict(sentence)
    prediction4 = knn.predict(sentence)
    prediction5 = log_reg.predict(sentence)

    # Assuming the models predict 1 for spam and 0 for ham
    results.append(('multinomial naive bayes - bow', prediction1 ))
    results.append(('multinomial naive bayes - tfidf', prediction2 ))
    results.append(('support vector machine', prediction3 ))
    results.append(('k Nearest Neighbours', prediction4 ))
    results.append(('Logistic Regression', prediction5 ))

    return results

if __name__ == '__main__':
    app.run(debug=True)
