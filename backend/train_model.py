import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# 1. Load dataset
df = pd.read_csv("../spam.csv", encoding="latin-1")[['v1', 'v2']]
df.columns = ['label', 'message']

# 2. Encode labels (ham=not spam, spam=spam)
df['label'] = df['label'].map({'ham': 'not spam', 'spam': 'spam'})

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

# 4. Vectorization (text → numbers)
vectorizer = TfidfVectorizer(stop_words="english")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 5. Train model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 6. Evaluate
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Save model & vectorizer
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully!")
