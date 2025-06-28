import sys
script, input_encoding, error = sys.argv

# main function, called at the end of the script
def main(language_file, encoding, errors):
    # read first line from given language file
    line = language_file.readline()
    # tests to see if there is something in the line and continues until the line is blank
    if line:
        # uses a separate function to print the line to keep this function readable
        print_line(line, encoding, errors)
        # calls main() inside itself basically to jump to the top and repeat
        # so calls the function, which first reads the next line, then the if statement
        # checks if there is content there; this stops it running forever
        return main(language_file, encoding, errors)

# Called by main()
def print_line(line, encoding, errors):
    next_lang = line.strip()  # strips "\n" from the line so there are not double newlines
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

# functions defined; now open the file
languages = open("languages.txt", encoding = "utf-8")

# runs the main function (which also uses print_line())
main(languages, input_encoding, error)

greek_raw = b'\xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac'.decode("utf-8")
print(greek_raw)
