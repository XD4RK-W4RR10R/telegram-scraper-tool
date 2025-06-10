# utils/delay.py
import random
import time

def random_sleep(min_seconds=3, max_seconds=8):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)
