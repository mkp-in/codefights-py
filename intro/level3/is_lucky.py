"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.

"""


def isLucky(n):

    def sum_digits(num):
        total = 0
        while num != 0:
            total += num % 10
            num = num // 10

        return total

    s = str(n)
    half_len = int(len(s)/2)
    first_half = s[:half_len]
    second_half = s[half_len:]
    if sum_digits(int(first_half)) == sum_digits(int(second_half)):
        return True

    return False


if __name__ == '__main__':
    print(isLucky(1230))

