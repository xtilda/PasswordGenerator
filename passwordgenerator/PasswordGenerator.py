import random
import string

class PasswordGenerator:
    def __init__(self, length=12, complexity=3):
        self.length = length
        self.complexity = complexity

    def generate_password(self):
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        pool = ''
        if self.complexity >= 1:
            pool += lowercase
        if self.complexity >= 2:
            pool += uppercase
        if self.complexity >= 3:
            pool += digits
        if self.complexity >= 4:
            pool += symbols

        # Generate pasword
        password = ''.join(random.choices(pool, k=self.length))
        return password

    def set_length(self, length):
        self.length = length

    def set_complexity(self, complexity):
        self.complexity = complexity

def main():
    print("Welcome to the Password Generator!")
    print("-----------------------------------------")

    length = int(input("Enter the length of the password: "))
    complexity = int(input("Enter the complexity level (1-4): "))

    generator = PasswordGenerator(length, complexity)
    password = generator.generate_password()

    print("\nYour generated password is:")
    print(password)

if __name__ == "__main__":
    main()
