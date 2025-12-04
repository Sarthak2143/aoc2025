with open("input.txt", "r", encoding="utf-8") as f:
  data: list[str] = f.readlines()

count: int = 0
point: int = 50
temp: int = 0

for d in data:
  print(f"{d.strip()} -> {point}")
  move: str = d[0]
  steps: int = int(d[1:])
  if move == "L":
    temp = 99
  else:
    temp = 1
  for i in range(steps):
    point = (point + temp) % 100
    if point == 0:
      count += 1

print(count)
