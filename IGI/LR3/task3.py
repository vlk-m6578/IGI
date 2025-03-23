from input import input_agreement


def count_of_words(str):
    """
    The number of words starting with a lower and consonant letter 
    """
    consonant = set('qwrtpsdfghjklzxcvbnm')
    count = 0
    for word in str.split():
        if len(word) > 0 and word[0].islower() and word[0] in consonant:
            count += 1
    return count


def run_task3():
    while True:
        str = input("Enter string: ")

        result = count_of_words(str)

        print(f"Number of words: {result}")

        if not input_agreement("\nContinue? (y/n): "):
            break

