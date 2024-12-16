def encode(data):
    result = []

    if data is None:
        result.append(0x00)

    elif isinstance(data, bytes):
        result.append(len(data))
        result.extend(data)

    elif isinstance(data, int):
        result.extend(data.to_bytes(2, byteorder='little'))

    elif isinstance(data, list):
        result.append(0x04)
        result.append(len(data))

        for idx, item in enumerate(data):
            result.extend(encode(item))

    elif isinstance(data, dict):
        num_items = len(data)
        result.append(num_items)

        for key, value in data.items():
            key_bytes = key.encode('utf-8')
            result.append(len(key_bytes))
            result.extend(key_bytes)
            result.extend(encode(value))

    else:
        raise TypeError(f"Unsupported data type: {type(data)}")

    return result
