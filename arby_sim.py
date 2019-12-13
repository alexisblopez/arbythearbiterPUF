import csv


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


def getParityVectors(challenges):
    import numpy
    parityVectors = []

    for row in challenges:
        parityVector = []
        del parityVector[:]

        for count, element in enumerate(row):
            j = count
            parityBits = []
            while j < len(row):
                parityBits.append(1 - (2 * row[j]))
                j = j + 1
            parityBit = numpy.prod(parityBits)
            del parityBits[:]
            # print(len(parityBits))
            parityVector.append(parityBit)
        print(parityVector)

        parityVectors.append(parityVector)

    return parityVectors


def supportVectorMachine():
    challengeResponsePairs = grabChallengeResponsePairs()

    challenge, response = splitChallengesResponsePairs(challengeResponsePairs)

    trainSVM()

    testSVM()

    print(challenge)
    print(response)


def print_parity_to_csv(parityVectors):
    print("writing parity vectors to csv file\n")
    with open('parity_vectors.csv', 'w') as csv_File:
        writer = csv.writer(csv_File)
        for row in parityVectors:
            writer.writerow(parityVectors[row])
    print("done writing parity vector csv file\n")


if __name__ == "__main__":
    supportVectorMachine()


