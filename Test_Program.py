import unittest
from unittest.mock import patch, mock_open
from AtkinsAProjectMod6 import validate_file, encrypt, decrypt

class TestEncryptionProgram(unittest.TestCase):
    # Test validate_file function
    def test_validate_file(self):
        self.assertRaises(FileNotFoundError, validate_file, "nonexistent.txt")
        with open("existing_file.txt", "w") as f:  # Create a temporary test file
            f.write("test content")
        self.assertEqual(validate_file("existing_file.txt"), "existing_file.txt")

    # Test encryption
    @patch("builtins.open", new_callable=mock_open, read_data="test data")
    @patch("builtins.input", side_effect=["test_file.txt", "output_file.txt"])
    def test_encrypt(self, mock_input, mock_open_func):
        output_file = encrypt()
        self.assertEqual(output_file, "output_file.txt")

    # Test decryption with valid data
    @patch("builtins.open", new_callable=mock_open, read_data="116.115.114.")
    @patch("builtins.input", side_effect=["encrypted_file.txt", "decrypted_file.txt"])
    def test_decrypt_valid(self, mock_input, mock_open_func):
        output_file = decrypt()
        self.assertEqual(output_file, "decrypted_file.txt")

    # Test decryption with invalid data
    @patch("builtins.open", new_callable=mock_open, read_data="abc.def.")
    @patch("builtins.input", side_effect=["encrypted_file.txt", "decrypted_file.txt"])
    def test_decrypt_invalid(self, mock_input, mock_open_func):
        with self.assertLogs() as log:
            decrypt()
            self.assertIn("Invalid number in encrypted file: 'abc'", log.output[0])

if __name__ == "__main__":
    unittest.main()
