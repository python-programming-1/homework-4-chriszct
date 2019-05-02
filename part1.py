vegetables = ['carrot', 'lettuce', 'onion', 'radish']

def func (some_list):
    my_formatted_string = ''
    for i in some_list:
        if i == some_list[-1]:
            my_formatted_string = my_formatted_string + i + '.'
        else:
            my_formatted_string = my_formatted_string + i + ', '
    return my_formatted_string

print(func(vegetables))

input() # for the prompt window to stay