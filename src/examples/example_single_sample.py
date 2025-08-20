from rankensemblesig import calc_rank_ensemble_pvalue
import numpy as np

def main():
  ranks = np.array([1,1,2,2])
  print("Example ranks: " + str(ranks))
  print(calc_rank_ensemble_pvalue(ranks, 4))
