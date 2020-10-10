# First this app verify whether user is registered.
# Registered user can select between the hardcoded paragraphs 1 to 3.
# The selected paragraph will be analysed by this app.


welcome = print('\nWelcome to the Text analyser app!\nYou can select one of the three avalable texts.\nPlease login.\n')


# hardcoded users in dictionary
users = {'ann': '123',
         'bob': 'abc123',
         'ross': 'pass123',
         'mike': '123abc'
         }


# function to verify an user in dictionary
def is_user_registered():
    username = input('Enter Username:')
    password = input('Enter Password:')
    for user in users:
        if username == user:
            if password == users[user]:
                return True
    return False


# hardcoded text which is used for text analysis
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


def repeat_characters(char, num_repetitions):
    return char * num_repetitions


def ask_user_for_input(list_length):
    user_input = - 1  # -1 as helper
    while user_input == - 1:
        selection = input('Your selection: ')
        if selection.isnumeric():
            selection = int(selection)
            if 0 < selection <= list_length:
                user_input = selection
                return user_input - 1  # texts index 0
            else:
                print('Only numbers 1-' + str(list_length) + ' are accepted.')
        else:
            print('Only positive numbers are accepted.')


def count_words(input_text):
    words = len(input_text.split())
    return words


def count_words_start_upper(input_text):
    start_upper = sum(1 for word in input_text.split() if word[0].isupper())
    return start_upper


def count_words_contain_upper(input_text):
    total = 0
    for word in input_text.split():
        if contains_uppercase(word):
            total = total + 1
    return total


# function return true in case the argument contains uppercase
def contains_uppercase(word):
    for char in word:
        if char.isupper():
            return True
    return False


def count_words_starts_lower(input_text):
    lower = sum(1 for word in input_text.split() if word[0].islower())
    return lower


def count_string_numeric(input_text):
    number = sum(1 for num in input_text.split() if num.isdigit())
    return number


def dictionary_length_frequency(input_text):
    dictionary = {}
    text_split = input_text.split()
    for word in text_split:
        word = word.strip('.,?!\'\"')
        if len(word) in dictionary:
            dictionary[len(word)] = dictionary[len(word)] + 1
        else:
            dictionary[len(word)] = 1
    return dictionary


def print_my_dictionary(my_dictionary):
    # for key, value in my_dictionary.items():
    #     print(key, (repeat_char('*', value)), value)
    ordered_list = sorted(my_dictionary.items())
    for my_tuple in ordered_list:
        print(my_tuple[0], end=' ')
        print(repeat_characters('*', my_tuple[1]), end=' ')
        print(my_tuple[1])


def total_sum_digits(input_text):
    sum_digit = 0
    for num in input_text.split():
        if num.isdigit():
            number = int(num)
            sum_digit = sum_digit + number
    return sum_digit


# function to call the text analyser functions
def text_process(list_of_texts):
    selected_paragraph = list_of_texts[ask_user_for_input(len(list_of_texts))]
    print(repeat_characters('-', 70))
    print('Total number of words in selected paragraph is:', count_words(selected_paragraph))
    print('Total words start with upper-case letter in selected paragraph is:',
          count_words_start_upper(selected_paragraph))
    print('Total words contain upper-case letter in selected paragraph is:',
          count_words_contain_upper(selected_paragraph))
    print('Total words start with lower-case letter in selected paragraph is:',
          count_words_starts_lower(selected_paragraph))
    print('Total numeric strings in selected paragraph is:', count_string_numeric(selected_paragraph))
    print(repeat_characters('-', 70))
    print_my_dictionary(dictionary_length_frequency(selected_paragraph))
    print(repeat_characters('-', 70))
    print('Total sum of all numbers in selected paragraph:', total_sum_digits(selected_paragraph))
    print(repeat_characters('-', 70))

# function to run the entire text analyser app
def run_project(list_of_texts):
    if is_user_registered():
        text_process(list_of_texts)
    else:
        print('You are not registered.')


run_project(TEXTS)
