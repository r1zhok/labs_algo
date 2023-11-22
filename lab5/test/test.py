import unittest
from lab5.src.lab5 import main


class Test(unittest.TestCase):

    def test1(self):
        input_file = '../file1.txt'
        output_file = 'output1.txt'
        main(input_file, output_file)
        with open(output_file, 'r', encoding='UTF-8') as file:
            self.assertEqual('[]', str(eval(file.readline().strip())))

    def test2(self):
        input_file = '../file2.txt'
        output_file = 'output2.txt'
        main(input_file, output_file)
        with open(output_file, 'r', encoding='UTF-8') as file:
            self.assertEqual(str([['Сх2', ['Дон', 'Київ', 'Львів', 'Тер']], ['Сх3', ['Київ', 'Луг', 'Львів', 'Сев', 'Тер']]]),
                             str(eval(file.readline().strip())))


if __name__ == '__main__':
    unittest.main()
