"""Runnable smoke demo for the framework-free companion code.

Invoked by the CI workflow as the "run" stage; no PyTorch install required.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mastering_pytorch import (  # noqa: E402
    conv2d_output_shape,
    cosine_lr,
    pool2d_output_shape,
    step_lr,
)


def main():
    print("Mastering PyTorch specialization - core smoke demo")
    print("conv2d(32x32, k=3, s=1, p=1) ->", conv2d_output_shape(32, 32, 3, stride=1, padding=1))
    print("maxpool(32x32, k=2)          ->", pool2d_output_shape(32, 32, 2))
    print("step_lr @ epoch 10           ->", round(step_lr(0.1, 10, 10), 4))
    print("cosine_lr @ epoch 50/100     ->", round(cosine_lr(0.1, 50, 100), 4))
    print("OK: compile, import and run succeeded")


if __name__ == "__main__":
    main()
