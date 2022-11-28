import numpy as np

# Load data
def load_data(dataset):

    dataset2 = dataset
    if dataset2 == 'kaggle':
        dataset='Te'

    X = np.load('./x'+dataset+'.npy')
    N = X.shape[0]
    if dataset2 != 'kaggle':
        Y = np.load('./y'+dataset+'.npy')
        return X, Y
    else:
        return X

# Save kaggle submission
def save_submission(filename, yhats):
    assert np.ndim(yhats) == 1
    id_and_prediction = np.vstack([np.arange(len(yhats)).T, yhats]).T
    np.savetxt(filename, id_and_prediction,
               fmt='%d',
               delimiter=',',
               comments='',
               header='id,label')
    print("Saved:", filename)
