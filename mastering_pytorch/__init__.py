"""Course companion code for the Mastering PyTorch specialization.

These helpers are deliberately framework-free (standard library only) so that
CI can compile, import and run them without installing PyTorch.
"""

from .schedules import cosine_lr, step_lr
from .shapes import conv2d_output_shape, pool2d_output_shape

__all__ = [
    "conv2d_output_shape",
    "pool2d_output_shape",
    "step_lr",
    "cosine_lr",
]
