#! /usr/bin/python

""" Unit tests for compute_highest_affinity.py"""

from unittest import TestCase
import app.compute_highest_affinity as auth

class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""

    def test(self):
        site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com", "c.com", "c.com"]
        user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie", "bob", "ted"]
        computed_result = auth.highest_affinity(site_list, user_list)
        expected_result = ("a.com", "b.com")

	self.assertEqual(computed_result, expected_result)
        #assert computed_result == expected_result











