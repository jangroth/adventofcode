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

    def test_run_checksum(self):
        print(InventoryManagement('../resources/aoc2.txt').checksum())
