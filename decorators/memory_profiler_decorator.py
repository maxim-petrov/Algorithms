from memory_profiler import memory_usage

class MemoryProfilerDecorator:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        mem_before = memory_usage(max_usage=True)
        result = self.func(*args, **kwargs)
        mem_after = memory_usage(max_usage=True)
        print(
            f"Memory used by '{self.func.__name__}': "
            f"{mem_after - mem_before} MiB"
        )
        return result
