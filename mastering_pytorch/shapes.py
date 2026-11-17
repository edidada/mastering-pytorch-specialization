"""Output-shape helpers mirroring PyTorch's ``nn.Conv2d`` and pooling layers.

Handy when sketching a CNN on paper before writing the actual model.
"""


def _pair(value):
    return (value, value) if isinstance(value, int) else tuple(value)


def conv2d_output_shape(in_h, in_w, kernel_size, stride=1, padding=0, dilation=1):
    """Return ``(out_h, out_w)`` for a 2D convolution.

    Mirrors the shape formula used by ``torch.nn.Conv2d``::

        out = floor((in + 2*padding - dilation*(kernel-1) - 1) / stride) + 1
    """
    kh, kw = _pair(kernel_size)
    sh, sw = _pair(stride)
    ph, pw = _pair(padding)
    dh, dw = _pair(dilation)

    eff_kh = dh * (kh - 1) + 1
    eff_kw = dw * (kw - 1) + 1
    out_h = (in_h + 2 * ph - eff_kh) // sh + 1
    out_w = (in_w + 2 * pw - eff_kw) // sw + 1

    if out_h <= 0 or out_w <= 0:
        raise ValueError("kernel/padding/stride combination yields a non-positive output")
    return out_h, out_w


def pool2d_output_shape(in_h, in_w, kernel_size, stride=None, padding=0):
    """Return ``(out_h, out_w)`` for a 2D pooling layer.

    ``stride`` defaults to ``kernel_size``, matching ``nn.MaxPool2d``.
    """
    if stride is None:
        stride = kernel_size
    return conv2d_output_shape(in_h, in_w, kernel_size, stride=stride, padding=padding)
