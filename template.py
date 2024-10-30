import numpy as np

import numpy as np
import student_script  # replace 'student_script' with the actual filename

def test_function():
    # Test 1: Check if the function returns correct output
    input_data = np.array([1, 2, 3])
    expected_output = np.array([1, 4, 9])  # Example expected result
    result = student_script.some_function(input_data)
    assert np.array_equal(result, expected_output), f"Expected {expected_output}, but got {result}"
