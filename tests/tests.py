from selenium import webdriver
import unittest

class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

class NewVisitorTest(VisitorTest):

    def test_can_read_the_home_page(self):
        # Zoe wants to take a look at the code club site.
        # She opens up the browser at the homepage:
        self.browser.get('http://127.0.0.1:8000/virtualmicroscope/')
        self.browser.implicitly_wait(3)

        # She checks that the title shows that she's in the correct place.
        self.assertIn('NYU School of Medicine Virtual Microscope', self.browser.title)

if __name__ == '__main__':
    unittest.main()
