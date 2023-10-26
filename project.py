def count_words_in_file(file_name, words_list):
    # Open the file
    try:
        with open(file_name, 'r') as file:
            # Read the text from the file
            text = file.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
        return None

    # Initialize a dictionary to store the word counts
    word_counts = {}

    text = text.lower()
    
    # Remove punctuation marks, special characters and numbers
    text = ''.join(e for e in text if e.isalnum() or e.isspace())

    # Split the text into words
    words = text.split()

      # Iterate over each word in the list
    for word in words_list:
        # Convert the word to lowercase
        word = word.lower()

        # Count the occurrences of the word in the list of words
        word_counts[word] = words.count(word)

    # Return the dictionary containing the word counts
    return word_counts


def main():
    # Get the file name and the list of words from the user
    file_name = input("Enter the file name: ")
    words_list = input("Enter the list of words separated by spaces: ").split()

    # Call the function to count the occurrences of the words in the file
    word_counts = count_words_in_file(file_name, words_list)

    # Check if the word counts were obtained successfully
    if word_counts is not None:
        # Print the word counts
        for word, count in word_counts.items():
            print(f"'{word}': {count}")

if __name__ == "__main__":
    main()