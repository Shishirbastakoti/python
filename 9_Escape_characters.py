"""
Escape characters are used to insert syntatically incorrect symbols or special characters.

The case of syntatically incorrect example is

c="She is the most "beautiful" girl in the whole world"
print(c)

Above example is syntatically incorrect and while running it produces error as we cannot 
insert double quote (" ") within a double quote.

rather we can use \" escape character to print double quote

The example of using this escape sequence is :
"""

c="She is the most \"beautiful\" girl I have ever met."
print(c)

#for single quote \'
single_quote="He is the \'man\' of his word"
print(single_quote)

#for backslash \\
backslash="He\\She may or may not pass the mid term exam"
print(backslash)

#for new line \n
new_line="That boy is too nice.\n I want to talk to him."
print(new_line)

#for backspace \b
backspace="The US dollar is the most valuable currency in the world\b"
print(backspace)