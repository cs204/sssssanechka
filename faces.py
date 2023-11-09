def convert(inputString):
    inputString = inputString.replace(':)','\N{Slightly Smiling Face}')
    inputString = inputString.replace(':(', '\N{Slightly Frowning Face}')
    return inputString

textIn = input()
print(convert(textIn))