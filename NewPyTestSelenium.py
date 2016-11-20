import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://theradavist.com//")
    # driver.find_element_by_name("s").send_keys("specialized")
    driver.quit()
