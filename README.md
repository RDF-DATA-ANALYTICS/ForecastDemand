# Demand Forecasting Project repo

This repository is set up for demand forecasting project using the M5 Forecasting dataset.

## Setup GitHub SSH

Refer to https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## Set up venv (Linux)

From the project root:

```bash
cd ForecastDemand
python3 -m venv forecast_env
source forecast_env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Instructions using conda

```bash
cd ForecastDemand
conda create -n forecast-env python=3.12 -y
conda activate forecast-env
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you want the environment available as a Jupyter kernel:

```bash
python -m ipykernel install --user --name forecast-env --display-name "forecast-env"
```

## Set up on Windows

```powershell
cd ForecastDemand
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Kaggle API

This project downloads the M5 competition data via the Kaggle API and the `kagglehub` package.

1. Create a Kaggle account and generate a Kaggle API token (settings -> API token -> generate new token).
2. Once generated, follow the instructions.
3. Keep your local token in the project `.env` file, for example:

```bash
export KAGGLE_API_TOKEN="your_token_here"
```

If you want to save the token in a `.env` file and set the environment variable, run the following command.

```bash
set -a; source .env; set +a
```

To download the dataset into a local folder:

```bash
python data/download_m5.py --path /path/to/ForecastDemand/data/
```

If no path is supplied, the script downloads to the default Kaggle cache location.

## Notebooks structure

The repo structure is:

```text
ForecastDemand/
├── README.md
├── requirements.txt
├── data/
│   └── download_m5.py
|       ...
├── src/
│   └── <sub-package>
|       └── __init__.py
|       └── <example: interface>.py
|            ...
├── notebooks/
│   └── T001-Sample-View/
│       └── 0_data_view.ipynb
|           ...
└── ...
```

Follow the directory structure. Notebooks under each task should be named similar to the example folder.
If the module will be used in multiple places, place it under an appropriate sub-package in `src` directory.
