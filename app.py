{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3bf2c8f-57ce-41b4-abff-3408d547777f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app.py\n",
    "\n",
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the pre-trained model\n",
    "model = joblib.load('model.joblib')\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"Machine Learning API is running!\"\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    data = request.get_json(force=True)\n",
    "    features = data['features']\n",
    "    prediction = model.predict([features])\n",
    "    return jsonify(prediction=int(prediction[0]))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, host='0.0.0.0')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
