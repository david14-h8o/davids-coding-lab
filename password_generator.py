import random
import string

def generate_password():
    # Define character sets
    letters = string.ascii_lowercase
    digits = string.digits
    
    # Function to generate a random chunk of letters + digits
    def random_chunk(length=5):
        return ''.join(random.choice(letters + digits) for _ in range(length))
    
    # Build password with chunks separated by dashes
    password = f"{random_chunk()}-{random_chunk()}-{random_chunk()}"
    return password

# Example usage
print("Your strong password:", generate_password())