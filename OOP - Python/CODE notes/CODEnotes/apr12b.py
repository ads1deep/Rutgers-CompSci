def fetcher(obj, idx):
    return obj[idx]

try:
    fetcher("hello", 3)
except IndexError:
    print("error: invalid index")
finally:
    print("in finally block")
print("after finally block")


