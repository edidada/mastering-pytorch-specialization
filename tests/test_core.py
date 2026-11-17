import unittest

from mastering_pytorch import (
    conv2d_output_shape,
    cosine_lr,
    pool2d_output_shape,
    step_lr,
)


class TestShapes(unittest.TestCase):
    def test_conv2d_same_padding(self):
        self.assertEqual(conv2d_output_shape(32, 32, 3, stride=1, padding=1), (32, 32))

    def test_conv2d_valid_stride(self):
        self.assertEqual(conv2d_output_shape(32, 32, 3, stride=2, padding=1), (16, 16))

    def test_pool2d_default_stride(self):
        self.assertEqual(pool2d_output_shape(32, 32, 2), (16, 16))

    def test_invalid_combination_raises(self):
        with self.assertRaises(ValueError):
            conv2d_output_shape(4, 4, 8)


class TestSchedules(unittest.TestCase):
    def test_step_lr(self):
        self.assertAlmostEqual(step_lr(0.1, 0, 10, 0.1), 0.1)
        self.assertAlmostEqual(step_lr(0.1, 10, 10, 0.1), 0.01)

    def test_cosine_lr_endpoints(self):
        self.assertAlmostEqual(cosine_lr(0.1, 0, 100), 0.1)
        self.assertAlmostEqual(cosine_lr(0.1, 100, 100), 0.0)

    def test_cosine_lr_invalid_total(self):
        with self.assertRaises(ValueError):
            cosine_lr(0.1, 0, 0)


if __name__ == "__main__":
    unittest.main()
