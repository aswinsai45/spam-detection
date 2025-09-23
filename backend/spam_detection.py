import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
data = pd.read_csv('spam.csv', encoding='latin-1')
data = data[['v1', 'v2']]                  # Keep only label & message
data.rename(columns={'v1': 'label', 'v2': 'message'}, inplace=True)

# Encode labels: ham=0, spam=1
data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label_num'], test_size=0.2, random_state=42
)

# Convert text to TF-IDF features
tfidf = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Sample prediction
sample_msg = ["Congratulations! You've won a free ticket."]
sample_tfidf = tfidf.transform(sample_msg)
prediction = model.predict(sample_tfidf)
print("\nSample Prediction:", "Spam" if prediction[0] else "Ham")
