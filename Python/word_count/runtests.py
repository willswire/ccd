import unittest
from testfile import *

TEST_DAT_1 = {'lorem': 158, 'ipsum': 191, 'dolor': 161, 'sit': 587, 'amet': 578, 'consectetur': 175, 
              'adipiscing': 233, 'elit': 214, 'sed': 714, 'do': 1, 'eiusmod': 1, 'tempor': 120, 'incididunt': 1, 
              'ut': 473, 'labore': 1, 'et': 449, 'dolore': 1, 'magna': 148, 'aliqua': 1, 'vitae': 452, 'auctor': 132, 
              'eu': 344, 'augue': 159, 'non': 305, 'arcu': 285, 'risus': 271, 'quis': 328, 'varius': 118, 'quam': 257, 
              'quisque': 107, 'eget': 452, 'nunc': 401, 'lobortis': 97, 'mattis': 212, 'aliquam': 292, 'gravida': 212, 
              'cum': 28, 'sociis': 30, 'natoque': 29, 'penatibus': 31, 'leo': 183, 'in': 602, 'turpis': 268, 
              'massa': 314, 'elementum': 241, 'tempus': 122, 'egestas': 350, 'metus': 60, 'vulputate': 156, 
              'scelerisque': 189, 'felis': 126, 'imperdiet': 127, 'proin': 145, 'fermentum': 145, 'ultrices': 224, 
              'neque': 283, 'ornare': 171, 'aenean': 129, 'euismod': 122, 'tincidunt': 299, 'dui': 195, 'lectus': 243, 
              'id': 506, 'faucibus': 292, 'nisl': 235, 'nullam': 105, 'odio': 213, 'pellentesque': 364, 'diam': 325, 
              'volutpat': 234, 'commodo': 191, 'nulla': 296, 'facilisi': 98, 'morbi': 288, 'iaculis': 103, 
              'urna': 216, 'lacus': 215, 'convallis': 130, 'posuere': 114, 'molestie': 98, 'at': 395, 'sem': 110, 
              'magnis': 29, 'porttitor': 129, 'vestibulum': 171, 'blandit': 140, 'cursus': 218, 'orci': 202, 
              'dapibus': 23, 'vel': 270, 'pharetra': 186, 'platea': 43, 'dictumst': 48, 'sagittis': 167, 'purus': 249, 
              'luctus': 41, 'bibendum': 150, 'tristique': 211, 'mi': 205, 'aliquet': 237, 'nec': 192, 'nibh': 247, 
              'tortor': 263, 'ac': 374, 'dignissim': 147, 'cras': 173, 'feugiat': 201, 'vivamus': 41, 
              'condimentum': 120, 'enim': 377, 'viverra': 319, 'accumsan': 120, 'tellus': 286, 'hac': 46, 
              'habitasse': 45, 'habitant': 79, 'senectus': 87, 'netus': 91, 'malesuada': 170, 'fames': 80, 
              'laoreet': 100, 'curabitur': 49, 'pretium': 182, 'fusce': 46, 'velit': 219, 'maecenas': 123, 
              'suspendisse': 157, 'a': 263, 'semper': 136, 'libero': 115, 'consequat': 139, 'interdum': 131, 
              'est': 180, 'ullamcorper': 197, 'mauris': 307, 'erat': 112, 'phasellus': 85, 'nisi': 145, 'porta': 73, 
              'mollis': 42, 'ultricies': 155, 'integer': 134, 'pulvinar': 166, 'nam': 66, 'justo': 93, 'donec': 175, 
              'duis': 151, 'venenatis': 112, 'hendrerit': 56, 'facilisis': 171, 'congue': 79, 'rhoncus': 111, 
              'sapien': 131, 'sodales': 77, 'etiam': 117, 'sollicitudin': 111, 'lacinia': 46, 'eleifend': 67, 
              'fringilla': 99, 'dictum': 125, 'ligula': 18, 'placerat': 103, 'praesent': 68, 'suscipit': 34, 
              'rutrum': 50, 'potenti': 28, 'ridiculus': 23, 'mus': 22, 'dis': 26, 'eros': 54, 'ante': 51, 
              'vehicula': 22, 'parturient': 25, 'montes': 22, 'nascetur': 23}


class PythonUnitTest(unittest.TestCase):
    def test_word_count(self):
        res_words, res_max, res_tot = word_count("data.txt")
        self.assertEqual(res_words[res_max], 714)
        self.assertEqual(res_tot, 29760)

    def test_no_file(self):
        res = word_count("missingfile.txt")
        self.assertEqual(res, None)

    def test_empty_file(self):
        res = word_count("empty.txt")
        self.assertEqual(res, None)

    def test_whitespace_file(self):
        res = word_count("whitespace.txt")
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
