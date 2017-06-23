import unittest
from app.utils.parse import (match, sub_downcase)

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass 

    def tearDown(self):
        pass
    
    def test_sub_downcase(self):
        text = "hello world"
        first_result = sub_downcase(text,0 , 4)
        self.assertEqual(first_result, text[0:4])
        second_result = sub_downcase(text, 0,1)
        self.assertEqual(second_result, 'h' )
    
    def test_match(self):
        text = "Google is a search engine service, google is also an engine for a lot of other services and tools"
        first_result = match(text, "google")
        self.assertEqual(first_result, "1, 36")
        second_result = match(text, "oo")
        self.assertEqual(second_result, "2, 37, 94")
        third_result = match(text, "Oo")
        self.assertEqual(third_result, "2, 37, 94")
        four_result = match(text, "a")
        self.assertEqual(four_result, "11, 15, 46, 51, 65, 89")
        five_result = match(text, "Sx")
        self.assertEqual(five_result, "<no matches>")

        len_result = match(text, "S" * 1000 )
        self.assertEqual(len_result, "<no matches>")

if __name__ == '__main__':
    unittest.main()
      