# Reproducing the Figures

The [Python script](reproduce-figures.py) reads the [capacity dataset](../data/capacity-scenarios.csv) and recreates the two figures used in the [case study](../projects/capacidade-linha-montagem.md). It also exports the 22 comparisons between layouts at equal pallet quantities.

**Scope:** Figure reproduction from 44 stored capacity values. This is not a WITNESS model execution or a verification of the underlying simulation results. The dataset still contains source-study values and is part of a local working draft.

## Run

Use Python 3.11 or later. From the portfolio root, install the plotting dependency and run:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/reproduce-figures.py
```

Output is written to `reproduced-figures/`, leaving the displayed portfolio images and input CSV unchanged:

- `production-capacity.png`, `.svg` and `.pdf`
- `layout-capacity-change.png`, `.svg` and `.pdf`
- `layout-capacity-change-data.csv`

PNG files are 2600 × 1500 pixels. SVG and PDF provide vector output. Minor rendering differences can occur between plotting environments.

Optional data and output paths:

```sh
python scripts/reproduce-figures.py --data data/capacity-scenarios.csv --output reproduced-figures
```

## Dataset

| Column | Meaning |
|---|---|
| `layout` | Original layout or Leak Test Moved |
| `availability_scenario` | H1 or H2, as defined in the case study |
| `pallets` | Circulating pallet quantity |
| `annual_capacity_thousand_units` | Projected annual output after calendar scaling and unit losses |

Each scenario contains eleven values, from 20 to 40 pallets in steps of two. Layout comparisons use `(relocated / original − 1) × 100` at matching availability and pallet quantity. Connecting lines do not imply simulations at intermediate quantities.

For a public synthetic demonstration, the dataset, model executions, figures and numerical interpretation must be updated together.
