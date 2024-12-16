import unittest
from encoder_decoder.encoder import encode
from encoder_decoder.decoder import decode

class TestEncoderDecoder(unittest.TestCase):

    def test_null_encoding_decoding(self):
        data = {"key": None}
        encoded_data = encode(data)
        decoded_data = decode(encoded_data)
        self.assertEqual(decoded_data, data, "Null encoding/decoding failed.")

    def test_integer_encoding_decoding(self):
        data = {"integer": 12345}
        encoded_data = encode(data)
        decoded_data = decode(encoded_data)
        self.assertEqual(decoded_data, data, "Integer encoding/decoding failed.")

    def test_bytes_encoding_decoding(self):
        data = {"octets": bytes([10, 20, 30])}
        encoded_data = encode(data)
        decoded_data = decode(encoded_data)
        self.assertEqual(decoded_data, data, "Bytes encoding/decoding failed.")

    def test_nested_dictionary_encoding_decoding(self):
        nested_data = {
            "user": {
                "name": "Alice",
                "age": 30,
                "preferences": [1, 2, 3]
            }
        }
        encoded_data = encode(nested_data)
        decoded_data = decode(encoded_data)
        self.assertEqual(decoded_data, nested_data, "Nested dictionary encoding/decoding failed.")

    def test_unsupported_data_type(self):
        data = {"unsupported": "string"}
        with self.assertRaises(TypeError):
            encode(data)

if __name__ == "__main__":
    unittest.main()
