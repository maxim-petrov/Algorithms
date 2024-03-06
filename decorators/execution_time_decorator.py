import time
from functools import wraps


class ExecutionTimeDecorator:
    def __init__(self, num_runs=100):
        self.num_runs = num_runs

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(self.num_runs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                total_time += (end_time - start_time)
            average_time = total_time / self.num_runs
            print(
                f"Average execution time over {self.num_runs} "
                f"runs: {average_time:.6f} seconds."
            )
            return result
        return wrapper
