def grabChallengeResponsePairs():
    import csv

    all_challenge_response_pairs = []

    with open('challenge_response_pairs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            all_challenge_response_pairs.append(row)

    return all_challenge_response_pairs


if __name__ == "__main__":
    # let's read the name of bench file
    print(grabChallengeResponsePairs())
