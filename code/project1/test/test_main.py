import unittest
import os
from ..src.Main import Main
import testbook


class Test_main(unittest.TestCase):

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super(Test_main, self).__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()

        self.main = Main(1, False)
        print(f"self.main.addTwo(3)={self.main.addTwo(3)}")

    # returns the directory of this script regardles of from which level the code is executed
    def get_script_dir(self):
        return os.path.dirname(__file__)

    # tests unit test on addTwo function of main class
    def test_addTwo(self):

        expected_result = 7
        result = self.main.addTwo(5)
        self.assertEqual(expected_result, result)

    def test_get_page_nr(self):
        example_source='age disabled">Previous</span> <em class="current" data-total-pages="3">1</em> <a rel="next" aria-lab'
        closing_character='"'
        result = self.main.get_value_from_html_source(example_source, 'data-total-pages="', closing_character)
        expected_result=3
        self.assertEqual(expected_result, result)

    def test_get_nr_of_issues(self):
        example_source='aria-labelledby="issue_126_link'
        closing_character='_'
        result = self.main.get_value_from_html_source(example_source, 'aria-labelledby="issue_', closing_character)
        expected_result=126
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
