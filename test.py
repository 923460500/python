# -*-coding:utf-8-*-

w = [1, 2]
n = [2, 1]


def all():
    for i in range(len(w)):
        for l in range(n[i]):
            print(w[i]*n[l])


def main():
    all()


if __name__ == '__main__':
    main()
