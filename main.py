def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    #print(word_count(file_contents))
    #print(char_count(file_contents))
    report(file_contents)

def word_count(t):
    cnt = len(t.split())
    return cnt

def char_count(t):
    lowered_text = t.lower()
    cnts = {}

    for c in lowered_text:
        if c in cnts:
            cnts[c] += 1
        else: cnts[c] = 1

    return cnts

def report (t):
    tot_words = word_count(t)
    all_cnts = char_count(t)
    pairs = [{"key": key, "value": value} for key, value in all_cnts.items()]

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{tot_words} words found in the document\n")

    pairs.sort(reverse=True, key=lambda x: x["value"])

    for pair in pairs:
        if pair["key"].isalpha():
            print(f"The '{pair["key"]}' character was found {pair["value"]} times")
    print("--- End report ---")





main()
