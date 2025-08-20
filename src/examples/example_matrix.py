from rankensemblesig import calc_matrix_significance
import numpy as np

def main():
  test_dat = np.array([[1,2,3, 4], [2,1,3, 4], [1,3,4,2]])
  print("Test matrix: " + str(test_dat))
  print(calc_rank_ensemble_pvalue(test_dat))
