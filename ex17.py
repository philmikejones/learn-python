from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_data = open(from_file).read()

print(f"The contents of the loaded file is {len(in_data)} bytes long.")
print(in_data)

if exists(to_file):
    print("The output file to_file exists. It will be overwritten.")
else:
    print("The output file, to_file, does not exist. It will be created")

out_file = open(to_file, "w")
out_file.write(in_data)
print("Success: file contents written.")

out_file.close()
