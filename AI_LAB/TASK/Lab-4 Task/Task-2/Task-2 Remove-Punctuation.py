# Remove Punctuations From String...........

def remove_punctuation(input_string):
    punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    result = ""

    for char in input_string:
        if char not in punctuation:
            result += char

    return result

user_input = input("Enter a string :")
cleaned_string = remove_punctuation(user_input)
print("String without Punctuation :", cleaned_string)
