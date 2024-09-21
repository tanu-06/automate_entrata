# Pytest Selenium !

1.Steps to Create a Virtual Environment:
git clone https://github.com/tanu-06/automate_entrata.git
cd automate_entrata

2.Create a Virtual Environment:
python3 -m venv venv

3.Activate the Virtual Environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate

# To install Pytest and Selenium, you can use pip, which is the package installer for Python. Here are the steps:

1.Open your terminal or command prompt.
2.Make sure you have Python and pip installed. You can check by running:
python --version
pip --version

3.Install Pytest and Selenium by running the following commands:
pip install pytest
pip install selenium

4.Verify the installation: You can check if they are installed correctly by running:
pytest --version
python -c "import selenium; print(selenium.__version__)"

# To run Automated Entrata site project, follow these steps:
1.Packages required:
  pytest
  selenium
  
2.Navigate to your project directory
cd /tests

3.Run Pytest by executing the following command:
Command to run: pytest

4.To run a specific test file
pytest test_example.py

