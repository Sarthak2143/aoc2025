def part_1(data: list[str]) -> None:
  sum_invalid: int = 0

  for d in data:
    first_num: int = int(d.split("-")[0])
    second_num: int = int(d.split("-")[1])
    for num in range(first_num, second_num + 1):
      num_str: str = str(num)
      # check for leading zero
      if num_str[0] == "0":
        sum_invalid += num
      # check for repetition
      if len(num_str) % 2 == 0:
        if num_str[0 : len(num_str) // 2] == num_str[len(num_str) // 2 : len(num_str)]:
          sum_invalid += num

  print(sum_invalid)


def part_2(data: list[str]) -> None:
  sum_invalid: int = 0

  for d in data:
    first_num: int = int(d.split("-")[0])
    second_num: int = int(d.split("-")[1])
    for num in range(first_num, second_num + 1):
      num_str: str = str(num)
      if checkRep(num_str):
        sum_invalid += num

  print(sum_invalid)


def checkRep(text: str) -> bool:
  # idea: divide the text into n pieces where n is factor of len(text) and check if each of em is equal
  facts: list[int] = []
  for n in range(2, len(text) + 1):
    if len(text) % n == 0:
      facts.append(n)
  for fact in facts:
    reps: list[str] = []
    for i in range(0, len(text), len(text) // fact):
      reps.append(text[i : i + len(text) // fact])
    all_eq: bool = True
    for i in range(len(reps) - 1):
      if reps[i] != reps[i + 1]:
        all_eq = False
    if all_eq:
      return True
  return False


def main() -> None:
  with open("input.txt", "r", encoding="utf-8") as f:
    data: list[str] = f.read().strip().split(",")

  print("part_1:")
  part_1(data)
  print("part_2:")
  part_2(data)


if __name__ == "__main__":
  main()
