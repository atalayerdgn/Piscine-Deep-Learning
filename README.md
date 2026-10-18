# Piscine Deep Learning

* *This project aims to improve deep learning skills. I've learning how to use deep learning concepts like tensors etc.*

## Keywords

- **Tensors** 
   
   A PyTorch Tensor is the core data structure — an n-dimensional array (like a NumPy array) that can run on GPU and track gradients. If you know NumPy, tensors will feel familiar; the main differences are GPU support and requires_grad for automatic differentiation.

    ## Key facts
    ▸ 
    Tensors are multi-dimensional arrays: scalars (0-D), vectors (1-D), matrices (2-D), and 
    beyond.

    ▸ 
    Created via torch.tensor(), torch.zeros(), torch.ones(), torch.rand(), torch.arange(), torch.linspace().

    ▸ 
    Two key properties: shape (dimensions) and dtype (data type: float32, int64, etc.).

    ▸ 
    Device matters: tensors live on CPU or GPU (cuda, mps). Use .to(device) or tensor.cuda() to move them.
    ▸ 

    `requires_grad=True` enables autograd — PyTorch tracks operations to compute gradients via .backward().

    ▸ 
    Operations come in two flavors: tensor.add(x) (new tensor) and tensor.add_(x) (in-place, marked with _).

    ▸ 
    Tensor vs NumPy: they share memory when converted (torch.from_numpy(), .numpy()), so changes affect both.
    
- **Devices**
    * PyTorch runs computations on "devices" — typically cpu or cuda (NVIDIA GPU). Every tensor and model lives on exactly one device; mixing devices in one operation raises a RuntimeError. Core APIs: torch.device(), .to(), .cuda(), torch.cuda.is_available().
    ## Key facts
    
    ▸
    Device objects: torch.device('cpu'), torch.device('cuda'), torch.device('cuda:0') (specific GPU index on multi-GPU machines).

    ▸
    Check availability: torch.cuda.is_available() → True if an NVIDIA GPU with proper drivers + CUDA build is present.

    **Recommended idiom**:
    ```python

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = model.to(device)

    inputs, labels = inputs.to(device), labels.to(device)

    ```