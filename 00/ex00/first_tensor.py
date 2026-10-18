import torch


def describe(x: "torch.Tensor") -> None:
    """
    To give some informations about the tensor like shape, dimensions
    values etc.
    Args : x {torch.Tensor}
    Returns : None
    """
    print(f"Values :\n {x}") # To print Values of Tensor.
    print(f"Shape : {x.shape}") # To print shape like row and column count of given Tensor.
    print(f"Dimensions : {x.shape[0]}") # To print dimensions of given Tensor.
    print(f"Dtype : {x.dtype}") # To print given Tensor's data-type
    print(f"Device : {x.device}") # To print device of given Tensor.
