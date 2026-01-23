# Write a custom context manager class using __enter__ and __exit__ that logs when a block starts and ends.


class LoggerContext:
    def __enter__(self):
        print("Block has started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Block has ended")
        return False

with LoggerContext():
    print("Inside the block")
