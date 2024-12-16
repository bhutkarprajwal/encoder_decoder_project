def decode(data):
    def parse(data, index):
        marker = data[index]

        if marker == 0x00:
            return None, index + 1

        elif marker == 0x03:
            length = data[index + 1]
            start = index + 2
            return data[start:start + length], start + length

        elif marker == 0x07:
            start = index + 1
            value = int.from_bytes(data[start:start + 2], byteorder='little')
            return value, start + 2

        elif marker == 0x04:
            length = data[index + 1]
            index += 2
            result = []
            for _ in range(length):
                item, index = parse(data, index)
                result.append(item)
            return result, index

        elif marker < 0x04:
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
