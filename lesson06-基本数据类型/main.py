import torch
import numpy as np

if __name__ == "__main__":
    a = torch.randn(2,3)
    b = torch.tensor(1.3)
    c = torch.tensor([1.1])
    print(a)
    print(a.type())
    print(type(a))
    print(b.shape)
    print(b.size())
    print(c.type())

    data = np.ones(2)
    data_torch = torch.from_numpy(data)

    d = torch.ones(2)
    print(data)
    print(data_torch.type())

    print(d)
    print(d.shape,d.type())