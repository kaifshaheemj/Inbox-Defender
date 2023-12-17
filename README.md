
# InboxDefender

This project focuses on spam detection within textual data using several machine learning algorithms trained on the Spam Dataset. Various classification models such as KNN, SVM, Logistic Regression (with TF-IDF and Bag-of-Words approaches), and Multinomial Naive Bayes are employed to identify spam messages.

## Preprocessing

The Spam Dataset is utilized for training and testing the models. The NLTK library is used for text preprocessing, which involves tasks like tokenization, removing stopwords, and stemming or lemmatization to enhance model performance.

## Algorithms
The project employs the following algorithms and techniques:

* **K-Nearest Neighbors (KNN)**
* **Support Vector Machine (SVM)**
* **Logistic Regression**:
    * With both TF-IDF and Bag-of-Words approaches
* **Multinomial Naive Bayes**

Each algorithm is implemented with its specific approach to text representation and classification to compare their effectiveness in spam detection.

## Flask Application
The project files are structured as follows:

* dataset/: Directory containing the Spam Dataset and processed data.
* models/: Folder housing trained models for each algorithm.
* main.py: Flask application file for the web interface.
* ML_LAB_TEST_SPAM_DETECTION.ipynb: jupyter script for training the model


## Getting Started

To run this Application

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/spam-detection.git


2. Start the Flask application:
    ```bahs
    python main.py

3. Open your browser and visit http://localhost:5000 to access the spam detection interface.

4. Install dependencies (assuming you have Python and pip installed):
   ```bash
   pip install -r requirements.txt

I hereby attach the output files
![image](https://github.com/kaifshaheemj/Inbox-Defender/blob/main/image.png)
## Acknowledgements

The project utilizes NLTK for text preprocessing, enhancing the models' ability to detect spam messages effectively.

Feel free to explore the project, contribute, or utilize the models for your spam detection tasks!


## Authors

- [@kaifshaheemj](https://github.com/kaifshaheemj/)
- [@harish-123445](https://github.com/harish-123445/)

