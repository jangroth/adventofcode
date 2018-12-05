from unittest import TestCase

from aoc.day02 import InventoryManagement


class TestInventoryManagement(TestCase):

    def test_checksum(self):
        inventory_management = InventoryManagement.__new__(InventoryManagement)
        inventory_management.content = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

        self.assertEqual(12, inventory_management.checksum())

    def test_common_letters(self):
        inventory_management = InventoryManagement.__new__(InventoryManagement)
        inventory_management.content = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

        self.assertEqual('fgij', inventory_management.common_letters())

    def test_two_strings_are_different_by_one_character(self):
        inventory_management = InventoryManagement.__new__(InventoryManagement)

        self.assertEqual(False, inventory_management._are_different_by_one_character('foo', 'foo')[0])
        self.assertEqual(False, inventory_management._are_different_by_one_character('foo', 'bar')[0])
        self.assertEqual(False, inventory_management._are_different_by_one_character('abcde', 'edcba')[0])
        self.assertEqual(False, inventory_management._are_different_by_one_character('abcde', 'abffe')[0])
        self.assertEqual((True, 'abcd'), inventory_management._are_different_by_one_character('abcde', 'abcdf'))

    def test_run_checksum(self):
        print(InventoryManagement('../resources/aoc2.txt').checksum())

    def test_run_common_letters(self):
        print(InventoryManagement('../resources/aoc2.txt').common_letters())
