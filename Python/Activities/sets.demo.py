example_set = {"apple", "banana"," cherry"}
print(example_set)

for item in example_set:
    print(item)

    example_set.add(" orange")# one item

    example_set.update(["mango grape"])

    print(example_set)
    print(len(example_set))

    # example_set.remove("berry")  #
    example_set.discard("cherry")
    print(example_set)

    example_set1 =set(("kiwi","blueberry", "grapes"))
    print(example_set)

