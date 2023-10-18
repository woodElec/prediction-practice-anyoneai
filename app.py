from flask import Flask, render_template, request
import logging

import predictor

app = Flask(__name__)

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":
        # Make predictions
        '''if 'file' not in request.files:
            app.logger.info("No file")
            return "No file loaded"
        
        request_file = request.files.get('file')

        if request_file.filename == "":
            return "No file selected"'''

        data = [[5.1, 1.5, 4.5, 0.2], [5.1, 0.5, 4.5, 0.4]]
        result = predictor.predict(data=data)
        return result

    return render_template("upload_data.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True, use_reloader=False)


