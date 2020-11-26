import unittest
import Old_MacDonald

class Test_Cases(unittest.TestCase):

    def test_one_word(self):
        text = 'macdonald'
        result = Old_MacDonald.old_macdonald(text)
        self.assertEqual(result, 'MacDonald')

    def multiple_test_case(self):
        text = 'corey'
        result = Old_MacDonald.old_macdonald(text)
        self.assertEqual(result, 'CorEy')

    def two_word_case(self):
        text = 'corey anderson'
        result = Old_MacDonald.old_macdonald(text)
        self.assertEqual(result, 'CorEy anderson')

    def test_with_symbols(self):
        text = "corey anderson is an Fast Bowler's "
        result = Old_MacDonald.old_macdonald(text)
        self.assertEqual(result, "CorEy anderson is an Fast Bowler's ")


if __name__ == '__main__':
    unittest.main()
