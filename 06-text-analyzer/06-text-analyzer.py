"""
Day 05 (Project 06): Text Analyzer & Word Counter
Analyzes text input for character counts, word counts, and word frequency.
"""

def analyze_text():
    print("=" * 45)
    print("📊 TEXT ANALYZER & WORD COUNTER 📊")
    print("=" * 45)
    
    text = input("Please enter or paste your sentence/paragraph:\n\n").strip()
    
    if not text:
        print("\n⚠️ No text entered! Exiting program.")
        return

    # Process text
    words = text.lower().split()
    total_chars_with_spaces = len(text)
    total_chars_no_spaces = len(text.replace(" ", ""))
    total_words = len(words)

    # Word Frequency Dictionary
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Most frequent word
    most_common = max(frequency, key=frequency.get)
    highest_count = frequency[most_common]

    # Print Report
    print("\n" + "-" * 35)
    print("📈 ANALYSIS REPORT")
    print("-" * 35)
    print(f"🔤 Total Characters (with spaces)   : {total_chars_with_spaces}")
    print(f"🔤 Total Characters (without spaces): {total_chars_no_spaces}")
    print(f"📝 Total Words                      : {total_words}")
    print(f"🔥 Most Frequent Word              : '{most_common}' ({highest_count} times)")
    print("-" * 35)

if __name__ == "__main__":
    analyze_text()