def count_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    char_counts = {}
    words = file_contents.split()
    for word in words:
        for char in word:
            if char.lower() not in char_counts:
                char_counts[char.lower()] = 1
            else:
                char_counts[char.lower()] += 1
    return char_counts

def sort_list_of_characters(char_counts):
    def sort_on(item):
        return item["num"]

    chars = []
    for char in char_counts:
        chars.append({"char": char, "num": char_counts[char]})
    chars.sort(reverse=True, key=sort_on)
    return chars
