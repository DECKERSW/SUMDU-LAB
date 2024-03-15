import string

def count_words_by_length(file_name):
    word_counts = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Розділити рядок на слова, використовуючи тільки букви та дефіси
                words = ''.join(c if c.isalpha() or c == '-' else ' ' for c in line).split()
                for word in words:
                    length = len(word)
                    if length not in word_counts:
                        word_counts[length] = 0
                    word_counts[length] += 1
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    return word_counts

# Решта коду залишається незмінною


def write_word_counts_to_file(word_counts, output_file):
    try:
        with open(output_file, 'w') as file:
            for length, count in word_counts.items():
                file.write(f"Words of {length} characters: {count}\n")
    except IOError:
        print("Помилка запису у файл")

def print_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Файл не знайдено")

def create_text_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("The quick brown fox jumps over the lazy dog.\n")
            file.write("Pack my box with five dozen liquor jugs.\n")
            file.write("How razorback-jumping frogs can level six piqued gymnasts!\n")
            #2 - 1
            #3 - 8
            #4 - 6
            #5 - 6
            #6 - 2
            #8 - 1
            #17- 1
    except IOError:
        print("Помилка створення файлу")

if __name__ == "__main__":
    input_file = "TF4_1.txt"
    output_file = "TF4_2.txt"

    # Create input text file
    create_text_file(input_file)

    # Count words by length
    word_counts = count_words_by_length(input_file)

    if word_counts is not None:
        # Write word counts to output file
        write_word_counts_to_file(word_counts, output_file)

        # Print contents of output file
        print("Вміст файлу TF4_2:")
        print_file_contents(output_file)
