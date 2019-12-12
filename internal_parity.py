import csv


def grabChallenges():
    import csv
    all_challenges = []
    with open('challenge_response_pairs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            all_challenges.append(row[0:63])
    return all_challenges


# function that takes in 64 bits from csv and int number of internally generated bits (0-32)
def internal_parity_generation(num_generated_bits):
    all_challenges = grabChallenges()
    last_index_of_challenge = 63 - int(num_generated_bits)
    new_challenges = []
    for index in all_challenges:
        new_challenge = index[0:last_index_of_challenge]
        # generating all bits necessary
        extra_bits = ""
        bit = 0
        while bit < int(num_generated_bits):
            # call function that xor's challenge bits and returns new bit
            new_bit = generate_challenge_bit(bit, index)
            # add to list
            new_challenge.append(new_bit)
            bit += 1
        # adding to new list of challenges
        new_challenges.append(new_challenge)
    file_name = "parity_w_" + num_generated_bits + "_bits.csv"
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_challenges)


def generate_challenge_bit(bit, challenge):
    # saving bits from challenge to list in order to xor
    bits_to_xor = [challenge[bit], challenge[bit+1]]

    # taking -1 into account and making into zero in order to xor
    if bits_to_xor[0] == '-1':
        bits_to_xor[0] = 0
    if bits_to_xor[1] == '-1':
        bits_to_xor[1] = 0

    # performing bitwise xor of challenge bits to generate new internally generated parity challenge bits
    challenge_bit = int(bits_to_xor[0]) ^ int(bits_to_xor[1])

    # making challenge bit -1/1 and getting rid of zeros
    if challenge_bit == 0:
        challenge_bit = -1
    return challenge_bit


if __name__ == "__main__":
    num = input("how many internally generated bits would you like to generate? ")
    internal_parity_generation(num)