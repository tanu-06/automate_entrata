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
  
2.Navigate to your project directory:
cd /tests

3.Run Pytest by executing the following command:
Command to run: pytest

4.To run a specific test file:
pytest test_example.py

# Testcase performed 

All the testcase performed using web URL: https://www.entrata.com/b
1. TestCase1:

    Navigate to homepage and validate webpage is properly fetch or not.
    Validate using actual title and expected title.
    If not matched then raise and assert.

    Steps Performed:
    1. Navigate to HomePage
    2. Fetch title of Home Page
    3. Verify title is - Property Management Software | Entrata
  
2. TestCase2:

     Firstly I went to bottom of the webpage using javascript script module.
     and then match the string with actual string
     if not raise an assert.

     Steps Performed:
     1. Navigate to HomePage
     2. Go to bottom of the HomePage
     3. Fetch the text present in the footer
     4. Verify text/string - Sales: 1.800.700.2097 matched

3. TestCase3:

    Here we click on hyperlink - Join us at Summit 2024!
    and move to new tab when we click on hyperlink
    then implementation is we collect windows ID's of all tabs
    and then close all tabs.

    Steps Performed:
    1. Navigate to HomePage
    2. Click on hyperlink - Join us at Summit 2024!
    3. Collect the len of windowsID
    4. Verify if windowd id not matched

4. Create fixture:
   
    Opens the URL and return the driver
   
