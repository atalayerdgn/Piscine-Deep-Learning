import torch


def manual_grads(x: float, w: float, b: float) -> float:
    """
    the function compute a derivative of y = (wx + b)^2
    args:
        x -> float
        w -> float
        b -> float
    returns:
        float
    """
    u = w * x + b
    dy_du = 2 * u
    dy_dx = dy_du * w
    dy_dw = dy_du * x
    dy_db = dy_du
    return dy_dx, dy_dw, dy_db


def autograd_grads(x: float, w: float, b: float) -> float:
    """
    the function compute a derivative of (wx + b)^2
    args:
        x -> float
        w -> float
        b -> float
    """
    x = torch.tensor(float(x), requires_grad=True)
    w = torch.tensor(float(w), requires_grad=True)
    b = torch.tensor(float(b), requires_grad=True)
    y = (w * x + b) ** 2
    y.backward()
    return x.grad.item(), w.grad.item(), b.grad.item()


if __name__ == "__main__":
    x, w, b = 2.0, 3.0, 1.0
    y = (w * x + b) ** 2
    print(f"x={x} w={w} b={b} -> y={y}")

    _, gdw, gdb = manual_grads(x, w, b)
    print(f"Manual   : dy/dw={gdw} dy/db={gdb}")

    _, adw, adb = autograd_grads(x, w, b)
    print(f"Autograd : dy/dw={adw} dy/db={adb}")
    t1 = torch.isclose(torch.tensor(gdw), torch.tensor(adw))
    t2 = torch.isclose(torch.tensor(gdb), torch.tensor(adb))
    print("Match:", (t1 and t2).item())
