def main():
    with open('input.txt') as f:
        data = f.read()

    ranges = [(int(d.split('-')[0]), int(d.split('-')[1])) for d in data.split(',')]

    def is_invalid(id):
        id = str(id)
        length = len(id)

        for d in range(1, length // 2 + 1):
            if length % d != 0:
                continue

            if d >= length:
                return False

            if length % d == 1:
                continue

            parts = [id[i:i + d] for i in range(0, len(id), d)]

            if len(set(parts)) == 1:
                return True

        return False

    invalid = []
    for start, end in ranges:
        for id in range(start, end + 1):

            if is_invalid(id):
                invalid.append(id)

    print(invalid)
    print(sum(invalid))



if __name__ == '__main__':
    main()
