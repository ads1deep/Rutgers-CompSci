def fetcher(obj, idx):
    return obj[idx]

def catcher(obj, i):
    try:
        answer = fetcher(obj, i)
    except IndexError:
        print("caught an exception: ", i, "is invalid index")
        answer = "Index error"
    except:
        print("some other exception")
        answer = "some other error"
    finally:
        print("in finally block")
    print("continuing on...")
    return answer
    
