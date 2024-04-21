def test_func():
    def inner_func():
        print("I am in scope 'test_func'")
    inner_func()
print(test_func())
# print(inner_func())