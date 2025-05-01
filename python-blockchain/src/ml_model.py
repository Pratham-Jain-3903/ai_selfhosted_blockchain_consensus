import json
import pickle
import base64
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

class IrisModel:
    """A simple ML model for Iris flower classification"""
    
    def __init__(self):
        """Initialize a new model or load existing one"""
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.scaler = StandardScaler()
        self.classes = ['setosa', 'versicolor', 'virginica']
        self.is_trained = False
        self.data_count = 0
        
    def add_data_point(self, features, label):
        """
        Update the model with a single data point
        
        Args:
            features (list): [sepal_length, sepal_width, petal_length, petal_width]
            label (str): Flower type (setosa, versicolor, or virginica)
        
        Returns:
            bool: True if update succeeded
        """
        if not self._validate_data(features, label):
            return False
            
        label_idx = self.classes.index(label) if label in self.classes else -1
        if label_idx == -1:
            return False
        
        # If first data point, just store it
        if not self.is_trained:
            self.X = [features]
            self.y = [label_idx]
            self.is_trained = True
        else:
            # Otherwise add to existing data and retrain
            self.X.append(features)
            self.y.append(label_idx)
            
        # Retrain model with all data
        self._train_model()
        self.data_count += 1
        return True
        
    def predict(self, features):
        """Predict flower type from features"""
        if not self.is_trained:
            return {"error": "Model not trained yet"}
            
        if not self._validate_features(features):
            return {"error": "Invalid features format"}
            
        # Scale features and predict
        features_scaled = self.scaler.transform([features])
        prediction = self.model.predict(features_scaled)[0]
        
        # Return prediction and confidence scores
        probabilities = self.model.predict_proba(features_scaled)[0]
        result = {
            "predicted_class": self.classes[prediction],
            "confidence": float(probabilities[prediction]),
            "probabilities": {
                self.classes[i]: float(prob) 
                for i, prob in enumerate(probabilities)
            }
        }
        return result
    
    def _train_model(self):
        """Train or update the model with all data"""
        # Scale features
        self.scaler.fit(self.X)
        X_scaled = self.scaler.transform(self.X)
        
        # Train model
        self.model.fit(X_scaled, self.y)
    
    def _validate_data(self, features, label):
        """Validate format of data point"""
        if not self._validate_features(features):
            return False
            
        if not isinstance(label, str):
            return False
            
        return True
    
    def _validate_features(self, features):
        """Validate format of features"""
        if not isinstance(features, list) or len(features) != 4:
            return False
            
        # Check if all features are numeric
        try:
            for f in features:
                float(f)
            return True
        except:
            return False
    
    def serialize(self):
        """Serialize model to string for blockchain storage"""
        model_data = {
            "is_trained": self.is_trained,
            "data_count": self.data_count,
        }
        
        if self.is_trained:
            # Serialize the model and scaler
            model_bytes = pickle.dumps(self.model)
            scaler_bytes = pickle.dumps(self.scaler)
            x_bytes = pickle.dumps(self.X)
            y_bytes = pickle.dumps(self.y)
            
            model_data.update({
                "model": base64.b64encode(model_bytes).decode('utf-8'),
                "scaler": base64.b64encode(scaler_bytes).decode('utf-8'),
                "X": base64.b64encode(x_bytes).decode('utf-8'),
                "y": base64.b64encode(y_bytes).decode('utf-8')
            })
            
        return json.dumps(model_data)
        
    @classmethod
    def deserialize(cls, serialized_data):
        """Create model from serialized string"""
        model_obj = cls()
        
        try:
            model_data = json.loads(serialized_data)
            model_obj.is_trained = model_data.get("is_trained", False)
            model_obj.data_count = model_data.get("data_count", 0)
            
            if model_obj.is_trained:
                model_bytes = base64.b64decode(model_data["model"])
                scaler_bytes = base64.b64decode(model_data["scaler"])
                x_bytes = base64.b64decode(model_data["X"])
                y_bytes = base64.b64decode(model_data["y"])
                
                model_obj.model = pickle.loads(model_bytes)
                model_obj.scaler = pickle.loads(scaler_bytes)
                model_obj.X = pickle.loads(x_bytes)
                model_obj.y = pickle.loads(y_bytes)
                
            return model_obj
        except Exception as e:
            print(f"Error deserializing model: {e}")
            return model_obj