class Enhancer():
  def __init__(self):
    self.algorithm = '##..##...#..#.#...#.....##....#.#..#.#.####...#####..#.######...#......#.##.#..######.########....#.#..##.####.##...##..#.########.#.##..........##.######.#......#..#...##..#..#.###.#.#..#..#...##.###.....#.#.###..##.####....##.#....#.#.###..###.....####..###..##.#.#..##....#.#....#####.##.....#.#.#..###..#.....####..##.#..#.###....#...##..###.#.###.##.####..#.##......##.##.#.##..##...##..######..####.#.##..###..###.###.##.##..###..#.......##.#######.#..##..##.###.#.#.#.####...####..#.#.#.......##.##.#.....'
    
    file = open('12-20.txt')
    self.img = [line.strip() for line in file.readlines()]
    self.void = '.'

  def swap_void(self):
    if self.void == '.':
      self.void = '#'
    else:
      self.void = '.'

  def access(self, i, j):
    if i >= len(self.img) or j >= len(self.img[0]):
      ch = self.void
    elif i < 0 or j < 0:
      ch = self.void
    else:
      ch = self.img[i][j]

    return '0' if ch == '.' else '1'

  def find_index(self, x, y):
    bit_string = ''.join([
      self.access(i, j)
      for i in range(x-1, x+2)
      for j in range(y-1, y+2)
    ])
    return int(bit_string, 2)

  def enhance(self):
    result = []
    for i in range(-1, len(self.img) + 2):
      line = ''
      for j in range(-1, len(self.img[0]) + 2):
        line += self.algorithm[self.find_index(i, j)]
      result.append(line)
    self.img = result

    if self.algorithm[0] == '#' and self.algorithm[-1] == '.':
      self.swap_void()

  def light_count(self):
    return '\n'.join(self.img).count('#')
 
if __name__=='__main__':
  enhancer = Enhancer()

  for _ in range(50):
    enhancer.enhance()
  
  print(enhancer.light_count())

