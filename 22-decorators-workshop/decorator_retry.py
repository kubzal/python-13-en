import random

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise Exception("All attempts failed")
        return wrapper
    return decorator

@retry(3)
def risky_operation():
    if random.random() < 0.7:
        raise ValueError("Error from risky operation")
    return "Succeed!"

print(risky_operation())