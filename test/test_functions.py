from public_search.functions import get_company_details
from data.companies import btw_nr
import unittest
import sys

sys.path.append("../functions")


class TestSum(unittest.TestCase):
    mock_btw_nr = "BTW BE 0123 456 789"
    street = "Distellaan"
    postcode = "8400"

    def test_get_company_details(self):
        company_details = get_company_details(self.mock_btw_nr)
        self.assertEqual(
            company_details['address']['street'], self.street, f"Should be {self.street}")
        self.assertEqual(
            company_details['address']['postcode'], self.postcode, f"Should be {self.postcode}")

        if __name__ == "__main__":
            unittest.main()
