
def decorator_apply(lambda_func):
    def decorator(func):
        def wrapper(num):
            return func(lambda_func(num))
        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num

if __name__ == '__main__':
    assert return_user_id(3) == 4
    assert return_user_id(-5) == -4
    assert return_user_id(256) == 257