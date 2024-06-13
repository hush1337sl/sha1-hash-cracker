# SHA1 Hash Cracker

This Python script attempts to brute-force a given SHA1 hash by generating all possible strings up to a specified maximum length using a defined character set. It prints each attempt and the corresponding hash until it finds a match or exhausts all possibilities.

## Features

- **Brute-force SHA1 hash**: Generates all possible strings of a given length and compares their SHA1 hash to the target.
- **Configurable character set**: By default, the character set includes all lowercase letters and digits.
- **Adjustable maximum length**: The maximum length of strings to attempt can be set as needed.
- **Clear console output**: The script clears the console before starting to keep the output clean.

## Usage

1. Clone the repository.
2. Run the script using Python.
3. Input the SHA1 hash you want to brute-force when prompted.

### Example

```bash
python sha1 bruteforcer.py
```

You will be prompted to enter the SHA1 hash you want to brute-force:

```plaintext
Enter the SHA1 HASH you want to Bruteforce:
```

The script will then attempt to find the original string by generating all possible combinations of characters up to the specified length.

## Requirements

This script uses only standard Python libraries, so no additional packages are required.

## Libraries Used

- `hashlib`: To generate SHA1 hashes.
- `itertools`: To create combinations of characters.
- `string`: To provide the default character set.
- `os`: To clear the console.

## Notes

- This script is for educational purposes only. Brute-forcing hashes without permission is illegal and unethical.
- The default character set and maximum length can be adjusted to suit your needs.
