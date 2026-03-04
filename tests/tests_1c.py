import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_addition():
    assert max_subarray_sum([1, 2])  == 3      # Test for zero addition

if __name__ == "__main__":
    pytest.main()