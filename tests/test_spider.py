import unittest
from spider import Spider

class TestSpider(unittest.TestCase):
    def test_search(self):
        bug = [
            ["|", " ", "|", ],
            ["#", "#", "#", "o", ],
            ["|", " ", "|", ],
        ]

        landscape = [
            [" ", " ", " ", " ", "|", " ", "|", ],
            [" ", " ", " ", " ", "#", "#", "#", "o", ],
            [" ", " ", " ", " ", "|", " ", "|", ],
            ["|", " ", "|", " ", " ", " ", " ", ],
            ["#", "#", "#", "o", " ", " ", " ", " ", ],
            ["|", " ", "|", " ", " ", " ", " ", ],
        ]

        spider = Spider(landscape, bug)
        self.assertEqual(2, spider.search())


if __name__ == "__main__":
    unittest.main()
