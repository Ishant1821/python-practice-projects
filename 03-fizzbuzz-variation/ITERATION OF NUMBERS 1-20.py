"""
Day 03: Word Replacement Game (FizzBuzz Variation)
Prints numbers 1 to 20, replacing multiples of 4 with 'HI', 
multiples of 5 with 'HELLO', and multiples of both with 'HOW ARE YOU'.
"""

def word_replacement_game(limit=20):
    print(f"--- Running Word Replacement Game (1 to {limit}) ---\n")
    
    for num in range(1, limit + 1):
        if num % 4 == 0 and num % 5 == 0:
            print(f"{num:2d} --> HOW ARE YOU")
        elif num % 4 == 0:
            print(f"{num:2d} --> HI")
        elif num % 5 == 0:
            print(f"{num:2d} --> HELLO")
        else:
            print(f"{num:2d} --> {num}")

if __name__ == "__main__":
    word_replacement_game()