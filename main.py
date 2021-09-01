from PIL import Image
import pytesseract
import io

def process_image(image_name, lang_code):
    return pytesseract.image_to_string(Image.open(image_name), lang=lang_code)

def print_data(data):
    print(data)

def output_file(filename, data):
    file = io.open(filename, "w+", encoding="utf-8")
    file.write(data)
    file.close()

def main():
    data_eng = process_image("test_eng.png", "eng")
    data_ben = process_image("test_ben.png", "ben")

    print(data_eng)
    print(data_ben)

    output_file("eng.txt", data_eng)
    output_file("ben.txt", data_ben)

if __name__ == "__main__":
    main()