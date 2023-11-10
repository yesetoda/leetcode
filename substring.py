def get_all_substrings(string):
    substrings = []
    length = len(string)

    for i in range(length):
        for j in range(i+1, length+1):
            substrings.append(string[i:j])

    return substrings

string = "".join([str("x") for i in range(500)])
all_substrings = get_all_substrings(string)
print(all_substrings)