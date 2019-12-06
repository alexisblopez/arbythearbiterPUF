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

    challenge, response = splitChallengesResponsePairs()

    trainSVM()

    testSVM()


if __name__ == "__main__":

    # print(challenges)
    # print(responses)

    supportVectorMachine()
