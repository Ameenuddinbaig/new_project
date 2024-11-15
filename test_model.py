{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5993edcc-ca1a-4193-8683-f96712fb1abd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# test_model.py\n",
    "\n",
    "import pytest\n",
    "from model import train_model\n",
    "from sklearn.datasets import load_iris\n",
    "\n",
    "def test_train_model():\n",
    "    model = train_model()\n",
    "    iris = load_iris()\n",
    "    X_test = iris.data[0:1]\n",
    "    prediction = model.predict(X_test)\n",
    "    assert prediction is not None\n",
    "    assert len(prediction) == 1\n"
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
