import json

import pytest_html
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="edge", help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.node.driver = driver  # attach driver to test node
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.failed:
        driver = getattr(item, 'driver', None)
        if driver:
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(screenshot_path)
            extra.append(pytest_html.extras.image(screenshot_path))
    report.extra = extra
