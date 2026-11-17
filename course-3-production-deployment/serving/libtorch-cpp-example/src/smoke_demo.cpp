#include <torch/torch.h>

#include <cmath>
#include <cstdlib>
#include <iostream>

int main() {
  // Minimal stand-in for a Course-3 exported module: one linear layer.
  torch::nn::Linear fc(/*in_features=*/4, /*out_features=*/3);
  torch::Tensor input = torch::randn({2, 4});
  torch::Tensor output = fc->forward(input);

  std::cout << "LibTorch C++ smoke demo\n"
            << "  input  : " << input.size(0) << " x " << input.size(1) << "\n"
            << "  output : " << output.size(0) << " x " << output.size(1) << "\n"
            << "  sum    : " << output.sum().item<double>() << "\n";

  if (output.dim() != 2 || output.size(0) != 2 || output.size(1) != 3) {
    std::cerr << "unexpected output shape\n";
    return EXIT_FAILURE;
  }
  if (!std::isfinite(output.sum().item<double>())) {
    std::cerr << "output contains non-finite values\n";
    return EXIT_FAILURE;
  }

  std::cout << "OK: C++ compiled against LibTorch and ran successfully\n";
  return EXIT_SUCCESS;
}
