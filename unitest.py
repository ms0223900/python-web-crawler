import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        # self.browser = webdriver.Firefox()
        # 主要是設定 webdirver remote
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def testYahoo(self):
        self.browser.get('http://www.yahoo.com')
        assert 'Yahoo' in self.browser.title

        elem = self.browser.find_element_by_name('p')  # Find the search box
        elem.send_keys('seleniumhq' + Keys.RETURN)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)