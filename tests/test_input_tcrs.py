import os
import csv

def test_input_tcrs_length():
    # Get the path to the test data file
    test_data_path = os.path.join(os.path.dirname(__file__), '../test_data/input_tcrs.csv')
    with open(test_data_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    assert len(data) == 100_000
