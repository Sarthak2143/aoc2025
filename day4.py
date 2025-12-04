def part1(data: list[list[str]]) -> tuple[int, list[list[int]]]:
  total: int = 0
  indices: list[list[int]] = []
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data[i][j] != "@":
        continue
      li: list[str] = []
      if i > 0:
        li.append(data[i - 1][j])
        if j > 0:
          li.append(data[i - 1][j - 1])
        if j < len(data[i]) - 1:
          li.append(data[i - 1][j + 1])
      if i < len(data) - 1:
        li.append(data[i + 1][j])
        if j > 0:
          li.append(data[i + 1][j - 1])
        if j < len(data[i]) - 1:
          li.append(data[i + 1][j + 1])
      if j > 0:
        li.append(data[i][j - 1])
      if j < len(data[i]) - 1:
        li.append(data[i][j + 1])
      if count(li) < 4:
        total += 1
        indices.append([i, j])
  return total, indices


def part2(data: list[list[str]]) -> int:
  totalVal: int = 0
  while True:
    total, indices = part1(data)
    if total == 0:
      break
    totalVal += total
    for indice in indices:
      i: int = indice[0]
      j: int = indice[1]
      data[i][j] = "."
  return totalVal


def count(li: list[str]) -> int:
  c: int = 0
  for ch in li:
    if ch == "@":
      c += 1
  return c


def main() -> None:
  with open("input.txt", "r", encoding="utf-8") as f:
    data: list[str] = f.readlines()

  dataLi: list[list[str]] = []
  for d in data:
    li: list[str] = []
    for di in d:
      li.append(di)
    dataLi.append(li)

  print(f"part1: {part1(dataLi)[0]}")
  print(f"part2: {part2(dataLi)}")


if __name__ == "__main__":
  main()
