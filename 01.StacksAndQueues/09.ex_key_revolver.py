import timeit
from collections import deque

start = timeit.default_timer()
# inputs
bullet_price = int(input())
barrel_size = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks_queue = deque(int(lock) for lock in input().split())
intelligence_value = int(input())

safe_unlocked = False
bullets_fired = 0

# shooting
while bullets:
    bullet = bullets.pop()
    lock = locks_queue[0]
    if bullet <= lock:
        print("Bang!")
        locks_queue.popleft()
    else:
        print("Ping!")
    bullets_fired += 1
    if bullets_fired % barrel_size == 0 and bullets:
        print("Reloading!")

    if not locks_queue:
        safe_unlocked = True
        break

money_earned = intelligence_value - bullet_price * bullets_fired
if not safe_unlocked and not bullets:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
elif safe_unlocked:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
end = timeit.default_timer()
print(end - start)