def generate_greeting(role: str) -> str:
    return f"Hello, {role}!"

if __name__ == "__main__":
    print(generate_greeting("Admin"))
    print(generate_greeting("User"))
