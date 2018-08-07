def fetcher(obj, idx):
    return obj[idx]

def catcher(X):
    try:
        answer = fetcher(X, 2)
    except IndexError:
        print("I caught an exception: index out of range")
        answer = "error1"
    except TypeError:
        print("I caught an exception: cannot subscript " + str(type(X))) 
        answer = "error2"
    #except:
        #print("some other exception")
        #answer = "error3"
    else:
        print("index 2 worked for", X)
    finally:
        print("in finally block")
    print("continuing on...")
    return answer
