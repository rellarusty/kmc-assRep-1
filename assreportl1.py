# Assessment Report L1
# Control system program; production system

# The Queue
A = 19
B = 26
C = 23
D = 4
E = 78
F = 90
G = 32
H = 54
I = 32
J = 12
K = 67
L = 90
M = 87
N = 6
O = 36
P = 12
Q = 24

queue = []
queue.extend((A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q))

def entrance_function(queue_list):
  entry_list = []
  denied_list = []

  ordered_queue = sorted(queue_list, reverse = True)

  for each in ordered_queue:
    if each == 90:
      denied_list.append(each)
    elif each >= 18:
      entry_list.append(each)
    else:
      denied_list.append(each)

  return(entry_list, denied_list)

test_1, test_2 = entrance_function(queue)

print(test_1)
print(test_2)
