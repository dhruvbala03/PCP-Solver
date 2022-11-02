class Domino:

  def __init__(self, top, bottom):
    self.top = top
    self.bottom = bottom


def print_path(path):
  print("PATH:")
  for domino in path:
    print("\t" + domino.top + " | " + domino.bottom)


def find_match(dominos):
  queue = []
  queue.extend([([d], d.top, d.bottom) for d in dominos])

  while queue:
    n = queue.pop(0)
    path = n[0]
    top_string = n[1]
    bottom_string = n[2]

    if (top_string == bottom_string) and (path != []):
      print("Match found!\n")
      print_path(path)
      return

    for d in dominos:
      top_p = top_string + d.top
      bottom_p = bottom_string + d.bottom
      if (top_p in bottom_p) or (bottom_p in top_p):
        tup = (path + [d], top_p, bottom_p)
        queue.append(tup)

#########################################################

# USAGE:

dominos = [
  Domino("ab", "abab"),
  Domino("b", "a"),
  Domino("aba", "b"),
  Domino("aa", "a")
]

find_match(dominos)

# OUTPUT:
## Match found!
## PATH:
##     aa | a
##     aa | a
##     b | a
##     ab | abab