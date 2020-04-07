# COVID-19 Open Research Dataset Challenge (CORD-19)

Kaggle challenge: [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Task: [What do we know about COVID-19 risk
factors?](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/tasks?taskId=558)

## Dataset citation

COVID-19 Open Research Dataset (CORD-19). 2020. Version 2020-03-13.
Retrieved from https://pages.semanticscholar.org/coronavirus-research.
Accessed 2020-03-26. doi:10.5281/zenodo.3715506

## Prodigy

### Annotations

```bash
# manual annotation with suggestions from patterns
# https://prodi.gy/docs/named-entity-recognition#manual-patterns
prodigy ner.manual cord_19_abstracts en_core_web_lg data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RISK_FACTOR.jsonl

# accept or reject suggestions from patterns
# https://prodi.gy/docs/recipes#match
prodigy match cord_19_abstracts_match models/en_core_web_lg_no_ner data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RF_list_2020.03.17.20037572.jsonl --label-span

# manual annotation with suggestions from patterns and existing model in the loop
# https://prodi.gy/docs/recipes#ner-teach
prodigy ner.teach cord_19_abstracts_teach models/2020_03_28_match/en_rf_web_lg data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RF_list_2020.03.17.20037572.jsonl
```

### Training

```bash
# train model
prodigy train ner cord_19_abstracts_match models/en_core_web_lg_no_ner --output models/2020_03_28_match/en_rf_web_lg
```

### Other

```bash
# save annotations to a file
prodigy db-out cord_19_abstracts > data/annotated/cord_19_abstracts.jsonl
```

### Misc

1. [When to reject when annotating text for NER?](https://support.prodi.gy/t/when-to-reject-in-ner-manual-or-ner-make-gold/892/2)
1. [When should I press accept, reject or ignore?](https://prodi.gy/docs/named-entity-recognition#manual-accept-reject)
(never - accept both highlights and samples with no spans)
1. [`batch-train` is deprecated](https://prodi.gy/docs/recipes#deprecated)

## Raw data filtering

```bash
fgrep "risk factor" data/raw/cord_19_abstracts.jsonl > data/raw/cord_19_abstracts_filtered.jsonl
```

## GPU support in spaCy

For GPU support, you must install package `spacy[cuda100]` ([must match CUDA version](https://docs-cupy.chainer.org/en/stable/install.html#install-cupy))
for wheel distribution or `spacy[cuda]` to compile it from source.

- [Run spaCy with GPU](https://spacy.io/usage#gpu)
- [What do square brackets mean in pip install?](https://stackoverflow.com/q/46775346/95)

### Windows 10

```bash
conda env create -f environment-gpu.yml
```

#### Windows 10 (failed attempt)

In theory, this method should work. However, CuPy could not get installed properly, so I decided to downgrade to CUDA 10 and
install the Toolkit as part of the Conda environment (see `environment-gpu.yml`).

1. Install C++ compiler from Microsoft
   (e.g. [VS 2019 Community](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017))
2. Install [CUDA Toolkit 10.2](https://developer.nvidia.com/cuda-downloads)
3. Reboot
4. `conda activate cord-19-env`
5. `pip install -U spacy[cuda]`
    - I tried `spacy[cuda102]`, but got _WARNING: spacy 2.2.4 does not provide the extra 'cuda102'_

In case of errors:

1. confirm that the version of installed package `cupy-cudaNNN` matches CUDA Toolkit version (e.g. `cupy-cuda102` for version 10.2)
2. read carefully the output of `python -c "import cupy; cupy.show_config()"`; it contains useful tips
3. uninstall CuPy and install with `pip install cupy --no-cache-dir -vvvv`

### WSL

I was unable to install `spacy[cuda]` using WSL, because [WSL is not able to access the host GPU](https://github.com/Microsoft/WSL/issues/3847).

```bash
Modules:
  cuda      : No
    -> Cannot link libraries: ['cublas', 'cuda', 'cudart', 'cufft', 'curand', 'cusparse', 'nvrtc']
    -> Check your LDFLAGS environment variable.

ERROR: CUDA could not be found on your system.
```

BTW, Zsh did not recognize the package name with brackets, but escaping them helped (`pip install spacy\[cuda\]`).
