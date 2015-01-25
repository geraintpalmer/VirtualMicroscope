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

    def test_can_get_login_page(self):
        # Zoe wants to log in
        # She opens up the browser at the homepage
        self.browser.get('http://127.0.0.1:8000/virtualmicroscope/')
        self.browser.implicitly_wait(3)

        # She clicks on log in
        link = self.browser.find_element_by_link_text('Login')
        link.click()
        self.assertEquals('http://127.0.0.1:8000/admin/login/?next=/admin/', self.browser.current_url)

    def test_can_see_auraya(self):
        # Zoe wants to view the auraya slide
        # She opens the browser at the homepage
        self.browser.get('http://127.0.0.1:8000/virtualmicroscope/')
        self.browser.implicitly_wait(3)

        # She clicks on Auraya from the dropdown menu Collections
        dropdown = self.browser.find_elements_by_class_name('dropdown-toggle')
        dropdown[0].click()
        link = self.browser.find_element_by_link_text('auraya')
        link.click()
        self.assertEquals('http://127.0.0.1:8000/virtualmicroscope/collection/2/', self.browser.current_url)
        link = self.browser.find_element_by_link_text('dog')
        link.click()
        self.assertEquals('http://127.0.0.1:8000/virtualmicroscope/v/2/?p=1', self.browser.current_url)


if __name__ == '__main__':
    unittest.main()
