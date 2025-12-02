def main():
    with open('input_test.txt') as f:
        data = f.read()

    ranges = [(int(d.split('-')[0]), int(d.split('-')[1])) for d in data.split(',')]

    def is_valid(id):
        id = str(id)

        length = len(id)
        if length % 2 == 1:
            return True

        if str(id)[:length//2] == str(id)[length//2:]:
            return False

        return True

    invalid = []
    for start, end in ranges:
        for id in range(start, end + 1):
            if not is_valid(id):
                invalid.append(id)

    print(invalid)
    print(sum(invalid))



if __name__ == '__main__':
    main()
