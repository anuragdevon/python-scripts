#!usr/bin/python3

# E-mail and phone number extractor
import pyperclip
import re

# text containing email's and phone number to be pasted from clipboard
text = str(pyperclip.paste())

# regular expression for phone numbers
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?    # this is for non-greedy approach for area code
    (\s|-|\.)?            # this is for hypen or a dot(phoneNumbe format)
    (\d{3})               # first 3 digit
    (\s|-|\.)?            # separator
    (\d{4})               # last 4 digits

)''', re.VERBOSE)

# regular expression for emails
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     # UserName
    @                     # symbol
    [a-zA-Z0-9.-]+        # domain Name
    (\.[a-z{2,4}])        # dot something
)''', re.VERBOSE)

match = []  # list of storing all match found

for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1],groups[3],groups[5]])
    match.append(phone_number)

for groups in email_regex.findall(text):
    match.append(phone_number)

for groups in email_regex.findall(text):
    match.append(groups[0])

# copy the results to clipboard

if len(match)>0:
    pyperclip.copy('\n'.join(match))
    print('Copied to clipboard')
    print('\n'.join(match))

else:
    print("Oops! Nothing Found!")


