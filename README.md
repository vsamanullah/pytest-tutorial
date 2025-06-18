# pytest-tutorial
A hands-on guide to learning and mastering Pytest – from basics to advanced features with practical examples.

# Understanding Pytest

**Pytest** is a popular testing framework for Python, much like **JUnit** for Java and **NUnit** for C#. It is known for its simplicity, scalability, and support for writing both simple unit tests and complex functional test suites.

## 🔧 Prerequisites

- Python **3.8+** is required to use Pytest.
- Before proceeding, make sure Python is installed.

👉 If you're new to Python and need help installing it, check out this video tutorial:  
📺 [How to Install Python](https://youtu.be/SzIOGisGcy4)

👉 For detailed official documentation and guides, refer to:  
📘 [Pytest Official Docs – Getting Started](https://docs.pytest.org/en/stable/getting-started.html)

## 📦 Installing Pytest

After Python is successfully installed, you can install Pytest using pip:

```bash
pip install -U pytest
````

## 📁 What This Repo Covers

This repository is a practical guide to understanding Pytest. It includes:

* ✅ Basic test writing
* 🧪 Using assertions
* 🔁 Parameterization
* 🧩 Fixtures
* 🔌 Plugins
* 🛠 Best practices


## 🚀 Running the Tests
To execute the tests in this project, follow these steps:

1. **Navigate to the root folder** (which is this repo's base directory, named `pytest-tutorial`):

		cd pytest-tutorial


2. **Run the tests using the following command:**

	python -m pytest
	
This will automatically discover and run all the test cases in the current directory and its subfolders.


## 🔍 How Pytest Finds Tests
Pytest uses a simple naming convention to discover tests:

* **Test files** should start or end with `test`.

  Examples:

  * `test_example.py`
  * `example_test.py`

* **Test functions** inside those files should start with `test_`.

  Example:
  
		def test_addition():
			assert 2 + 2 == 4
		  
Following this naming convention ensures that Pytest will correctly detect and run your tests.


## ⚙️ Pytest Command-Line Options

You can run your tests in various ways using Pytest’s flexible command-line options.

For full reference, check the official Pytest usage documentation:  
📘 [Pytest CLI Usage Guide](https://docs.pytest.org/en/stable/how-to/usage.html#usage)

### ✅ Common Pytest Commands

1. **Run all tests in the project:**

  	 python -m pytest


2. **Run all tests with detailed output (verbose):**

   	python -m pytest -v
 

3. **Run tests and show print statements in the console (no output capturing):**

   	python -m pytest -s


4. **Run all tests in a specific file:**

   	python -m pytest tst/test_calc_add.py


5. **Run a specific test function in a file:**

   	python -m pytest tst/test_calc_add.py::test_calc_add_one


6. **Run all tests in a specific class:**

   	python -m pytest tst/test_calc_div_class.py::TestCalcDivClass
  

7. **Run a specific test method inside a class:**

   	python -m pytest tst/test_calc_div_class.py::TestCalcDivClass::test_calc_div_positive_no_exp