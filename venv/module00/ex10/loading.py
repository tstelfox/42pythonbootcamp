import time
import os

bar = 35

def ft_progress(lst):
    starttime = time.time()
    for i in lst:
        yield i
        elapsed_time = time.time() - starttime
        completed = int(i / (len(lst) / 100))
        estimated = (elapsed_time / (i + 1)) * (len(lst) - i)
        filled = int(bar * (completed / 100))
        left = bar - filled
        os.system("clear")
        print(f"ETA: {estimated:.2f}s  [{completed}%][{filled * '='}>{left * ' '}] {i}/{len(lst)} | elapsed time {elapsed_time:.2f}s")
    os.system("clear")
    print(f"ETA: 0.0s  [100%][{(bar - 1) * '='}>] {i + 1}/{len(lst)} | elapsed time {elapsed_time:.2f}s")



if __name__ == '__main__':
    listy = range(200)
    ret = 0
    for elem in ft_progress(listy):
        # print(elem)
        ret += elem
        time.sleep(0.01)
    print()
    print("finished!")
    print(ret)