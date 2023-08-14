def word_counter(text):
    words = text.split()
    num_words = len(words)

    characters = len(text)

    # Counting sentences by assuming that each sentence ends with '.', '!', or '?'
    sentences = text.count('.') + text.count('!') + text.count('?')

    return num_words, characters, sentences

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    word_count, char_count, sentence_count = word_counter(input_text)

    print(f"Number of words: {word_count}")
    print(f"Number of characters: {char_count}")
    print(f"Number of sentences: {sentence_count}")
