import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    # ------------------------------------------------------------------
    # Express service
    # ------------------------------------------------------------------
    def test_express_local(self):
        # standard local for 2 kg = 8.0; express adds 7.0 → 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional for 2 kg = 11.0; express adds 7.0 → 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # local: 5.0 + 1.5*1.5 + 7.0 = 14.25
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    def test_express_regional_fractional_weight(self):
        # regional: 8.0 + 1.5*3.0 + 7.0 = 19.5
        self.assertEqual(shipping_quote(3.0, "regional", service="express"), 19.5)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_unknown_service_raises(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")

    def test_unknown_zone_raises(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_zero_weight_raises(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local", service="express")

    def test_negative_weight_raises(self):
        with self.assertRaises(ValueError):
            shipping_quote(-1, "regional", service="express")
