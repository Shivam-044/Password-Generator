import secrets
import string

def generate_secure_password(length=16):
    """
    Generates a cryptographically secure random password.
    Ensures at least one uppercase, lowercase, digit, and special character.
    """
    if length < 8:
        return "Error: Password length should be at least 8 characters for security."

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    all_chars = lower + upper + digits + symbols

    while True:
        # Generate password using secrets (Cryptographically Secure)
        password = ''.join(secrets.choice(all_chars) for _ in range(length))
        
        # Validation: Ensure it meets security standards
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in symbols for c in password)

        if has_upper and has_lower and has_digit and has_symbol:
            return password

# --- User Interaction ---
if __name__ == "__main__":
    print("--- 🔐 Cryptographic Password Generator ---")
    try:
        user_length = int(input("Enter desired password length (default 16): ") or 16)
        secure_pass = generate_secure_password(user_length)
        
        print("\n" + "="*30)
        print(f"Your Secure Password: \n{secure_pass}")
        print("="*30)
        print("✅ This password is cryptographically secure.")
    except ValueError:
        print("❌ Please enter a valid number for the length.")
