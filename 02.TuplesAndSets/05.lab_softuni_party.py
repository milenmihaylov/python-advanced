n = int(input())
regular_guests = set()
vip_guests = set()
for _ in range(n):
    reservation_code = input()
    if len(reservation_code) == 8:
        if reservation_code[0].isdigit():
            vip_guests.add(reservation_code)
        else:
            regular_guests.add(reservation_code)

guests_at_party = set()
redeemed_code = input()
while not redeemed_code == 'END':
    guests_at_party.add(redeemed_code)
    redeemed_code = input()

vip_guests.difference_update(guests_at_party)
regular_guests.difference_update(guests_at_party)
print(len(vip_guests) + len(regular_guests))
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]
