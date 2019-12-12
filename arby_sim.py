def grabChallengeResponsePairs():
    import csv

    all_challenge_response_pairs = []

    with open('challenge_response_pairs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            all_challenge_response_pairs.append(row)

    return all_challenge_response_pairs


def splitChallengesResponsePairs(all_challenge_response_pairs):
    responses = []
    binaryChallenges = []
    decimalChallenges = []

    for response in all_challenge_response_pairs:
        responses.append(int(response[64]))

    for challenge in all_challenge_response_pairs:
        binaryChallenges.append(''.join(challenge[0:63]))

    for challenge in binaryChallenges:
        decimalChallenges.append(int(challenge, 2))

    return decimalChallenges, responses


def trainSVM():
    print('train me')


def testSVM():
    print('test me')


def supportVectorMachine():
    challengeResponsePairs = grabChallengeResponsePairs()

    challenge, response = splitChallengesResponsePairs(challengeResponsePairs)

    trainSVM()

    testSVM()

    print(challenge)
    print(response)


def parity_gen(challenges):
    parity_bits = []
    for row in challenges:
        for c_bit in challenges[row]:
            bit = c_bit
            parity = 1
            while bit < len(challenges[row]):
                parity = parity * (1 - 2 * challenges[row][c_bit])
                bit += 1
            parity_bits[row][c_bit] = parity
    return parity_bits


if __name__ == "__main__":
    supportVectorMachine()
