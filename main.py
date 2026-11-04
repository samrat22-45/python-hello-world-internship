"""
Fundamentals and Setup - Python Development Internship
A simple Hello World program.
"""

def main():
    name = input("Enter your name: ").strip()
    if not name:
        name = "Intern"
    print(f"Hello, {name}! My Python environment is working correctly.")

if __name__ == "__main__":
    main()
