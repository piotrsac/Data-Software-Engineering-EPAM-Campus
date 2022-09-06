
def decorator_apply(lambda_func):
    '''
    Add your implementation here
    '''
    pass


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num
