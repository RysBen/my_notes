# 1. 基本概念
- 进程和线程
- 全局（CPython）解释器锁

# 2. 
```python
from time import sleep,ctime

def lo(sec):
    print("loop%s starts: %s" %(sec,ctime()) )
    sleep(sec)
    print("loop%s ends: %s"%(sec,ctime()))

def main():
    print("Begin******************************")
    lo(1)
    lo(2)
    print("End*********************************")

if __name__ == "__main__":
    main()
```
