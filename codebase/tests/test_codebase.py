import os
import unittest

import pandas as pd

import codebase


data_path = os.path.join(codebase.__path__[0], 'data')


class test_Perceptron(unittest.TestCase):

    def test_predict(self):
        """
        Testing the perceptron

        """
        weights = [-0.1, 0.20653640140000007, -0.23418117710000003]
        df = pd.read_csv(os.path.join(data_path, 'test.csv'))
        dataset = df.values.tolist()

        for row in dataset:
            prediction = codebase.predict(row, weights)
            self.assertAlmostEqual(row[-1], prediction)
