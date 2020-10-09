welcome = print('Welcome to the best app ever')

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


# hardcoded text
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


# function to repeat characters or symbols, use inside some other functions
def repeat_char(char,num_repetitions):
    return char * num_repetitions


# function to print paragraph from TEXTS
def paragraphs_print(list_of_texts):
    print('Please, select one of these paragraphs:')
    print(repeat_char('=', 50))
    print('1', list_of_texts[0])
    print(repeat_char('-', 50))
    print('2\n', list_of_texts[1])
    print(repeat_char('-', 50))
    print('3\n', list_of_texts[2])
    print(repeat_char('=', 50))


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
    upper = sum(1 for word in input_text if word.isupper())
    return upper


def count_words_starts_lower(input_text):
    lower = sum(1 for word in input_text.split() if word[0].islower())
    return lower


def count_string_numeric(input_text):
    number = sum(1 for num in input_text.split() if num.isdigit())
    return number


def bar_chart_word_len_frequency(input_text):
    container = []
    text_split = input_text.split()
    for index, word in enumerate(text_split):
        word = word.strip('.,?!')
        length = len(word)
        container.append(length)
        return container


def text_process(list_of_texts):
    selected_paragraph = list_of_texts[ask_user_for_input(len(list_of_texts))]
    print('Total number of words in selected paragraph is:', count_words(selected_paragraph))
    print('Total words start with upper-case letter in selected paragraph is:', count_words_start_upper(selected_paragraph))
    print('Total words contain upper-case letter in selected paragraph is:', count_words_contain_upper(selected_paragraph))
    print('Total words start with lower-case letter in selected paragraph is:', count_words_starts_lower(selected_paragraph))
    print('Total numeric strings in selected paragraph is:', count_string_numeric(selected_paragraph))
    print('To jsem zvedava co to vytiskne', bar_chart_word_len_frequency(selected_paragraph))

def run_project(list_of_texts):
    if is_user_registered():
        text_process(list_of_texts)
    else:
        print('You are not registered.')


run_project(TEXTS)





