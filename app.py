from flask import Flask, render_template, request, jsonify
import prediction

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status': 'error',
                    'message': 'Empty Review'}
    else:
        sentiment, path = prediction.predict(review)
        response = {'status': 'success',
                    'message': 'Got it',
                    'sentiment': sentiment,
                    'path': path}
    return jsonify(response)


@app.route('/', methods=[])
def save():
    date = request.json.get('date')
    product = request.json.get('product')
    review = request.json.get('review')
    sentiment = request.json.get('sentiment')

    data_entry = date + "," + product + "," + review + "," + sentiment

    with open("./static/assests/dtat_files/data_entry.csv", "a") as f:
        f.write(data_entry + "\n")

    return jsonify({'status': 'success',
                    'message': 'Data Logged'})


if __name__ == '__main__':
    app.run(debug=True)