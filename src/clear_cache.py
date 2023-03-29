import subprocess

def check_cache(threshold=5.0):
    ot = subprocess.check_output("free -h".split()).decode()
    i = i_count = 0
    while True:
        i = ot.find('i',i+1)
        i_count += 1
        if i_count==5:
            shared_i = i
            buff_i = ot.find('i',i+1)
            break
        if i==-1:
            exit()
    ot = ot[shared_i+1:buff_i].replace(' ','')
    print(ot)
    check_clear = ot[-1]=='G' and float(ot[:-1]) > threshold
    return check_clear

def clear_cache():
    subprocess.run(('sudo', 'sh', '-c', "echo 3 > /proc/sys/vm/drop_caches"))
    print('cache clear!')

def sub(threshold=5.0):
    print()
    subprocess.run('sync') # writeするときはsyncしたほうがいいとか
    flag = check_cache(threshold)
    if flag:
        clear_cache()



def main():
    import time
    while True:

        ot = subprocess.check_output("free -h".split()).decode()
        # start = ot.find('Mem',0)
        # end = ot.find('Swap',0)-1
        # ot = ot[start:end]
        print(ot)
        i = i_count = 0
        while True:
            i = ot.find('i',i+1)
            i_count += 1
            if i_count==5:
                shared_i = i
                buff_i = ot.find('i',i+1)
                break
            if i==-1:
                exit()

        ot = ot[shared_i+1:buff_i].replace(' ','')
        if ot[-1]=='G' and float(ot[:-1]) > 6.0:
            print('cache clear!')
            # subprocess.run("echo 3 > /proc/sys/vm/drop_caches".split())
            subprocess.run(('sudo', 'sh', '-c', "echo 3 > /proc/sys/vm/drop_caches"))

        time.sleep(5)

if __name__ == '__main__':
    main()

