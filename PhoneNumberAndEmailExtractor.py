import pyperclip
import re
phoneNumberRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? 				#Area code, We take note of two instances with and without brackets
	(\s|-|\.)?         				# separator
	\d{3}              				# first 3 digits
	(\s|-|\.).         				# seperator
	\d{4}              				# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?    # extension

	)''',re.VERBOSE)


emailAddressRegex = re.compile(r'''(

	\w+							#Email Name
	\@							# The @ symbol
	\w+						    #The domain provider
	(\.[a-zA-Z]{2,5})			#extension

	)''',re.VERBOSE)

   # Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneNumberRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    for groups in emailAddressRegex.findall(text):
    	matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')