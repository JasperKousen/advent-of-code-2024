import math


def get_primes(n):

    primes = []
    for i in range(2, n):
        while True:
            for x in range(2, int(math.sqrt(i) + 1)):
                if i % x == 0:
                    break
            else:
                primes.append(i)

def get_factors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def main():
    with open('input.txt') as f:
        data = f.read()

    ranges = [(int(d.split('-')[0]), int(d.split('-')[1])) for d in data.split(',')]

    # divisors = get_primes(max(end for _, end in ranges) // 2)
    # print(f"divisors: {len(divisors)}")

    def is_invalid(id):
        id = str(id)
        length = len(id)

        for d in get_factors(length):
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
