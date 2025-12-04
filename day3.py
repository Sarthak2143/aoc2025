def part1(data: list[str]) -> None:
  sum_jolt: int = 0
  for d in data:
    d_str: str = d.strip()
    maxm: int = 0
    max_i: int = 0
    for i in range(len(d_str)):
      if int(d_str[i]) > maxm:
        maxm = int(d_str[i])
        max_i = i
    secondMaxm: int = 0

    if max_i == len(d_str) - 1:
      # its in the rightmost, find largest num till max_i
      for i in range(max_i):
        if int(d_str[i]) > secondMaxm:
          secondMaxm = int(d_str[i])
      sum_jolt += secondMaxm * 10 + maxm

    else:
      # there is still some space in right
      for i in range(max_i + 1, len(d_str)):
        if int(d_str[i]) > secondMaxm:
          secondMaxm = int(d_str[i])
      sum_jolt += maxm * 10 + secondMaxm

  print(sum_jolt)


def part2(data: list[str]) -> None:
  sum_jolt: int = 0
  for d in data:
    d_str: str = d.strip()
    # no of digits we need to remove
    lenRem: int = len(d_str) - 12
    digitsFound: int = 0
    number: int = 0
    maxmPosn: int = 0
    while digitsFound != 12:
      dataFn: tuple[int, int] = maxString(d_str[maxmPosn : maxmPosn + lenRem + 1])
      maxmPosn += dataFn[1] + 1
      number = number * 10 + dataFn[0]
      digitsFound += 1
      lenRem = len(d_str) - maxmPosn - (12 - digitsFound)
    sum_jolt += number

  print(sum_jolt)


def maxString(string: str) -> tuple[int, int]:
  maxm: int = 0
  maxm_i: int = 0
  for i in range(len(string)):
    if int(string[i]) > maxm:
      maxm = int(string[i])
      maxm_i = i
  return maxm, maxm_i


def main() -> None:
  with open("input.txt", "r", encoding="utf-8") as f:
    data: list[str] = f.readlines()

  print("part1:")
  part1(data)
  print("part2:")
  part2(data)


if __name__ == "__main__":
  main()
