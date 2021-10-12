class TestA:
    attr = 1


obj_a = TestA()
obj_b = TestA()

TestA.attr = 42
print(obj_b.attr)
