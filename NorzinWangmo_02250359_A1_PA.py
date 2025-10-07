import urllib.request

# 1. Perfect Number Sum Calculator
def perfect_number_sum(start: int, end: int) -> int:
    #Return the sum of all perfect numbers within the inclusive range [start, end]
    def is_perfect(n: int) -> bool:
        return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

    return sum(n for n in range(start, end + 1) if is_perfect(n))


# 2. Weight Unit Converter
def weight_converter(value: float, direction: str) -> float:
    #Convert between kilograms and pounds. Use 'K' for kg→lb and 'P' for lb→kg.
    if direction.upper() == 'K':
        return round(value * 2.205, 2)
    elif direction.upper() == 'P':
        return round(value / 2.205, 2)
    else:
        raise ValueError("Invalid direction. Use 'K' for kilograms to pounds or 'P' for pounds to kilograms.")


# 3. Vowel Counter
def count_vowels(text: str) -> int:
    #Return the number of vowels in the string (case insensitive).
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)


# 4. Average and Range Finder
def average_and_range(numbers: list[float]) -> tuple[float, float]:
    """Return the average and range (max – min) of the numbers."""
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    avg = sum(numbers) / len(numbers)
    rng = max(numbers) - min(numbers)
    return round(avg, 2), round(rng, 2)


# 5. String Reverser with Word Count
def reverse_and_count_words(text: str) -> tuple[str, int]:
    """Return the reversed string and the word count (handling multiple spaces)."""
    reversed_str = text[::-1]
    words = [w for w in text.split(" ") if w.strip() != ""]
    return reversed_str, len(words)


# 6. Specific Word Counter
def specific_word_counter(file_url: str) -> dict:
    """Count the occurrences of specific words ['is', 'are', 'has', 'have'] in a text file from URL."""
    try:
        with urllib.request.urlopen(file_url) as response:
            text = response.read().decode("utf-8").lower()
    except Exception:
        raise ConnectionError("Failed to fetch file content. Check the URL or internet connection.")

    target_words = ["is", "are", "has", "have"]
    counts = {word: text.count(word) for word in target_words}
    return counts


# Main Program
def main():
    FILE_URL = "https://gist.github.com/konrados/a1289ade329ac6f4598ebf5ee3dbcb3c"
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate sum of perfect numbers")
        print("2. Convert weight units")
        print("3. Count vowels in string")
        print("4. Find average and range of numbers")
        print("5. Reverse string and count words")
        print("6. Count specific words in text file")
        print("0. Exit program")

        choice = input("Enter your choice: ").strip()
        if choice == '0':
            print("Goodbye! 👋")
            break

        try:
            if choice == '1':
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                print(f"Sum of perfect numbers: {perfect_number_sum(start, end)}")

            elif choice == '2':
                val = float(input("Enter weight value: "))
                direction = input("Enter 'K' for kg→lb or 'P' for lb→kg: ").strip()
                print(f"Converted value: {weight_converter(val, direction)}")

            elif choice == '3':
                text = input("Enter a string: ")
                print(f"Number of vowels: {count_vowels(text)}")

            elif choice == '4':
                n = int(input("How many numbers to enter? "))
                nums = []
                for i in range(n):
                    nums.append(float(input(f"Enter number {i+1}: ")))
                avg, rng = average_and_range(nums)
                print(f"Average: {avg}, Range: {rng}")

            elif choice == '5':
                text = input("Enter a string: ")
                rev, wc = reverse_and_count_words(text)
                print(f"Reversed: {rev}\nWord count: {wc}")

            elif choice == '6':
                counts = specific_word_counter(FILE_URL)
                for word, count in counts.items():
                    print(f"{word}: {count}")

            else:
                print("Invalid choice!. Please enter a number between 0 and 6.")

        except Exception as e:
            print(f" ! Error: {e}")

        again = input("\nWould you like to try another function? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye! :) ")
            break


if __name__ == "__main__":
    main()
