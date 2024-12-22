from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class BubblegumBotTrainer:
    def __init__(self):
        # Create a machine learning pipeline
        self.model = Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('classifier', MultinomialNB())
        ])
        
        self.training_data = [
            # Your existing dataset goes here
        ]
    
    def train(self):
        # Prepare training data
        X = [item['input'] for item in self.training_data]
        y = [item['intent'] for item in self.training_data]
        
        # Train the model
        self.model.fit(X, y)
    
    def predict_intent(self, message):
        # Predict the intent of a message
        return self.model.predict([message])[0]
    
    def get_response(self, message):
        # Determine intent and select appropriate response
        intent = self.predict_intent(message)
        matching_responses = [
            item['response'] for item in self.training_data 
            if item['intent'] == intent
        ]
        
        # Randomly select a response
        return random.choice(matching_responses) if matching_responses else "whatever."
