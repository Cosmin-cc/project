import string

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def process_text(filename):
    text = read_file(filename)
    return text

def main():
    input_file = "text.txt"
    processed_text = process_text(input_file)
    print("Processed text:")
    print(processed_text)

if __name__ == "__main__":
    main()
