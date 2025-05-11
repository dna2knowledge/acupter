import base64

def split_base64_string(b64_string, line_length=100):
    """
    Splits a Base64 string into lines of specified length (default: 100 chars).

    :param b64_string: The Base64 encoded string.
    :param line_length: Number of characters per line.
    :return: A string with newlines inserted every `line_length` characters.
    """
    return '\n'.join(
        b64_string[i:i + line_length] for i in range(0, len(b64_string), line_length)
    )

def encode_file_to_base64(input_file, output_file=None):
    """
    Encodes the content of a binary file into a Base64 string.
    
    :param input_file: Path to the input binary file.
    :param output_file: (Optional) Path to save the Base64 string. If None, returns as string.
    :return: Base64 encoded string (if no output file is provided)
    """
    try:
        with open(input_file, "rb") as bin_file:
            encoded_str = base64.b64encode(bin_file.read()).decode("utf-8")

        if output_file:
            with open(output_file, "w") as out_file:
                out_file.write(split_base64_string(encoded_str, 80))
            print(f"[+] File encoded and saved to {output_file}")
        else:
            return encoded_str
    except Exception as e:
        print(f"[-] Error encoding file: {e}")


def decode_base64_to_file(input_file, output_file):
    """
    Decodes a Base64 string back into its original binary form.
    
    :param input_string: The Base64 encoded string or path to file containing it.
    :param output_file: Path to save the decoded binary file.
    """
    try:
        # Check if input_string is a file path
        try:
            with open(input_file, "r") as f:
                encoded_data = ''.join(f.read().strip().split('\n'))
        except FileNotFoundError:
            encoded_data = input_string.strip()

        decoded_data = base64.b64decode(encoded_data)

        with open(output_file, "wb") as bin_file:
            bin_file.write(decoded_data)
        
        print(f"[+] File successfully decoded and saved to {output_file}")

    except Exception as e:
        print(f"[-] Error decoding data: {e}")


# Example usage:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Base64 Encode/Decode Files")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encoder parser
    encode_parser = subparsers.add_parser("encode", help="Encode a file to Base64 string")
    encode_parser.add_argument("-i", "--input", required=True, help="Input binary file")
    encode_parser.add_argument("-o", "--output", help="Output file to store Base64 string")

    # Decoder parser
    decode_parser = subparsers.add_parser("decode", help="Decode Base64 string to file")
    decode_parser.add_argument("-i", "--input", required=True, help="Base64 string or file containing it")
    decode_parser.add_argument("-o", "--output", required=True, help="Output binary file")

    args = parser.parse_args()

    if args.command == "encode":
        encode_file_to_base64(args.input, args.output)
    elif args.command == "decode":
        decode_base64_to_file(args.input, args.output)
