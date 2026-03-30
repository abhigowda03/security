import re

def validate_password(password):
    """
    Validate password based on common security requirements.
    
    Requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    
    Returns:
        tuple: (is_valid: bool, messages: list)
    """
    messages = []
    is_valid = True
    
    # Check length
    if len(password) < 8:
        messages.append("❌ Password must be at least 8 characters long")
        is_valid = False
    else:
        messages.append("✓ Length requirement met")
    
    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        messages.append("❌ Password must contain at least one uppercase letter")
        is_valid = False
    else:
        messages.append("✓ Contains uppercase letter")
    
    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        messages.append("❌ Password must contain at least one lowercase letter")
        is_valid = False
    else:
        messages.append("✓ Contains lowercase letter")
    
    # Check for digit
    if not re.search(r'\d', password):
        messages.append("❌ Password must contain at least one digit")
        is_valid = False
    else:
        messages.append("✓ Contains digit")
    
    # Check for special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        messages.append("❌ Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>)")
        is_valid = False
    else:
        messages.append("✓ Contains special character")
    
    return is_valid, messages


def main():
    print("=== Password Validator ===\n")
    
    while True:
        password = input("Enter a password to validate (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        is_valid, messages = validate_password(password)
        
        print("\nValidation Results:")
        for message in messages:
            print(f"  {message}")
        
        if is_valid:
            print("\n✓ Password is VALID!\n")
        else:
            print("\n✗ Password is INVALID. Please try again.\n")
        
        print("-" * 50)


if __name__ == "__main__":
    main()
