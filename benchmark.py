import time

def benchmark():
    start_time = time.time()
    
    # Basic math operations
    result = 0
    for i in range(1, 10_000_001):
        result += i
        result *= 1.0000001
        result /= 1.0000001
    
    end_time = time.time()
    print(f"Result: {result}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
