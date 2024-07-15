import multiprocessing
import math
import sys
import time

#increasing maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

#function to compute factorial of given number
def compute_factorial(num):
    print(f"Computing Factorial of {num}")
    res=math.factorial(num)
    print(f"Factorial of {num} is: {res}")
    return res

if __name__=="__main__":
    num=[25,30,40,50]

    start_time=time.time()

    #create pool of workers process

    with multiprocessing.Pool() as pool:
        res=pool.map(compute_factorial,num)

    end_time=time.time()

    print(f"Results: {res}")
    print(f"Time taken: {end_time - start_time} seconds")
