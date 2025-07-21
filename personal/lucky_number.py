import time
class Test:
    def __init__(self):
        print(self.lucky_number(1, 2, 5))

    def lucky_number(self, x, y, n) -> str:
        ###################################
        start_time = time.time()
        ###################################

        x, y = min(x,y), max(x,y)

        cnt_x = n // x
        while (n - cnt_x*x) <=0 or (n - cnt_x*x) % y != 0:
            cnt_x -= 1

        cnt_y = (n - cnt_x*x) // y

        res = str(y)*cnt_y + str(x)*cnt_x

        ###################################
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"실행 시간: {elapsed_time:.4f}초")
        ###################################

        return res

if __name__ == '__main__':
    Test()