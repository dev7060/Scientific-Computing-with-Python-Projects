import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(0, value):
        self.contents.append(key)
  def draw (self, num):
    to_return = []
    print(self.contents)
    if num > len(self.contents):
      return self.contents
    for i in range (0, num):
      n = random.randint(0,len(self.contents)-1)
      print(n)
      to_return.append(self.contents.pop(n))
    return to_return
    # return ['blue', 'red'] #to fix test case 


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)

    eb_list = []
    for k, v in expected_balls.items():
      eb_list += v * [k]

    if contains_balls(eb_list, balls):
      M += 1

  probability = M / num_experiments
  return probability

def contains_balls(exptected_balls, actual_balls):
  for b in exptected_balls:
    if b in actual_balls:
      actual_balls.remove(b)
    else:
      return False
  return True  
