VALID = ['R', 'G', 'Y', 'P', 'B', 'O']


def display_feedback(feedback):
    print("Feedback: {0}{1}{2}{3}".format(feedback[0], feedback[1], feedback[2], feedback[3]))


def error_message():
    print("Error")


def final_score_codebreaker(num_turns):
    print("Score: -{0}".format(num_turns))


def find_id(a, g, r, cur):
    """
    Finds the identity (the letters that match)
    Parameters: a (list), g (list), r (list), cur (list)
    """
    for index, pair in enumerate(zip(a, g)):
        if pair[0] == pair[1]:
            r[index] = pair[0]
            cur[index] = 1


def find_w(result, guess, actual, taken):
    """
    Finds the letters that need to be replaced with W
    Parameters: g (list), r (list), cur (list)
    """
    # for each character in the guess, see if we have something in the result that is not yet taken
    for i, c in enumerate(guess):
        # check if this character in the guess is some nontaken character in the actual
        for j, a in enumerate(actual):
            # if we find a match, take it and stop looking for matches for this index in the guess
            if taken[j] == 0 and a == c:
                result[i] = 'W'
                taken[j] = 1
                break


def do_turn(actual):
    result = ['_', '_', '_', '_']
    guess = input("Guess: ")

    if len(guess) > 4 or len(guess) < 4:
        error_message()
        return

    for c in guess:
        if c not in VALID:
            error_message()
            return

    taken = [0, 0, 0, 0]

    find_id(actual, guess, result, taken)

    find_w(result, guess, actual, taken)

    feedback = ''.join(result)
    display_feedback(feedback)
    return feedback


def game(file):
    for actual in file:
        actual = actual.strip("\n")
        turns = 0

        while turns < 10:
            feedback = do_turn(actual)

            if feedback is None:
                turns += 0
            else:
                turns += 1

            if feedback == actual:
                final_score_codebreaker(turns)
                break

            if turns == 10:
                final_score_codebreaker(turns)
                break


def main():
    with open("input.txt", "r") as file:
        game(file)


main()