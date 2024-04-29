import concurrent.futures
def worker():
    print("Worker thread running")
pool = concurrent.futures.ThreadPoolExecutor(max_workers=3)

pool.submit(worker)
pool.submit(worker)
pool.submit(worker)

print("Main thread continuing to run")
