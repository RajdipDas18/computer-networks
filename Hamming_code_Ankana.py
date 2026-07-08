"""
Hamming Code Generator and Error Detector

This program:
1. Generates a Hamming code for a given binary data string.
2. Detects a single-bit error in a received Hamming code.
"""

def calculate_parity_bits(data_length):
    """Return the number of parity bits required."""
    parity_bits = 0
    while (2 ** parity_bits) < (data_length + parity_bits + 1):
        parity_bits += 1
    return parity_bits


def insert_parity_bits(data, parity_bits):
    """Insert placeholder parity bits into the data."""
    result = []
    data_index = 0

    for position in range(1, len(data) + parity_bits + 1):
        if position & (position - 1) == 0:  # Power of 2
            result.append("0")
        else:
            result.append(data[data_index])
            data_index += 1

    return "".join(result)


def generate_hamming_code(code, parity_bits):
    """Calculate and set parity bits."""
    code = list(code)

    for i in range(parity_bits):
        parity_position = 2 ** i
        parity = 0

        for position in range(1, len(code) + 1):
            if position & parity_position:
                parity ^= int(code[position - 1])

        code[parity_position - 1] = str(parity)

    return "".join(code)


def detect_error(received_code, parity_bits):
    """Return the position of a single-bit error (0 if no error)."""
    error_position = 0

    for i in range(parity_bits):
        parity_position = 2 ** i
        parity = 0

        for position in range(1, len(received_code) + 1):
            if position & parity_position:
                parity ^= int(received_code[position - 1])

        error_position += parity * parity_position

    return error_position


def flip_bit(binary_string, position):
    """Correct the erroneous bit."""
    bits = list(binary_string)
    index = position - 1
    bits[index] = "1" if bits[index] == "0" else "0"
    return "".join(bits)


def is_binary(binary_string):
    """Check whether the input contains only 0s and 1s."""
    return all(bit in "01" for bit in binary_string)


def main():
    data = input("Enter binary data: ").strip()

    if not is_binary(data):
        print("Error: Please enter only binary digits (0 and 1).")
        return

    parity_bits = calculate_parity_bits(len(data))
    hamming_code = insert_parity_bits(data, parity_bits)
    hamming_code = generate_hamming_code(hamming_code, parity_bits)

    print("Generated Hamming Code:", hamming_code)

    received = input("Enter received Hamming code: ").strip()

    if not is_binary(received):
        print("Error: Please enter only binary digits (0 and 1).")
        return

    if len(received) != len(hamming_code):
        print("Error: Received code length does not match the generated Hamming code.")
        return

    error_position = detect_error(received, parity_bits)

    if error_position == 0:
        print("No error detected.")
    else:
        print(f"Error detected at position: {error_position}")
        corrected_code = flip_bit(received, error_position)
        print("Corrected Code:", corrected_code)


if __name__ == "__main__":
    main()