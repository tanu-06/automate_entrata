import time
from selenium.webdriver.common.by import By
import logging


def getLogger():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter(" %(asctime)s :%(levelname)s : %(name)s :%(message)s ")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger


def test_homepage(setup):
    """
    Navigate to homepage and validate webpage is properly fetch or not.
    Validate using actual title and expected title.
    If not matched then raise and assert.

    Steps Performed:
    1. Navigate to HomePage
    2. Fetch title of Home Page
    3. Verify title is - Property Management Software | Entrata
    """
    log = getLogger()

    log.info("1.Navigate to HomePage")
    driver = setup

    log.info("2.Fetch title of Home Page")
    act_title = driver.title

    log.info("3.Verify title is - Property Management Software | Entrata ")
    expected_title = "Property Management Software | Entrata"
    assert act_title == expected_title, "expected title not matched"


def test_footerpage(setup):
    """
     Firstly we go to bottom of the webpage using javascript script.
     and then match the string with actual string
     if not raise an assert.

     Steps Performed:
     1. Navigate to HomePage
     2. go to bottom of the HomePage
     3. Fetch the text present in the footer
     4. Verify text/string - Sales: 1.800.700.2097 matched
    """
    log = getLogger()
    log.info("1.Navigate to HomePage")
    driver = setup

    log.info("2.Go to bottom of the HomePage")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    log.info("3.Fetch the text present in the footer")
    footer_text = driver.find_element(By.LINK_TEXT, "Sales: 1.800.700.2097").text

    log.info("4.Verify text/string - Sales: 1.800.700.2097 matched")
    acc_text = "Sales: 1.800.700.2097"
    assert footer_text == acc_text, "expected footer not matched"


def test_navigatepage(setup):
    """
    Here we click on hyperlink - Join us at Summit 2024!
    and move to new tab when we click on hyperlink
    then implementation is we collect windows ID's of all tabs
    and then close all tabs.

    Steps Performed:
    1.Navigate to HomePage
    2. click on hyperlink - Join us at Summit 2024!
    3. collect the len of windowsID
    4. Verify if windowd id not matched
    """
    log = getLogger()
    log.info("1.Navigate to HomePage")
    driver = setup

    log.info("2.click on hyperlink - Join us at Summit 2024!")
    driver.find_element(By.XPATH, "//a[@class='white-button center-button hover_red left_btn w-inline-block']").click()

    log.info("3.collect the len of windowsID")
    window_handles = driver.window_handles

    log.info("4.Verify if windowd id not matched")
    assert len(window_handles) == 2, "Two tabs should be opened"
