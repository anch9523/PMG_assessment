import unittest
import os

import pandas as pd


class MyTestCase(unittest.TestCase):
    os.system("csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv")

    def test_csv_combiner(self):
        output_file = pd.read_csv("combined.csv")
        self.assertEqual(list(output_file.columns), ["email_hash", "category", "filename"])
        self.assertEqual(output_file.filename.unique(), ['accessories.csv', 'clothing.csv'])


if __name__ == '__main__':
    unittest.main()
