from time import *
import string

def ft_progress(lst):
    t = time()
    barSize = 60
    complete = int(lst[-1]) + 1
    print("\rETA: 0.00s [{p:>3}%%][{s:>40}] 0/%i | elapsed time 0.00s".format(p="0", s = "")%(complete), end="")
    for n in lst: 
        yield n
        progress = int(round(barSize * (n+1)) / complete) 
        bar = '=' * progress + '>'# + ' ' * (barSize - progress)
        per = int(100 * (progress) / barSize)
        elapsed = time() - t
        eta = elapsed / (n + 1) * (complete - n -1)
        print("\rETA: {t:.2f}s [{p:>3}%%][{s:<{b}}] {i:>{l}}/%i | elapsed time {e:.2f}s".format(s = bar, b = barSize + 1,t=eta, p= per, e = elapsed, i = n+1, l = len(str(complete)))%(complete), end="")

if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
