name = input("Enter file: ")
handle = open(name)

counts = dict()

for line in handle:
    words = line.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

biggest_count = None
biggest_word = None

for word,count in counts.items():
    if biggest_count is None or count > biggest_count:
        biggest_word = word
        biggest_count = count

print(biggest_word, biggest_count)
