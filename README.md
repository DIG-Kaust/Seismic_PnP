![LOGO](https://github.com/DIG-Kaust/Seismic_PnP/blob/main/utils/PnP_logo.png)  

Reproducible material for **Plug and Play Post-Stack Seismic Inversion with CNN-based Denoisers -
Romero J., Corrales M., Luiken N., Ravasi M.** submitted to Second EAGE Subsurface Intelligence Workshop, 28-31 October 2022, Manama, Bahrain


## Project structure :clipboard:
This repository is organized as follows:

- :open_file_folder: **data**: Marmousi impedance synthetic model.
- :open_file_folder: **models**: folder containing pre-trained models (DnCNN and DRUnet).
- :open_file_folder: **utils**: Deep denoisers architectures and PnP framework.

## Notebooks :orange_book:
The following notebooks are provided:

- :orange_book: ``PnP_PD_Post-Stack_Seismic_Inversion_marmousi.ipynb``: notebook performing the comparison between model-based regularization and Plug and Play. ...;


## Getting started :space_invader: :robot:
To ensure reproducibility of the results, we suggest using the `environment.yml` file when creating an environment.

Simply run:
```
./install_env.sh
```

Remember to always activate the environment by typing:
```
conda activate pnpseismic
```
**Disclaimer:** For computer time, this research used the resources of the Supercomputing Laboratory at KAUST in Thuwal, Saudi Arabia. All experiments have been carried on a Intel(R) Xeon(R) Platinum 8260 CPU @ 2.40GHz equipped with a single NVIDIA TESLA V100. Different environment 
configurations may be required for different combinations of workstation and GPU.

## Pre-trained Models
For more details of the Pre-trained Deep Denoisers used in this study, please refer to the following repositories: https://github.com/cszn/DnCNN and https://github.com/cszn/DPIR.  


## Cite us :black_nib:
