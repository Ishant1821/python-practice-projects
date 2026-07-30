"""
Python Loop Control Statements Demonstration
Covers: break, continue, pass, and while-loop control.
"""

def demonstrate_break():
    print("--- 1. BREAK STATEMENT (Exits loop completely) ---")
    for i in range(5):
        if i == 3:
            print("  --> Encountred 3, breaking out of loop!")
            break
        print(f"  Current value: {i}")


def demonstrate_continue():
    print("\n--- 2. CONTINUE STATEMENT (Skips current iteration) ---")
    for i in range(5):
        if i == 2:
            print("  --> Skipping value 2")
            continue
        print(f"  Current value: {i}")


def demonstrate_pass():
    print("\n--- 3. PASS STATEMENT (Syntactic placeholder) ---")
    for i in range(3):
        if i == 1:
            # 'pass' allows code to run without syntax errors where a body is required
            pass 
        else:
            print(f"  Current value: {i}")


def demonstrate_interactive_while():
    print("\n--- 4. WHILE LOOP WITH BREAK (Interactive) ---")
    print("Type anything to test the loop. Type 'stop' or 'exit' to break out.")
    
    while True:
        user_input = input("Enter command --> ").strip().lower()
        if user_input in ["stop", "exit"]:
            print("  --> Break command received. Exiting loop!")
            break
        print(f"  Loop active. You typed: '{user_input}'")


if __name__ == "__main__":
    demonstrate_break()
    demonstrate_continue()
    demonstrate_pass()
    demonstrate_interactive_while()