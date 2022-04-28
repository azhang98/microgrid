num = 1
u_id = 1

def elapsed_time():
    import time
    elapsed_time = time.time()
    return "%02d:%02d:%02d" % (elapsed_time // 3600, (elapsed_time % 3600 // 60), (elapsed_time % 60 // 1))

def elapsed_time_seconds():
    import time
    elapsed_time = time.time()
    return elapsed_time
