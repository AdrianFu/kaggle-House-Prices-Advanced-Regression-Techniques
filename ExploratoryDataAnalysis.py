import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch

class ExploratoryDataAnalysis:
    #def __init__(self, train_val_X, train_val_y):
    #    self.train_val_X = train_val_X
    #    self.train_val_y = train_val_y

    def DuplicatedRows(self):
        return self.train_val_X.duplicated()

    def cluster_corr(self, corr_array, inplace=False):
        """
        Rearranges the correlation matrix, corr_array, so that groups of highly
        correlated variables are next to eachother

        Parameters
        ----------
        corr_array : pandas.DataFrame or numpy.ndarray
            a NxN correlation matrix 

        Returns
        -------
        pandas.DataFrame or numpy.ndarray
            a NxN correlation matrix with the columns and rows rearranged
        """
        pairwise_distances = sch.distance.pdist(corr_array)
        linkage = sch.linkage(pairwise_distances, method='complete')
        cluster_distance_threshold = pairwise_distances.max()/2
        idx_to_cluster_array = sch.fcluster(linkage, cluster_distance_threshold,
            criterion='distance')
        idx = np.argsort(idx_to_cluster_array)

        if not inplace:
            corr_array = corr_array.copy()

        if isinstance(corr_array, pd.DataFrame):
            return corr_array.iloc[idx, :].T.iloc[idx, :]
        return corr_array[idx, :][:, idx]

EDA = ExploratoryDataAnalysis()