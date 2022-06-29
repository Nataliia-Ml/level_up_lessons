# a = [1, 2, 34]

# print(dir(a))
# my_iter = iter(a)
# print(type(my_iter))
# print(dir(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


def safe_iterator(iterable_list):
    try:
        x = iterable_list.__next__()
        return x
    except StopIteration:
        print("List is Empty")
        return False


# iterable_a = iter(a)
# res = True
#
# while res:
#     res = safe_iterator(iterable_a)
#     print(res)


# a = [1, 2, 34]
# b = ["A", "B", "C"]
# iterable_a = iter(a)
# iterable_b = iter(b)
#
# digits = safe_iterator(iterable_a)
# letters = safe_iterator(iterable_b)


def safe_iterator(iterable_list, size=1):
    res = []
    for _ in range(size):
        try:
            x = iterable_list.__next__()
            res.append(x)
        except StopIteration:
            print("List is Empty")
            return False
    return res


a = [1, 2, 34, 35, 36, 37]
iterable_a = iter(a)

print(safe_iterator(iterable_a, 2)) # [1, 2]
print(safe_iterator(iterable_a, 3)) # [34, 35, 36]
print(safe_iterator(iterable_a, 7)) # List is Empty, False
# Чтобы начать заново, нужно прописать iterable_a = iter(a)
