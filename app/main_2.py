from multiprocessing import cpu_count
from time import time
from multiprocessing import Process, Pool

def factorize(number: list) -> list:
    result_all = []
    for num in number:
        result = []
        for i in range(num+1)[1:]:
            if num % i == 0:
                result.append(i)
        result_all.append(result)
    return result_all
if __name__ == "__main__":

    exp = (128, 255, 99999, 10651060)
    timer1 = time()
    a, b, c, d = factorize(exp)
    print(a)
    print(b)
    print(c)
    print(d)
    print(f"{round(time() - timer1, 4)} second")
    print("cpu count = ", cpu_count())


    prs = []
    timers = []
    for i in exp:
        timer = time()
        timers.append(timer)
        pr = Process(name= f"{i} number process", target= factorize, args= ([i],))
        pr.start()
        prs.append(pr)
    # [pr.join() for pr in prs]
    [print(f"{round(time() - timer, 4)} second") for timer in timers]

    with Pool(processes=2) as pool:
        pool.map(factorize, [128, 255, 99999, 10651060])