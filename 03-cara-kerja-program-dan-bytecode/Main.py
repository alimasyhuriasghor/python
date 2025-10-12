# 3. Cara Kerja Program Dan Bytecode

# Python is an interpreted language, which means it executes our code line-by-line.
# Unlike many complied languages, Python does not generate an executable file; it directly translates the source code using the Python's interpreter.

import time

def simple_search(n: list, target: int) -> int:
    """Search a particular number within a list."""
    for index, value in enumerate(n):
        if value == target:
            return index
    return -1

start_time = time.perf_counter_ns()  
nums = list(range(1000))
target = -1
result = simple_search(nums, target)
end_time = time.perf_counter_ns()

print(f"The time that it took to execute the source code: {end_time - start_time:,} microseconds")
