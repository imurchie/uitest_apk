import os

import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AndroidScrollTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../bin/uitest_apk-debug.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_scroll_elements(self):
        els = self.driver.find_elements_by_class_name('android.widget.Button')
        self.assertEqual(4, len(els))

        action = TouchAction(self.driver)
        action.press(els[-1]).move_to(els[0]).release().perform()
        el = self.driver.find_element_by_name('Button7')
        self.assertIsNotNone(el)


    def test_scroll_element_position(self):
        els = self.driver.find_elements_by_class_name('android.widget.Button')
        self.assertEqual(4, len(els))

        action = TouchAction(self.driver)
        action.press(els[-1]).move_to(x=10).release().perform()
        el = self.driver.find_element_by_name('Button7')
        self.assertIsNotNone(el)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidScrollTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
