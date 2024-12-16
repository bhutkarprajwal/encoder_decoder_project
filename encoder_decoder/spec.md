
---

### 6️⃣ **`SPEC.md`**

```markdown
# SPEC.md

## Data Serialization Specification

### Supported Data Types
- **Null**: Encoded as a single byte `0x00`.
- **Bytes (octets)**: Length-prefixed encoding.
- **Integer**: Encoded in 2-byte little-endian format.
- **List**: Prefixed with a marker `0x04` and a length byte.
- **Dictionary**: Encoded with key-value pairs in UTF-8 and prefixed by the number of key-value pairs.

### Encoding Rules
- All data types are recursively encoded.
- Dictionaries must maintain the key order.

### Test Vectors
1. **Test Vector 1**: Basic types (null, octets, integer).
2. **Test Vector 2**: Nested dictionaries.
3. **Test Vector 3**: Large integers up to 2^64-1.

---

## Error Handling
- Unsupported data types raise a `TypeError`.
- Malformed markers result in a `ValueError`.

