import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    def test_valid_visa(self):
        """Verifies a valid Visa card returns True.
        Selected using Partition Testing: valid prefix (4), valid length (16),
        and valid checksum.
        """
        self.assertTrue(credit_card_validator("4000000000000002"))

    def test_valid_mastercard_51(self):
        """Verifies a valid MasterCard with prefix 51 returns True.
        Selected using Boundary Value Testing at the lower bound of 51–55.
        """
        self.assertTrue(credit_card_validator("5100000000000008"))

    def test_valid_mastercard_55(self):
        """Verifies a valid MasterCard with prefix 55 returns True.
        Selected using Boundary Value Testing at the upper bound of 51–55.
        """
        self.assertTrue(credit_card_validator("5500000000000004"))

    def test_valid_mastercard_2221(self):
        """Verifies a valid MasterCard with prefix 2221 returns True.
        Selected using Boundary Value Testing at the lower bound of 2221–2720.
        """
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_valid_mastercard_2720(self):
        """Verifies a valid MasterCard with prefix 2720 returns True.
        Selected using Boundary Value Testing at the upper bound of 2221–2720.
        """
        self.assertTrue(credit_card_validator("2720000000000005"))

    def test_valid_amex_34(self):
        """Verifies a valid American Express card with prefix 34 returns True.
        Selected using Partition Testing: valid AmEx prefix and correct length (15).
        """
        self.assertTrue(credit_card_validator("340000000000009"))

    def test_valid_amex_37(self):
        """Verifies a valid American Express card with prefix 37 returns True.
        Selected using Partition Testing: second valid AmEx prefix and correct length (15).
        """
        self.assertTrue(credit_card_validator("370000000000002"))

    def test_invalid_visa_bad_checksum(self):
        """Verifies a Visa card with correct prefix and length but invalid checksum returns False.
        Selected using Partition Testing to isolate checksum validation.
        """
        self.assertFalse(credit_card_validator("4000000000000003"))

    def test_invalid_amex_bad_checksum(self):
        """Verifies an AmEx card with correct prefix and length but invalid checksum returns False.
        Selected using Partition Testing to isolate checksum validation.
        """
        self.assertFalse(credit_card_validator("340000000000008"))

    def test_invalid_prefix(self):
        """Verifies a card with an unsupported prefix returns False.
        Selected using Partition Testing for invalid issuer category.
        """
        self.assertFalse(credit_card_validator("6011111111111117"))

    def test_invalid_visa_short_length(self):
        """Verifies a Visa card shorter than 16 digits returns False.
        Selected using Boundary Value Testing just below valid length.
        """
        self.assertFalse(credit_card_validator("400000000000002"))

    def test_invalid_visa_long_length(self):
        """Verifies a Visa card longer than 16 digits returns False.
        Selected using Boundary Value Testing just above valid length.
        """
        self.assertFalse(credit_card_validator("40000000000000022"))

    def test_invalid_amex_short_length(self):
        """Verifies an AmEx card shorter than 15 digits returns False.
        Selected using Boundary Value Testing just below valid length.
        """
        self.assertFalse(credit_card_validator("34000000000000"))

    def test_invalid_amex_long_length(self):
        """Verifies an AmEx card longer than 15 digits returns False.
        Selected using Boundary Value Testing just above valid length.
        """
        self.assertFalse(credit_card_validator("3400000000000000"))

    def test_mastercard_prefix_50(self):
        """Verifies prefix 50 is rejected for MasterCard.
        Selected using Boundary Value Testing below valid prefix range.
        """
        self.assertFalse(credit_card_validator("5000000000000009"))

    def test_mastercard_prefix_56(self):
        """Verifies prefix 56 is rejected for MasterCard.
        Selected using Boundary Value Testing above valid prefix range.
        """
        self.assertFalse(credit_card_validator("5600000000000007"))

    def test_mastercard_prefix_2220(self):
        """Verifies prefix 2220 is rejected.
        Selected using Boundary Value Testing below new MasterCard range.
        """
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test_mastercard_prefix_2721(self):
        """Verifies prefix 2721 is rejected.
        Selected using Boundary Value Testing above new MasterCard range.
        """
        self.assertFalse(credit_card_validator("2721000000000003"))

    def test_empty_string(self):
        """Verifies empty string returns False.
        Selected using Error Guessing for extreme invalid input.
        """
        self.assertFalse(credit_card_validator(""))

    def test_single_digit(self):
        """Verifies a single-digit input returns False.
        Selected using Error Guessing for minimal input size.
        """
        self.assertFalse(credit_card_validator("4"))

    def test_all_zeroes(self):
        """Verifies all-zero input returns False.
        Selected using Error Guessing for repeated digit edge case.
        """
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test_valid_prefix_wrong_length_and_checksum(self):
        """Verifies valid prefix but incorrect length and checksum returns False.
        Selected using Error Guessing combining multiple invalid properties.
        """
        self.assertFalse(credit_card_validator("411111111111111"))

    def test_amex_prefix_37_wrong_length(self):
        """Verifies valid AmEx prefix with incorrect length returns False.
        Selected using Partition Testing across issuer-specific length rules.
        """
        self.assertFalse(credit_card_validator("3700000000000002"))

    def test_prefix_2221_wrong_length(self):
        """Verifies MasterCard prefix 2221 with incorrect length returns False.
        Selected using Boundary Testing on prefix-length mismatch.
        """
        self.assertFalse(credit_card_validator("222100000000000"))

    def test_prefix_4_wrong_length(self):
        """Verifies Visa prefix with incorrect length returns False.
        Selected using Partition Testing for prefix-length mismatch.
        """
        self.assertFalse(credit_card_validator("400000000000000"))

    def test_amex_bad_checksum_variant(self):
        """Verifies AmEx prefix with alternate invalid checksum returns False.
        Selected using Error Guessing to test checksum variation.
        """
        self.assertFalse(credit_card_validator("370000000000001"))

    def test_mastercard_wrong_length_and_checksum(self):
        """Verifies MasterCard with invalid length and checksum returns False.
        Selected using Error Guessing combining multiple invalid conditions.
        """
        self.assertFalse(credit_card_validator("51000000000000"))

    def test_mastercard_2221_length_15(self):
        """Verifies MasterCard prefix 2221 with incorrect length returns False.
        Selected using Boundary Testing across issuer-specific constraints.
        """
        self.assertFalse(credit_card_validator("222100000000000"))

    def test_invalid_amex_wrong_prefix_3x(self):
        """Verifies that numbers starting with 3 but not 34 or 37 are invalid.
        Selected using Partition Testing to ensure only valid AmEx prefixes (34, 37)
        are accepted and all other 3x prefixes are rejected.
        """
        self.assertFalse(credit_card_validator("3100000000000005"))

    def test_invalid_amex_prefix_38(self):
        """Verifies that prefix 38 is not a valid AmEx prefix.
        Selected using Boundary Testing around valid AmEx prefixes (34 and 37).
        """
        self.assertFalse(credit_card_validator("3800000000000000"))

    def test_visa_length_10(self):
        """Verifies extremely short Visa-like number returns False.
        Selected using Boundary Testing far below valid length.
        """
        self.assertFalse(credit_card_validator("4000000000"))

    def test_mastercard_prefix_only(self):
        """Verifies prefix-only input fails validation.
        Selected using Error Guessing for incomplete input.
        """
        self.assertFalse(credit_card_validator("51"))

    def test_amex_prefix_only(self):
        """Verifies AmEx prefix-only input fails validation.
        Selected using Error Guessing for incomplete input.
        """
        self.assertFalse(credit_card_validator("34"))


if __name__ == "__main__":
    unittest.main()
