import torch
import torch.nn as nn


class MLP(nn.Module):

    
    def __init__(self, in_features: int, hidden: int, out_features: int):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(in_features, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_features)
        )


    def forward(self, x: "torch.Tensor") -> "torch.Tensor":
        return self.layers(x)

