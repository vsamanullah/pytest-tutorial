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
* 🏷️ Markers
* 📂 conftest.py usage
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

## 🏷️ Using Markers in Pytest

**Markers** allow you to categorize and selectively run tests.
For example, you might have tests marked as `smoke`, `regression`, or `slow`.

### Example:

```python
import pytest

@pytest.mark.smoke
def test_login_valid():
    assert True

@pytest.mark.regression
def test_add_item_to_cart():
    assert True
```

### Running tests by marker:

```bash
python -m pytest -m smoke
```

### Registering custom markers:

Add them to `pytest.ini` to avoid warnings:

```ini
[pytest]
markers =
    smoke: quick checks for core functionality
    regression: full regression tests
```

---

## 🧩 Fixtures in Pytest

**Fixtures** are a powerful way to set up and tear down resources needed for your tests.
They help avoid repetitive code and keep tests clean.

### Example:

```python
import pytest

@pytest.fixture
def sample_data():
    return {"username": "test_user", "password": "secret"}

def test_user_login(sample_data):
    assert sample_data["username"] == "test_user"
```

### Running with fixture setup/teardown:

Fixtures can also use `yield` to run cleanup code after the test.

```python
@pytest.fixture
def db_connection():
    print("Connecting to DB")
    yield
    print("Closing DB connection")
```

---

## 🔁 Parameterization

Parameterization lets you run the same test logic with multiple sets of data.

### Example:

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (1, 1, 2),
    (10, -5, 5)
])
def test_addition(a, b, expected):
    assert a + b == expected
```

Run once, this will execute **three test cases**.

---

## 📂 The Role of `conftest.py`

The `conftest.py` file allows you to share **fixtures**, **hooks**, and **plugins** across multiple test files without importing them manually.

### Example:

**conftest.py**

```python
import pytest

@pytest.fixture
def api_client():
    return {"base_url": "https://api.example.com"}
```

**test\_api.py**

```python
def test_get_users(api_client):
    assert api_client["base_url"] == "https://api.example.com"
```

💡 **Tip:** Pytest automatically detects `conftest.py` in your project tree.

---

## 🔌 Using Pytest Plugins

Pytest has many plugins to extend its capabilities.
You can install them via `pip` and use them right away.

### Example: `pytest-html` for HTML reports

```bash
pip install pytest-html
python -m pytest --html=report.html
```

### Example: `pytest-xdist` for parallel execution

```bash
pip install pytest-xdist
python -m pytest -n 4
```

---

## 📂 Example Project Structure

```
pytest-tutorial/
│
├── tests/
│   ├── test_calc_add.py
│   ├── test_calc_div_class.py
│   └── test_api.py
│
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🛠 Best Practices

* **Use descriptive test names** (e.g., `test_user_login_with_valid_credentials` instead of `test_login1`)
* **Keep tests independent** (don’t rely on one test’s output for another)
* **Leverage fixtures** for setup/teardown
* **Mark slow or resource-heavy tests** so they can be skipped in quick runs
* **Use `pytest.ini`** to define markers, addopts, and other defaults
* **Run tests in CI/CD** for automation

---

## 📌 Summary

With Pytest, you can:

* Write clean and readable tests.
* Use fixtures for setup/teardown.
* Organize tests with markers.
* Share resources via `conftest.py`.
* Run tests flexibly using CLI options.
* Extend functionality with plugins.
* Apply best practices for maintainability.

For more information, explore:
📘 [Pytest Documentation](https://docs.pytest.org)

```