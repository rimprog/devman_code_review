from random import sample


def find_target_index(sorted_random_sequence, target):
    start_index = 0
    end_index = len(sorted_random_sequence) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if sorted_random_sequence[middle_index] < target:
            start_index = middle_index + 1
        elif sorted_random_sequence[middle_index] > target:
            end_index = middle_index - 1
        else:
            return middle_index

    return None


if __name__ == "__main__":
    sequence_len = 10
    random_sequence = sample(range(0, 101, 2), sequence_len)
    sorted_random_sequence = sorted(random_sequence)

    try:
        target = int(input('Pick a number between 0-100: '))
        target_index = find_target_index(sorted_random_sequence, target)

        print(f'List: {rand_list}')

        if target_index:
            print(f'Found {target} in index {target_index}')
        else:
            print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')
