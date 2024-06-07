'hw_5.3'
import string

user_input = input('Enter: ')
cleaned_input = ''.join(char for char in user_input if char not in string.punctuation)
words = cleaned_input.split()
titled_input = ''.join(word.capitalize() for word in words if word)
hashtag = f'#{titled_input[:139]}'
print(f'{user_input} -> {hashtag}')