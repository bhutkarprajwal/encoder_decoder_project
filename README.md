
# Encoding and Decoding Functions

This project includes functions to encode and decode data structures efficiently.

## `encode(data)`
Encodes various data types into a byte array:
- `None` → Encoded as `0x00`
- `bytes` → Length-prefixed byte array
- `int` → Little-endian 2-byte representation
- `list` → Encoded with length and individual items
- `dict` → Encoded with key-value pairs

## `decode(data)`
Decodes a byte array into its original data structure using a marker-based format.

## Example Usage
```python
encoded_data = encode({"name": "Alice", "scores": [85, 90, 78]})
decoded_data = decode(encoded_data)
print(decoded_data)  # {'name': 'Alice', 'scores': [85, 90, 78]}
```


