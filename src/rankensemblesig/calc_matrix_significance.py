def calc_matrix_significance(ranks_mat):
    def format_input(ranks_mat):
        if isinstance(ranks_mat, pd.DataFrame):
            ranks_mat = np.array(ranks_mat)
        if set(ranks_mat[:,0].ravel())==set(range(1,np.max(ranks_mat)+1)):
            return ranks_mat
        elif set(ranks_mat[0,:].ravel())==set(range(1,np.max(ranks_mat)+1)):
            return ranks_mat.T
        else:
            print("Error, input matrix does not appear to consist of ranks")
            sys.exit()
    ranks_mat = format_input(ranks_mat)
    pvalues = []
    for col in range(ranks_mat.shape[0]):
        max_rank = np.max(ranks_mat)
        pvalues.append(calc_rank_ensemble_pvalue(np.array(ranks_mat[col,:]), max_rank))
    return(pvalues)
