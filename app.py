from flask import Flask, jsonify
from joblib import load 
from model.train import load_model, load_data, split_data, test_model

app = Flask(__name__)


@app.route('/')
def index():
    """
    Display the main webpage where users can enter theirs details
    which we will then pass to the prediction endpoint
    """
    return "Hello World!"

@app.route('/predict_test')
def predict_test():
    """
    Endpoint for displaying the confusion matrix 
    of the previously trained model
    """
    model = load_model()
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # converting the ndarray to a list so that we can json serialise it
    report = test_model(model, "Train", X_train, y_train).tolist()


    return jsonify({"test_type": "Train", "confusion_matrix": report})


if __name__ == '__main__':
    app.run(debug=True)