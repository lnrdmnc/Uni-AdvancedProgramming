
@float_args_and_return
def mean(first,second,*rest):
    numbers=(first,second) +rest
    return sum(numbers)/ len(numbers)


def float_args_and_return(function):
    def wrapper(*args,**kwargs):
        args=[float(arg) for arg in args]
        return float(function(*args,**kwargs))
    return wrapper

def mean(first,second,*rest):
    numbers=(first,second) +rest
    return sum(numbers)/ len(numbers)

