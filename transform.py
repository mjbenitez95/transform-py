import sys, signal, random, time, string

colors = [
    '\033[95m',
    '\033[94m',
    '\033[96m',
    '\033[92m',
    '\033[93m',
    '\033[91m',
]

def signal_handler(sig, frame):
    sys.exit(0)

def get_possible_characters():
    possible_characters = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation)
    possible_characters.append(" ")
    return possible_characters

def generate_random_sentence(sentence_len, possible_characters):
    sentence = ""
    for i in range(0, sentence_len):
        sentence += random.choice(possible_characters)
    return sentence

def print_as_different_colors(sentence, found_letters):
    colorful_sentence = ""
    for i in range(0, len(sentence)):
        letter_color = random.choice(colors)
        if found_letters[i] is not None and found_letters[i][0] is True:
            letter_color = found_letters[i][1]
        colorful_sentence += letter_color
        colorful_sentence += sentence[i]
    print colorful_sentence

if __name__=="__main__":
    signal.signal(signal.SIGINT, signal_handler)

    possible_characters = get_possible_characters()

    user_sentence = raw_input("Enter a sentence: ")
    sentence_len = len(user_sentence)
    found_letters = [None] * sentence_len

    current_guess = generate_random_sentence(sentence_len, possible_characters)
    match_all = False
    guesses = 0

    while not match_all:
        guesses += 1
        print_as_different_colors(current_guess, found_letters)
        match_all = True
        for index in range(0, sentence_len):
            if current_guess[index] != user_sentence[index]:
                match_all = False
                current_guess = current_guess[:index] + random.choice(possible_characters) + current_guess[index + 1:]
            else:
                if found_letters[index] is None:
                    found_letters[index] = (True, random.choice(colors))

        time.sleep(0.02)

    print ""
    print "Sentence matched. Took", guesses, "iterations."
        
            