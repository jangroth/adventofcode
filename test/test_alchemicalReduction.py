from unittest import TestCase

from aoc.day05 import AlchemicalReduction


class TestAlchemicalReduction(TestCase):

    def setUp(self):
        self.ar = AlchemicalReduction.__new__(AlchemicalReduction)

    def test_is_match(self):
        self.assertTrue(self.ar._is_match('aA'))
        self.assertTrue(self.ar._is_match('Aa'))
        self.assertFalse(self.ar._is_match('aa'))
        self.assertFalse(self.ar._is_match('AA'))
        self.assertFalse(self.ar._is_match('ab'))
        self.assertTrue(self.ar._is_match('zZ'))
        self.assertTrue(self.ar._is_match('Zz'))

    def test_can_react(self):
        self.assertEqual('dabCBAcaDA', self.ar._react('dabAcCaCBAcCcaDA'))

    def test_run_react_polymer(self):
        print(len(AlchemicalReduction('../resources/aoc5.txt').react_polymer()))
