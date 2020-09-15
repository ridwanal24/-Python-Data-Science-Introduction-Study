import time

start_time = time.time()

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                print(a,b,c,d,e,f,g,h,type(a))


end_time = time.time()

print('executed in',end_time-start_time,'s')