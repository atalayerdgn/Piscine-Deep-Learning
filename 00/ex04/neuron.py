import torch
import torch.nn as nn

def neuron(x: torch.Tensor) -> torch.Tensor:
    linear = nn.Linear(3,1)
    linear.weight = torch.nn.Parameter(torch.tensor([[0.1, 0.2, 0.3]]))
    linear.bias   = torch.nn.Parameter(torch.tensor([0.]))
    z = linear(x)
    return torch.sigmoid(z)


