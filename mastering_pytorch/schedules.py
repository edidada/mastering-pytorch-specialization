"""Learning-rate schedules used across the three courses."""

import math


def step_lr(base_lr, epoch, step_size, gamma=0.1):
    """Drop the learning rate by ``gamma`` every ``step_size`` epochs."""
    if step_size <= 0:
        raise ValueError("step_size must be positive")
    return base_lr * (gamma ** (epoch // step_size))


def cosine_lr(base_lr, epoch, total_epochs, min_lr=0.0):
    """Cosine annealing from ``base_lr`` down to ``min_lr``."""
    if total_epochs <= 0:
        raise ValueError("total_epochs must be positive")
    progress = min(max(epoch, 0), total_epochs) / total_epochs
    return min_lr + 0.5 * (base_lr - min_lr) * (1 + math.cos(math.pi * progress))
