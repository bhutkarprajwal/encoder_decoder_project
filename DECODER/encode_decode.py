def encode(data):
    result = []

    if data is None:  # Null value
        result.append(0x00)

    elif isinstance(data, bytes):  # Byte sequence
        result.append(0x03)  # Marker for bytes
        result.append(len(data))  # Length of byte sequence
        result.extend(data)

    elif isinstance(data, int):  # Integer
        result.append(0x07)  # Marker for integer
        result.extend(data.to_bytes(2, byteorder='little'))

    elif isinstance(data, list):  # List
        result.append(0x04)  # Marker for list
        result.append(len(data))  # Number of items
        for item in data:
            result.extend(encode(item))  # Recursively encode each item

    elif isinstance(data, dict):  # Dictionary
        result.append(len(data))  # Number of key-value pairs
        for key, value in data.items():
            key_bytes = key.encode('utf-8')
            result.append(len(key_bytes))  # Length of the key
            result.extend(key_bytes)  # UTF-8 encoded key
            result.extend(encode(value))  # Recursively encode the value

    else:
        raise TypeError(f"Unsupported data type: {type(data)}")

    return result


def decode(data):
    def parse(data, index):
        marker = data[index]

        if marker == 0x00:  # Null value
            return None, index + 1

        elif marker == 0x03:  # Byte sequence
            length = data[index + 1]
            start = index + 2
            return bytes(data[start:start + length]), start + length

        elif marker == 0x07:  # Integer
            start = index + 1
            value = int.from_bytes(data[start:start + 2], byteorder='little')
            return value, start + 2

        elif marker == 0x04:  # List
            length = data[index + 1]
            index += 2
            result = []
            for _ in range(length):
                item, index = parse(data, index)
                result.append(item)
            return result, index

        elif marker < 0x04:  # Dictionary
            num_items = marker
            result = {}
            index += 1
            for _ in range(num_items):
                key_length = data[index]
                key = data[index + 1: index + key_length + 1].decode('utf-8')
                index += key_length + 1
                value, index = parse(data, index)
                result[key] = value
            return result, index

        else:
            raise ValueError(f"Unsupported marker: {marker}")

    parsed, _ = parse(data, 0)
    return parsed
