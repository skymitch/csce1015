
print("Skylar Mitchell Modified This Credit Card Validator")

def is_credit_card_valid(card_number):
    # Check if the card number is not 16 digits long or contains non-digit characters
    if len(card_number) != 16 or not card_number.isdigit():
        return False
    if card_number == "0000000000000000":  # Reject all-zero card numbers
        return False
        
    total = 0
    reverse_digits = card_number[::-1]  # Reverse the card number for processing
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2:
            n *= 2
            if n > 9:  
                n -= 9
        total += n
    return total % 10 == 0  # Return True if the total modulo 10 is 0

# Get the card number from the user
card_number = input("Enter your 16-digit credit card number: ")

# Validate the card number
if is_credit_card_valid(card_number):     
    print("Card is valid.")
else:
    print("Invalid card number. It must be 16 digits long and pass the Luhn check.")

# Test the Luhn algorithm function
def run_tests():
    assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'
    assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'
    assert not is_credit_card_valid("134"), '134 should not pass but did'
    assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'
    assert not is_credit_card_valid("0000000000000000"), 'This is a bad test and we will get an error message'

# Run the tests
run_tests()



