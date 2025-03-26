
def analyze():
    """
    Analyze string according to three requirements:
        1. how many words have maximum length
        2. display all words followed by a comma or point
        3. find the longest word that ends with 'e'
    Returns:
        dict: (max_length_count, right_words, longest_word)
    """
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    expressions = text.split()

    #1.
    words = [expr.rstrip(',.') for expr in expressions]
    word_lengths = [len(word) for word in words]
    max_length = max(word_lengths)
    max_length_count = word_lengths.count(max_length)

    #2.
    right_words = []
    for expr in expressions:
        word = expr.rstrip(',.')
        if len(word)<len(expr):
            right_words.append(word)

    #3.
    e_words = [word for word in words if word.lower().endswith('e')]
    longest_word = max(e_words, key=lambda x: len(x)) if e_words else None

    return {
        '1': max_length_count,
        '2': right_words,
        '3': longest_word
    }



def run_task4():
    result = analyze()

    print(f"\n1. Number of words with maximum length: {result['1']}")
    print(f"\n2. Words followed by comma/point: " + ",".join(result['2']))
    print(f"\n3. Longest word ending with 'e': {result['3']}")