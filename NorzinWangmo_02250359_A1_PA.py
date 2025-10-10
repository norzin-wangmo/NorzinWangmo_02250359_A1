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
    #Return the average and range (max – min) of the numbers.
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    avg = sum(numbers) / len(numbers)
    rng = max(numbers) - min(numbers)
    return round(avg, 2), round(rng, 2)


# 5. String Reverser with Word Count
def reverse_and_count_words(text: str) -> tuple[str, int]:
    #Return the reversed string and the word count (handling multiple spaces).
    reversed_str = text[::-1]
    words = [w for w in text.split(" ") if w.strip() != ""]
    return reversed_str, len(words)


# 6. Specific Word Counter
def specific_word_counter():
    # Count the occurrences of specific words ['is', 'are', 'has', 'have'] in File.txt
    try:
        # Open and read the local File.txt
        file = open("File.txt", "r")
        text = file.read()
        file.close()
    except:
        print("Error: Could not find or read File.txt file.")
        return {"is": 0, "are": 0, "has": 0, "have": 0}

    # Convert text to lowercase for counting
    text = text.lower()
    
    # Split text into individual words
    words = text.split()
    
    # Remove punctuation from each word
    clean_words = []
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalpha():  # Keep only letters
                clean_word = clean_word + char
        if clean_word:  # Add word if it's not empty
            clean_words.append(clean_word)
    
    # Count target words
    target_words = ["is", "are", "has", "have"]
    counts = {"is": 0, "are": 0, "has": 0, "have": 0}
    
    for word in clean_words:
        if word in target_words:
            counts[word] = counts[word] + 1
    
    return counts


# Main Program
def main():
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate sum of perfect numbers")
        print("2. Convert weight units")
        print("3. Count vowels in string")
        print("4. Find average and range of numbers")
        print("5. Reverse string and count words")
        print("6. Count specific words in text file")
        print("0. Exit program")

        # Loop until valid choice is entered
        while True:
            choice = input("Enter your choice: ").strip()
            if choice in {'0','1','2','3','4','5','6'}:
                break
            print("Invalid choice!. Please enter a number between 0 and 6.")

        if choice == '0':
            print("Goodbye!")
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
                counts = specific_word_counter()
                print("Word counts from File.txt:")
                for word, count in counts.items():
                    print(f"{word}: {count}")

        except Exception as e:
            print(f" ! Error: {e}")

        while True:
            again = input("\nWould you like to try another function? (y/n): ").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                print("Goodbye! :) ")
                return
            else:
                print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()