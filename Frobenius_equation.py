def solvefrob(coefs, b):
  '''Function to find solution of the Frobenius equation (Diophantine equation)'''
  import numpy as np
  assert isinstance(b,int)
  assert isinstance(coefs,list)
  for a in coefs:
    assert isinstance(a,int)
    assert a>=0

  final_output = np.zeros((1,1))
 
  final_sum_range = np.arange(b+1)
  for coefficient in coefs:
    column = coefficient*final_sum_range
    final_output = final_output + column
    final_sum_range = final_sum_range[:,None]

 # filtering out the values where sum is equal to the b
  equation_solutions = []
  final_filtered_array = np.array(np.where(final_output ==b))
  final_filtered_array = np.transpose(final_filtered_array)# Transpose the solution matrix
  size = final_filtered_array.shape[0] - 1
  for i in range(size, -1, -1):
    solution = final_filtered_array[i, :]
    equation_solutions.append(tuple(np.flip(solution,0)))#flipping the matrix for solutions

  return equation_solutions
