from sys import stdin


MIN_SINGLE_SIGNED_BYTE_VALUE = -127
MAX_SINGLE_SIGNED_BYTE_VALUE = 127

ESCAPE_TOKEN_VALUE = -128


def read_sequence():
    sequence = stdin.readline()
    return [int(x) for x in sequence.split()]


def is_single_signed_byte_value(number):
    return number >= MIN_SINGLE_SIGNED_BYTE_VALUE and number <= MAX_SINGLE_SIGNED_BYTE_VALUE


def transform_with_difference(sequence):
    if len(sequence) == 0:
        return []
    
    result_sequence = []
    result_sequence.append(sequence[0])
    for i in range(len(sequence)-1):
        element = sequence[i+1] - sequence[i]
        result_sequence.append(element)
    
    return result_sequence


def transform_with_escape_token(sequence):
    if len(sequence) == 0:
        return []

    result_sequence = []
    result_sequence.append(sequence[0])
    for i in range(len(sequence)-1):
        if not is_single_signed_byte_value(sequence[i+1]):
            result_sequence.append(ESCAPE_TOKEN_VALUE)
        result_sequence.append(sequence[i+1])
    
    return result_sequence


sequence = read_sequence()
delta_encoding_sequence = transform_with_escape_token(transform_with_difference(sequence))

print(" ".join(str(n) for n in delta_encoding_sequence))
