import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    def test_valid_visa(self):
        """Verifies a valid Visa card returns True.
        Picked using Partition Testing: valid prefix, valid length, valid checksum.
        """
        self.assertTrue(credit_card_validator("4000000000000002"))

    def test_valid_mastercard_lower_old_range(self):
        """Verifies a valid MasterCard in the lower old prefix range returns True.
        Picked using Boundary Value Testing at the lower boundary of 51 through 55.
        """
        self.assertTrue(credit_card_validator("5100000000000008"))

    def test_valid_mastercard_upper_old_range(self):
        """Verifies a valid MasterCard in the upper old prefix range returns True.
        Picked using Boundary Value Testing at the upper boundary of 51 through 55.
        """
        self.assertTrue(credit_card_validator("5500000000000004"))

    def test_valid_mastercard_lower_new_range(self):
        """Verifies a valid MasterCard in the lower new prefix range returns True.
        Picked using Boundary Value Testing at the lower boundary of 2221 through 2720.
        """
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_valid_mastercard_upper_new_range(self):
        """Verifies a valid MasterCard in the upper new prefix range returns True.
        Picked using Boundary Value Testing at the upper boundary of 2720.
        """
        self.assertTrue(credit_card_validator("2720000000000005"))

    def test_valid_amex_34(self):
        """Verifies a valid American Express card with prefix 34 returns True.
        Picked using Partition Testing for a valid AmEx partition.
        """
        self.assertTrue(credit_card_validator("340000000000009"))

    def test_valid_amex_37(self):
        """Verifies a valid American Express card with prefix 37 returns True.
        Picked using Boundary/Partition Testing for the second valid AmEx prefix.
        """
        self.assertTrue(credit_card_validator("370000000000002"))

    def test_invalid_visa_bad_checksum(self):
        """Verifies a Visa with correct prefix and length but invalid checksum returns False.
        Picked using Partition Testing: invalid check digit only.
        """
        self.assertFalse(credit_card_validator("4000000000000003"))

    def test_invalid_amex_bad_checksum(self):
        """Verifies an AmEx with correct prefix and length but invalid checksum returns False.
        Picked using Partition Testing: isolate checksum failure in AmEx partition.
        """
        self.assertFalse(credit_card_validator("340000000000008"))

    def test_invalid_prefix_discover(self):
        """Verifies a card with an unsupported prefix returns False.
        Picked using Partition Testing: invalid issuer prefix.
        """
        self.assertFalse(credit_card_validator("6011111111111117"))

    def test_invalid_visa_short_length(self):
        """Verifies a Visa with length 15 instead of 16 returns False.
        Picked using Boundary Value Testing just below the valid Visa length.
        """
        self.assertFalse(credit_card_validator("400000000000002"))

    def test_invalid_visa_long_length(self):
        """Verifies a Visa with length 17 instead of 16 returns False.
        Picked using Boundary Value Testing just above the valid Visa length.
        """
        self.assertFalse(credit_card_validator("40000000000000022"))

    def test_invalid_amex_short_length(self):
        """Verifies an AmEx with length 14 instead of 15 returns False.
        Picked using Boundary Value Testing just below the valid AmEx length.
        """
        self.assertFalse(credit_card_validator("34000000000000"))

    def test_invalid_amex_long_length(self):
        """Verifies an AmEx with length 16 instead of 15 returns False.
        Picked using Boundary Value Testing just above the valid AmEx length.
        """
        self.assertFalse(credit_card_validator("3400000000000000"))

    def test_mastercard_prefix_below_old_range(self):
        """Verifies prefix 50 is rejected for MasterCard.
        Picked using Boundary Value Testing just below the valid 51 through 55 range.
        """
        self.assertFalse(credit_card_validator("5000000000000009"))

    def test_mastercard_prefix_above_old_range(self):
        """Verifies prefix 56 is rejected for MasterCard.
        Picked using Boundary Value Testing just above the valid 51 through 55 range.
        """
        self.assertFalse(credit_card_validator("5600000000000007"))

    def test_mastercard_prefix_below_new_range(self):
        """Verifies prefix 2220 is rejected for MasterCard.
        Picked using Boundary Value Testing just below the valid 2221 through 2720 range.
        """
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test_mastercard_prefix_above_new_range(self):
        """Verifies prefix 2721 is rejected for MasterCard.
        Picked using Boundary Value Testing just above the valid 2221 through 2720 range.
        """
        self.assertFalse(credit_card_validator("2721000000000003"))

    def test_empty_string(self):
        """Verifies an empty string returns False.
        Picked using Error Guessing for an extreme invalid input.
        """
        self.assertFalse(credit_card_validator(""))

    def test_single_digit(self):
        """Verifies a one-digit input returns False.
        Picked using Error Guessing for a minimal-length edge case.
        """
        self.assertFalse(credit_card_validator("4"))

    def test_all_zeroes_length_16(self):
        """Verifies a 16-digit string of all zeroes returns False.
        Picked using Error Guessing because repeated digits can expose logic mistakes.
        """
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test_valid_prefix_wrong_length_and_checksum(self):
        """Verifies a Visa with a valid prefix but multiple invalid properties returns False.
        Picked using Error Guessing to check robustness when prefix is valid
        but both length and checksum are wrong.
        """
        self.assertFalse(credit_card_validator("411111111111111"))

    def test_amex_prefix_37_wrong_length(self):
        """Verifies an AmEx with a valid prefix but Visa/MasterCard length returns False.
        Picked using Partition Testing across issuer-specific length requirements.
        """
        self.assertFalse(credit_card_validator("3700000000000002"))

    def test_prefix_2221_wrong_length(self):
        """Verifies a MasterCard prefix 2221 with incorrect length fails.
        Selected using Boundary Testing: valid prefix but invalid length.
        """
        self.assertFalse(credit_card_validator("222100000000000"))

    def test_prefix_4_wrong_length_15(self):
        """Verifies Visa prefix with length 15 fails.
        Selected using Partition Testing: valid prefix, invalid length.
        """
        self.assertFalse(credit_card_validator("400000000000000"))

    def test_amex_valid_prefix_bad_checksum_variant(self):
        """Verifies AmEx with correct prefix but different invalid checksum fails.
        Selected using Error Guessing to test alternative checksum failure.
        """
        self.assertFalse(credit_card_validator("370000000000001"))

    def test_mastercard_valid_range_wrong_length_and_checksum(self):
        """Verifies MasterCard in valid range but wrong length and checksum fails.
        Selected using Error Guessing combining multiple invalid properties.
        """
        self.assertFalse(credit_card_validator("51000000000000"))

    def test_mastercard_2221_length_15(self):
        """Verifies MasterCard prefix 2221 with length 15 fails.
        Selected using Boundary Testing across issuer-specific lengths.
        """
        self.assertFalse(credit_card_validator("222100000000000"))

    def test_empty_string_explicit(self):
        """Verifies empty string is invalid.
        Selected using Error Guessing for extreme invalid input.
        """
        self.assertFalse(credit_card_validator(""))

    def test_visa_valid_prefix_length_10(self):
        """Verifies Visa with very short length fails.
        Selected using Boundary Testing far below valid length.
        """
        self.assertFalse(credit_card_validator("4000000000"))

    def test_mastercard_prefix_only_valid(self):
        """Verifies MasterCard prefix without proper length fails.
        Selected using Error Guessing: prefix alone should not validate.
        """
        self.assertFalse(credit_card_validator("51"))

    def test_amex_prefix_only(self):
        """Verifies AmEx prefix alone fails.
        Selected using Error Guessing to ensure full validation is required.
        """
        self.assertFalse(credit_card_validator("34"))


if __name__ == "__main__":
    unittest.main()
