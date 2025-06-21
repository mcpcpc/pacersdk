from time import sleep
from unittest import main, TestCase

from pacersdk.otp import hotp, totp


class TestOTP(TestCase):
    def setUp(self):
        # Secret from RFC 4226 Appendix D
        self.secret = "JBSWY3DPEHPK3PXP"  # Base32 for 'Hello!\xde\xad\xbe\xef'

    def test_hotp_length(self):
        token = hotp(self.secret, counter=1, digits=6)
        self.assertEqual(len(token), 6)
        self.assertTrue(token.isdigit())

    def test_totp_stability_within_interval(self):
        token1 = totp(self.secret, time_step=30, digits=6)
        sleep(1)
        token2 = totp(self.secret, time_step=30, digits=6)
        self.assertEqual(token1, token2)

    def test_totp_change_after_interval(self):
        token1 = totp(self.secret, time_step=1, digits=6)
        sleep(2)
        token2 = totp(self.secret, time_step=1, digits=6)
        self.assertNotEqual(token1, token2)


if __name__ == "__main__":
    main()
