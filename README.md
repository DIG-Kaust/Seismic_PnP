![LOGO](https://github.com/DIG-Kaust/Project_Template/blob/master/logo.png)

Reproducible material for **Plug and Play Post-Stack Seismic Inversion with CNN-based Denoisers -
Romero J., Corrales M., Luiken N., Ravasi M.** submitted to Second EAGE Subsurface Intelligence Workshop, 28-31 October 2022, Manama, Bahrain


## Project structure
This repository is organized as follows:

:open_file_folder: **package**: python library containing routines for ....;
:open_file_folder: **data**: folder containing data (or instructions on how to retrieve the data.

## Notebooks
The following notebooks are provided:

- :orange_book: ``X1.ipynb``: notebook performing ...;
- :orange_book: ``X2.ipynb``: notebook performing ...


## Getting started :space_invader: :robot:
To ensure reproducibility of the results, we suggest using the `environment.yml` file when creating an environment.

Simply run:
```
./install_env.sh
```
It will take some time, if at the end you see the word `Done!` on your terminal you are ready to go. After that you can simply install your package:
```
pip install .
```
or in developer mode:
```
pip install -e .
```

Remember to always activate the environment by typing:
```
conda activate my_env
```

Finally, to run tests simply type:
```
pytest
```

**Disclaimer:** For computer time, this research used the resources of the Supercomputing Laboratory at KAUST in Thuwal, Saudi Arabia. All experiments have been carried on a Intel(R) Xeon(R) Platinum 8260 CPU @ 2.40GHz equipped with a single NVIDIA TESLA V100. Different environment 
configurations may be required for different combinations of workstation and GPU.

## Cite us 
