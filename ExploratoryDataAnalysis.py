class ExploratoryDataAnalysis:
    #def __init__(self, train_val_X, train_val_y):
    #    self.train_val_X = train_val_X
    #    self.train_val_y = train_val_y

    def DuplicatedRows(self):
        return self.train_val_X.duplicated()

EDA = ExploratoryDataAnalysis()