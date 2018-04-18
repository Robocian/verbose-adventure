num = input("Give an integer: ")

remainder_dump = open("remainder_dump.txt", "a")


def is_prime():
    for i in range(2, num-1):
        check = num % i

        if check == 0:
            remainder_dump.write("Not prime/n")

remainder_dump.close()

#remainder_dump_check = open("remainder_dump.txt", "r")
