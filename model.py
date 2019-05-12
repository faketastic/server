import pickle
import os

def get_model(model_path=None):
    if model_path is None:
        model_path = os.environ.get('MODEL_PATH')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model


if __name__ == '__main__':
    from db import engine

    pipeline = get_model()
    result = engine.execute('select * from tweets limit 1').fetchone()
    data = {}
    for key, value in result.items():
        data[key]= value

    prediction = pipeline.predict_proba([data['tweet_text']])
    print(prediction)

     
    