
# Case:

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or
# other items. We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take in input array, containing the names
# of people who like an item. It must return the display text as shown in the examples:

# Solution:

def likes(names):
    num_names = len(names)
    result = ""
    if num_names == 0:
        result = "no one likes this"
    elif num_names == 1:
        result = names[0] + " likes this"
    elif num_names == 2:
        result = names[0] + " and " + names[1] + " like this"
    elif num_names == 3:
        result = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        magic_num = num_names - 2
        result = names[0] + ", " + names[1] + " and " + str(magic_num) + " others like this"
    return result


def main():
    test_dictionary = {
        'names_0': [],
        'names_1': ["Peter"],
        'names_2': ["Jacob", "Alex"],
        'names_3': ["Max", "John", "Mark"],
        'names_4': ["Alex", "Jacob", "Mark", "Max"]
    }

    for i in range(5):
        result = likes(test_dictionary.get('names_' + str(i)))
        print(result)


if __name__ == '__main__':
    main()
