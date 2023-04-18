from time import *
import string

def ft_progress(lst):
    t = time()
    barSize = 60
    last = int(lst[-1])
    l = 1
    if last < 0:
       l *= -1
    complete = last + l
    total =(abs(complete - l))
    for n, m in enumerate(lst,1): 
        yield m
        progress = int(round(barSize * (n - 1)) / total)
        bar = '=' * progress + '>'# + ' ' * (barSize - progress)
        per = int(100 * (progress) / barSize)
        elapsed = time() - t
        eta = elapsed / n * (total - n + 1)
        print("\rETA: {t:.2f}s [{p:>3}%%][{s:<{b}}] {i:>{l}}/%i | elapsed time {e:.2f}s".format(s = bar, b = barSize + 1,t=eta, p= per, e = elapsed, i = m + l, l = len(str(complete)))%(complete), end="")

if __name__ == "__main__":
    listy = range(300)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.01)
    print()
    print(ret)
