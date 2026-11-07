import random

def generate_otp(length):
    """Generate a random OTP (One-Time Password) of specified length."""
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    otp = ''.join(random.choices('0123456789', k=length))
    return otp

otp = generate_otp(int(input("Enter the length of the OTP: ")))
print(f"Generated OTP: {otp}")