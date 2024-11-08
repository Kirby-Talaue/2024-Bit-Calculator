# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration *5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- instruction 1
- instruction 2
- etc
    ''')

# display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions or any key to continue")

if want_instructions == "":
    instructions()

print("Program continues")
