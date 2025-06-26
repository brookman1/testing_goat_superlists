
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has head about a cool new online to-do app.  She goes
        # to check out its homepage

        self.browser.get('http://localhost:8000')

        # She noteces the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        #self.fail('Finish the test!')
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.TAG_ID, 'id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.spleep(0.5)

        table = self.browser.find_element(By.TAG_ID, 'id_list_table')
        rows = table.fin_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows),
                'New to-do item does not appear in table'
                )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        # explanatory text to that effect.
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(0.5)

        table = self.browser.find_element(By.TAG_ID, 'id_list_table')
        rows = table.fin_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
                any(row.text == '2: Use peacock feathers to make a fly'\
                        for row in rows),
                'New to-do item does not appear in table'
                )

        # The page updates again, and now shows both items on her list
        # self.fail('Finish he test!')

        # She visits that URL - her to-do list is still there.

        self.browser.get('http://localhost:8000')

        # She noteces the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
