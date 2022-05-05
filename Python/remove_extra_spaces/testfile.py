# Refer to README.md for the problem instructions


def remove_extra_spaces(sentence):
    result = str()
    containsExtraSpaces = False
    for index in range(len(sentence)):
        if (index == 0 and sentence[index] == " "):
            containsExtraSpaces = True
        elif (index == len(sentence) - 1 and sentence[index] == " "):
            containsExtraSpaces = True
        elif (sentence[index] == " " and sentence[index + 1] == " "):
            containsExtraSpaces = True
        else:
            result += sentence[index]
    
    if containsExtraSpaces:
        return result
    else:
        return "The input sentence does not contain extra spacing"
