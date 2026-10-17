import torch


def describe(x: "torch.Tensor") -> None:
    """
    To give some informations about the tensor like shape, dimensions
    values etc.
    Args : x {torch.Tensor}
    Returns : None
    """
    print(f"Values :\n {x}")
    print(f"Shape : {x.shape}")
    print(f"Dimensions : {x.shape[0]}")
    print(f"Dtype : {x.dtype}")
    print(f"Device : {x.device}")
