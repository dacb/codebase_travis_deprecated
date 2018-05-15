def predict(row, weights):
    """
    Super simple one layer perceptron based on this example:
        https://machinelearningmastery.com/
            implement-perceptron-algorithm-scratch-python/
    """
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]
    if activation >= 0.0:
        return 1
    else:
        return 0.0
