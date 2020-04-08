# GPU support in spaCy

For GPU support, you must install package `spacy[cuda100]` ([must match CUDA version](https://docs-cupy.chainer.org/en/stable/install.html#install-cupy))
for wheel distribution or `spacy[cuda]` to compile it from source.

- [Run spaCy with GPU](https://spacy.io/usage#gpu)
- [What do square brackets mean in pip install?](https://stackoverflow.com/q/46775346/95)

## Summary

**All attempts to enable the GPU support on my laptop failed**, because I have `Intel UHD Graphics 620` and not an Nvidia card.
I don't know why I was able to install the CUDA Toolkit at all - one of the initial steps of the setup process was checking
the card compatibility and I would expect it to be interrupted then.

To my best knowledge though, the steps below are valid and will install spaCy with GPU support, if you have proper hardware.

## Windows 10

1. Install C++ compiler from Microsoft (e.g. [VS 2019 Community](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017);
   it may be unnecessary, since I trying to use the wheel distribution for all packages)
2. Install [CUDA Toolkit 10.0](https://developer.nvidia.com/cuda-downloads) (not 10.2, because _WARNING: spacy 2.2.4 does not provide the extra 'cuda102'_)
3. Reboot
4. `conda env create -f environment-gpu.yml`

In case of errors:

1. confirm that the version of installed package `cupy-cudaXXX` matches CUDA Toolkit version (e.g. `cupy-cuda102` for version 10.2)
2. read carefully the output of `python -c "import cupy; cupy.show_config()"`; it contains useful tips
3. uninstall CuPy, install in verbose mode (`pip install cupy --no-cache-dir -vvvv`) and check the output

## WSL

`spacy[cuda]` cannot be installed using WSL, because [WSL is not able to access the host GPU](https://github.com/Microsoft/WSL/issues/3847).

```bash
Modules:
  cuda      : No
    -> Cannot link libraries: ['cublas', 'cuda', 'cudart', 'cufft', 'curand', 'cusparse', 'nvrtc']
    -> Check your LDFLAGS environment variable.

ERROR: CUDA could not be found on your system.
```

BTW, Zsh did not recognize the package name with brackets, but escaping them helped (`pip install spacy\[cuda\]`).

## CUDA packages in the Anaconda repository

Important note from [CuPy installation guide](https://docs-cupy.chainer.org/en/stable/install.html):

> If you are installing CuPy on Anaconda environment, also make sure
> that the following packages are **not installed**:
>
> - cudatoolkit
> - cudnn
> - nccl
