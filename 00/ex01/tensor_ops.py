import torch


def sum_(a: torch.Tensor, b: torch.Tensor) -> str:
    """
    To multiply given tensors using Torch library.
    args :
            a -> torch.Tensor
            b -> torch.Tensor
    returns :
            str
    """
    return f"Sum :\n {torch.add(a, b)}\n"


def product_matrix(a: torch.Tensor, b: torch.Tensor) -> str:
    """
    To product given tensors using @ operator or torch.mathmul
    args :
            a -> torch.Tensor
            b -> torch.Tensor
    returns :
            str
    """
    output = f"Matmul : \n {torch.matmul(a, b)} \n"
    if a.shape == b.shape:
        return output
    else:
        raise AssertionError


def mean_(a: torch.Tensor) -> str:
    """
    To print given tensor's mean value
    args :
            a -> torch.Tensor
    returns :
            str
    """
    if a.dtype is not torch.is_floating_point:
        a = a.to(torch.float64)
    return f"Mean of a : {torch.mean(a)}\n"


def flatten(a: torch.Tensor) -> str:
    """
    To convert a tensor to 1 dimension tensor.
    args :
            a -> torch.Tensor
    returns :
            str
    """
    return f"Reshaped a: {a.reshape(1, (a.shape[0] * a.shape[1]))}"


def operations(a: torch.Tensor, b: torch.Tensor) -> tuple:
    """
    all the functions mixed in a one function.
    args :
            a -> torch.Tensor
            b -> torch.Tensor
    returns :
            tuple
    """
    txt1 = sum_(a, b)
    txt2 = product_matrix(a, b)
    txt3 = mean_(a)
    txt4 = flatten(a)
    return txt1 + txt2 + txt3 + txt4

# a = torch.tensor([[1,2],[3,4]])
# b = torch.tensor([[5,6],[7,8]])
# print(operations(a,b))
