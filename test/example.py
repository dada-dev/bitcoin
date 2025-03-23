import re

def is_valid_btc_address(address):
    """
    Validates a Bitcoin address using a simple regex pattern.
    Note: This is a basic check and does not guarantee full validity.
    """
    btc_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
    return bool(btc_pattern.match(address))

# Example usage
if __name__ == "__main__":
    test_addresses = [
        "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",  # Valid
        "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",  # Valid
        "bc1qw508d6qejxtdg4y5r3zarvaryv5gheyzcc7g9x",  # Valid
        "invalidBTCaddress123",  # Invalid
    ]

    for address in test_addresses:
        print(f"{address}: {'Valid' if is_valid_btc_address(address) else 'Invalid'}")

