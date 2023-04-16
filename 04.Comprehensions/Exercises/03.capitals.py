pairs = {country: capital for country, capital in zip(input().split(', '), input().split(', '))}
[print(f"{key} -> {value}") for key, value in pairs.items()]
