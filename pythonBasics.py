import pytest
import os

"""
@pytest.fixture is a decorator provided by the pytest framework,
one of the most popular testing frameworks for Python.
Fixtures are a powerful feature for setting up preconditions for tests,
such as preparing data, state, or configurations that tests may require.
"""
@pytest.fixture
def temp_file():
    with open("temp_file.txt", "w") as f:
        f.write("Hello, pytest!")
    # No explicit teardown is needed here because of the context manager,
    # but this is where you'd usually put teardown logic if needed.
    yield "temp_file.txt"
    # Teardown code to remove the temporary file after the test runs
    os.remove("temp_file.txt")

def test_temp_file_content(temp_file):
    with open(temp_file, "r") as f:
        content = f.read()
    assert content == "Hello, pytest!"
