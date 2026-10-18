import torch


def gradient_at(value: float) -> float:
    """
    the function compute a derivative of 3x^2 + 2x + 1
    args:
        value -> float
    returns:
        float
    """
    x = torch.tensor(value, requires_grad=True)
    y = (3 * (x ** 2)) + (2 * x) + 1
    y.backward()
    return x.grad


def main():
    value = 3.0
    grad_autograd = gradient_at(value)
    grad_analytical = (6 * value) + 2
    print(f"f'({value:.0f}) computed by autograd : {grad_autograd}")
    print(f"f'({value:.0f}) analytical (6x+2) : {grad_analytical}")
    if grad_autograd == grad_analytical:
        print("Match: True")
    else:
        print("Match: False")


if __name__ == '__main__':
    main()
