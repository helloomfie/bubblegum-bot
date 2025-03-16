from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class BubblegumBotTrainer:
    def __init__(self):

        self.model = Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('classifier', MultinomialNB())
        ])
        
        self.training_data = [

        ]
    
    def train(self):

        X = [item['input'] for item in self.training_data]
        y = [item['intent'] for item in self.training_data]
        

        self.model.fit(X, y)
    
    def predict_intent(self, message):

        return self.model.predict([message])[0]
    
    def get_response(self, message):

        intent = self.predict_intent(message)
        matching_responses = [
            item['response'] for item in self.training_data 
            if item['intent'] == intent
        ]

        return random.choice(matching_responses) if matching_responses else "whatever."
