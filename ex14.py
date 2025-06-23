from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hi {user_name}, I'm the script.")
print(f"Where do you live?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Your name is {user_name},
You live in {lives},
And you have a {computer} computer
""")
