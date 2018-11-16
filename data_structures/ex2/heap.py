from random import randint

def heapsort(arr):
  heap = Heap()
  result = []
  while len(arr) > 0:
    heap.insert(arr.pop())
  
  while heap.get_size() > 0:
    result.append(heap.delete())

  result.reverse()
  return result


class Heap:
  def __init__(self):
    self.storage = []
  def __str__(self):
    rv = "Heap:\n"

    l = 1
    c = 0

    for i in range(len(self.storage)):
      rv += str(self.storage[i]) + "  "

      c += 1

      if c >= l:
        rv += "\n" + "  " * l
        c = 0
        l *= 2

    rv += "\n"

    return rv

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2


# tests:
# def gen_random_input(length, max):
#   input = []
#   for i in range(length):
#     input.append(randint(0, max))
#   return input

# def is_sorted(arr):
#   for i in range(len(arr) - 1):
#     if arr[i] > arr[i+1]:
#       print(arr[i],arr[i+1])
#       return False
#   return True
# length = randint(100, 1000)
# input = gen_random_input(length, 1000)
# output = heapsort(input)
# is_sorted(output)

# print(output)

# self.assertEqual(len(output), length)
# self.assertTrue(is_sorted(output))