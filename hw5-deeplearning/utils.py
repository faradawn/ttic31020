import numpy as np

# For gradient check
def relative_error(x, y, h):
    h = h or 1e-12
    if type(x) is np.ndarray and type(y) is np.ndarray:
        top = np.abs(x - y)
        bottom = np.maximum(np.abs(x) + np.abs(y), h)
        return np.amax(top/bottom)
    else:
        return abs(x - y) / max(abs(x) + abs(y), h)

def numeric_gradient(f, x, df, eps):
    df = df or 1.0
    eps = eps or 1e-8
    n = x.size
    x_flat = x.reshape(n)
    dx_num = np.zeros(x.shape)
    dx_num_flat = dx_num.reshape(n)
    for i in range(n):
        orig = x_flat[i]
    
        x_flat[i] = orig + eps
        pos = f(x)
        if type(df) is np.ndarray:
            pos = pos.copy()
    
        x_flat[i] = orig - eps
        neg = f(x)
        if type(df) is np.ndarray:
            neg = neg.copy()

        d = (pos - neg) * df / (2 * eps)
        
        dx_num_flat[i] = d
        x_flat[i] = orig
    return dx_num

#Criterion for testing the modules
class TestCriterion(object):
    def __init__(self):
        return
        
    def forward(self, _input, _target):
        self._input = _input
        return np.mean(np.sum(np.abs(_input), 1))
    
    def backward(self, _target):
        self._gradInput = np.sign(self._input) / len(self._input)
        return self._gradInput
        
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
