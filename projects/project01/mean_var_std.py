import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    x = np.array(list).reshape(3, 3)

    dict = {
        'mean': [x.mean(0), x.mean(1), x.mean()],
        'variance': [x.var(0), x.var(1), x.var()],
        'standard deviation': [x.std(0), x.std(1), x.std()],
        'max': [x.max(0), x.max(1), x.max()],
        'min': [x.min(0), x.min(1), x.min()],
        'sum': [x.sum(0), x.sum(1), x.sum()]
    }

    dict = {
        key: [value.tolist() for value in values]
        for key, values in dict.items()
    }

    return dict