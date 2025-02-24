import string

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def rm_multiple_spaces(text):
    return ' '.join(text.split())

def to_lower(text):
    return text.lower()

def process_text(filename):
    text = read_file(filename)
    text = remove_punctuation(text)
    text = rm_multiple_spaces(text)
    text = to_lower(text)
    return text

def main():
    input_file = "text.txt"
    processed_text = process_text(input_file)
    print("Processed text:")
    print(processed_text)

if __name__ == "__main__":
    main()
