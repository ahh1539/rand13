import matplotlib.pyplot as plt
import random

# run pip3 install matplotlib

# given
def rand11() -> int:
    return random.randint(1,11)

def rand13() -> int:
    rand = 117
    while rand >= 117:
        rand = (rand11() - 1) * 11 + rand11() - 1 # max of 120
    return rand % 13 + 1

if __name__ == "__main__":
    counter = {}
    # runs program 100,000 times to prove randomness
    for i in range(0, 100000):
        num = rand13()
        if counter.get(num):
            counter[num] += 1
        else:
            counter[num] = 1
    keys = counter.keys()
    values = counter.values()
    plt.bar(keys, values)
    plt.show()