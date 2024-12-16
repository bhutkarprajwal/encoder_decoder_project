from encode_decode import encode, decode  # Ensure encode_decode.py has encode and decode functions.

def test_vector_1():
    input_data = {
        "null": None,
        "octets": bytes([1, 2, 3]),
        "integer": 12345
    }

    # Expected encoded output
    expected = [
        0x03,  # Number of key-value pairs in dictionary
        0x04, 0x6E, 0x75, 0x6C, 0x6C,  # Key "null"
        0x00,  # Null marker
        0x06, 0x6F, 0x63, 0x74, 0x65, 0x74, 0x73,  # Key: "octets"
        0x03, 0x01, 0x02, 0x03,  # Length-prefixed byte sequence
        0x07, 0x69, 0x6E, 0x74, 0x65, 0x67,0x65,
        0x39, 0x30  # Integer 12345 in Little Endian format
    ]

    # Encode the input data
    encoded_data = encode(input_data)

    # Check if encoding matches the expected output
    assert encoded_data == expected, f"Encode failed: {encoded_data} != {expected}"

    # Decode back to original data
    decoded_data = decode(encoded_data)

    # Check if decoding matches the input data
    assert decoded_data == input_data, f"Decode failed: {decoded_data} != {input_data}"

    print("All test cases passed successfully!")

# Run the test
test_vector_1()
