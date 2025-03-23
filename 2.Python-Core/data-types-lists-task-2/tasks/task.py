from typing import Union, List

ListType = List[Union[int, str]]

def get_fizzbuzz_list(n: int) -> ListType:
    t=[]
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            t.append('FizzBuzz')
        elif i % 3 == 0:
            t.append('Fizz')
        elif i % 5 == 0:
            t.append('Buzz')
        else:
            t.append(i)

    return t

if __name__ == '__main__':
    assert (get_fizzbuzz_list(15))==[1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz']
