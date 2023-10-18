import pickle

def predict(data):
    # load model
    with open("iris_model.pkl", 'rb') as f:
        model = pickle.load(f)

    return model.predict()