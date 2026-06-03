# Changes in line num 4,5,6 Complete rewrite of xor() – Fixed critical bug and made it efficient using zip and generator expression.
# Changes in line num 8 to 25 Major rewrite of mod2div() – Used list instead of string concatenation, removed redundant XOR with zeros, better loop structure.

def xor(a: str, b: str) -> str:
    """XOR two binary strings of equal length"""
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

def mod2div(dividend: str, divisor: str) -> str:
    """Perform modulo-2 division and return remainder"""
    divisor_len = len(divisor)
    temp = list(dividend[:divisor_len])  # Use list for mutability

    for i in range(divisor_len, len(dividend)):
        if temp[0] == '1':
            temp = list(xor(''.join(temp), divisor))
        else:
            temp = temp[1:]  # Just shift (no need to XOR with 0s)      
        temp.append(dividend[i])

    # Final remainder
    if temp[0] == '1':
        temp = list(xor(''.join(temp), divisor))
    else:
        temp = temp[1:]
    return ''.join(temp)

def encode_crc(data: str, generator: str):
    """Generate CRC remainder and codeword"""
    n = len(generator) - 1
    appended_data = data + '0' * n
    remainder = mod2div(appended_data, generator)
    codeword = data + remainder
    return remainder, codeword

def decode_crc(codeword: str, generator: str) -> bool:
    """Check if received codeword is valid"""
    remainder = mod2div(codeword, generator)
    return '1' not in remainder
    
print("----- CRC CHECKSUM PROGRAM -----")

data = input("Enter data bits: ").strip()
generator = input("Enter generator bits: ").strip()
remainder, codeword = encode_crc(data, generator)

print("\nSender Side")
print("CRC Remainder :", remainder)
print("Codeword      :", codeword)
print("\nReceiver Side (Original)")
print("No Error Detected" if decode_crc(codeword, generator) else "Error Detected")

# Test with error
corrupted = codeword[:-1] + ('1' if codeword[-1] == '0' else '0')
print("\nCorrupted Codeword :", corrupted)
print("No Error Detected" if decode_crc(corrupted, generator) else "Error Detected")
