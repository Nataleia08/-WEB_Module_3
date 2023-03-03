from multiprocessing import cpu_count
from time import time
from multiprocessing import Process, Pool, Manager

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
    timers_start = []
    for i in [128, 255, 99999, 10651060]:
        timer = time()
        timers_start.append(timer)
        pr = Process(name= f"{i} number process", target= factorize, args= ([i],))
        pr.start()
        prs.append(pr)
        # pr.join()
    # [pr.join() for pr in prs]
    timers_end = []
    for pr in prs:
        pr.join()
        timer = time()
        timers_end.append(timer)
    # for tm1, tm2 in timers_start, timers_end:
    #     print(f"{pr.name} {round(tm2 - tm1, 4)} second")
    # [print(f"{pr.name} {round(time() - tm, 4)} second") for tm in timers]

    with Pool(processes=4) as pool:
        print(pool.map(factorize, [[128], [255], [99999], [10651060]]))

    with Manager() as manager:
        m = manager.dict()
        processes = []
        for i in [128, 255, 99999, 10651060]:
            pr = Process(target=factorize, args=([i], m))
            pr.start()
            processes.append(pr)

        [pr.join() for pr in processes]
        print(m)