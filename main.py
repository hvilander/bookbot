

def countC(str_in):
    str_lower = str_in.lower()

    dic = {}

    for c in str_lower:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    for k,v in dic.items():
        msg = f"char: {k}, was found {v} times"
        print(msg)

    






def main():




    with open("books/frankenstein.txt") as f:
        frank = f.read()
        print(frank)
        print(f"Word count: {len(frank.split())}")

    # test countC
        print(countC(frank))





main()
