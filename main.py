## IMport to be able to load json file containing morse code
import json

print("Morse Code Converter")

## Open json file contianing morse code
with open("morse-code.json") as code:
    code = json.load(code)

## Take input for the user
text = input("Enter text to be converted to morse code: ").lower()

## Cycle throught the letteres in the text and compare to the dictionary codes

# Word converted to morse code
morse = ""

for letter in text:
    # Check if word is in json code file and doesn't change word if it isn't
    if letter in code:
        morse += code[letter]
        morse += " "

    else:
        morse += letter

## Output result
print(f"In morse-code your text is:  {morse}")

