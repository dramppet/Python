class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Popy')

    def test_cat_size_is_increased(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as contex:
            self.cat.eat()
        self.assertEqual(str(contex.exception), 'Already fed.')

    def test_cannot_sleep(self):
        with self.assertRaises(Exception) as contex:
            self.cat.sleep()
        self.assertEqual(str(contex.exception), 'Cannot sleep while hungry')

    def test_cat_not_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
