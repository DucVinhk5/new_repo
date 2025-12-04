import time
import sys

total = 50

for i in range(total + 1):
    percent = i / total
    bar = '#' * int(percent * 40) + '-' * (40 - int(percent * 40))
    print(f"f'\r[{bar}] {percent*100:.1f}%'", end="\r", flush=True)
    time.sleep(0.05)

# Khi xong, đổi màu chữ sang xanh lá
print("\n\033[92mHoàn thành!\033[0m")  # 92 = xanh lá, 0m = reset
