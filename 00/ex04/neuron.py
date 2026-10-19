import torch
import torch.nn as nn


linear = nn.Linear(3, 1)
linear.weight = torch.nn.Parameter(torch.tensor([[0.1, 0.2, 0.3]]))
linear.bias = torch.nn.Parameter(torch.tensor([0.]))


def neuron(x: torch.Tensor) -> torch.Tensor:
    """
    To create neuron with torch.Tensor
    args:
        x -> torch.Tensor
    returns:
        torch.Tensor
    """
    z = linear(x)
    return torch.sigmoid(z)


if __name__ == "__main__":
    x = torch.tensor([1., 2., 3.])
    print(f"Input : {x}")
    print(f"Weights: {linear.weight}")
    print(f"Bias : {linear.bias}")
    print(f"Output : {neuron(x)}")
