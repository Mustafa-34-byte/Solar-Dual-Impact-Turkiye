# Solar PV Penetration, Merit-Order Effects and Balancing Reserve Costs in Türkiye's Electricity Market

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## Versions

The files shown when this repository is opened are the current revision, release `RENE-D-26-09232-R1` (`main`). The original submission stays available as its own release.

| Release | What it contains | Open the files |
| --- | --- | --- |
| [RENE-D-26-09232-R1](https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye/releases/tag/RENE-D-26-09232-R1) | Revised analyses, Appendix J, and corrected figures. This is the version on this page. | [R1 files](https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye/tree/RENE-D-26-09232-R1) |
| [RENE-D-26-09232-R0](https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye/releases/tag/RENE-D-26-09232-R0) | Original submission to Renewable Energy. | [R0 files](https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye/tree/RENE-D-26-09232-R0) |

## Overview

Replication package for the manuscript:

> **Akkaya, M. A., Yetgin, R. U., & Kayalıca, M. Ö. (2026).** *Solar PV Penetration, Merit-Order Effects and Balancing Reserve Costs in Türkiye's Electricity Market.* Manuscript under review.

Using hourly data for Türkiye (2022–2025, 35,064 observations), the study shows that solar generation simultaneously lowers day-ahead wholesale prices (merit-order effect) and raises balancing reserve (a-FRR) costs, with a non-linear transition regime emerging between approximately 20% and 33% solar penetration.

## Key Findings

- A 1 pp increase in solar share is associated with a **51.52 TL/MWh decline** in the Market Clearing Price.
- Balancing costs peak during the **late-afternoon ramp** (Hour 17).
- Beyond **~33% penetration**, surplus-management costs overtake deficit-side stress (the *flexibility trap*).
- The merit-order / balancing-cost divergence survives **inflation-neutral checks** (a-FRR/MCP ratio and cap-normalised prices).

## Repository Structure

```
├── data/
│   ├── README.md                           # Variable dictionary and data source
│   └── Model_Data.xlsx                     # Hourly market dataset (2022-2025)
│
├── notebooks/
│   ├── Dual_Effect_Full_Pipeline.ipynb     # Submitted analysis pipeline (Phases 1-11), unchanged
│   └── Dual_Effect_Full_Pipeline_REVISED.ipynb  # Revision: pipeline + reviewer-response analyses
│
├── results/                                # Pre-computed outputs (auto-generated)
│   ├── Phase_2/                            # SARIMAX baseline estimation (9 models)
│   ├── Phase_3/                            # Grid search & seasonality diagnostics
│   ├── Phase_4/                            # Robust estimation with optimized parameters
│   ├── Phase_5/                            # Daily profiles & hourly coefficient plots
│   ├── Phase_6/                            # XGBoost PDP & flexibility-trap analysis
│   ├── Phase_7/                            # Quantile regression robustness (Q10/Q50/Q90) + convergence diagnostics (7.2-7.4)
│   ├── Phase_8/                            # GAM flexibility-stress analysis (cubic spline)
│   ├── Phase_9/                            # Methodological framework flowchart
│   ├── Phase_10/                           # Appendices A–J (tables, figures, Botaş robustness, reviewer robustness)
│   ├── Phase_11_Inflation/                 # Inflation-robustness FE-OLS checks
│   ├── Phase_11_Robustness/                # Revision: timing/confounding (11.2) & sub-period (11.3)
│   ├── Supplementary_Metrics/              # Model-fit diagnostics (XGBoost & GAM R²)
│   ├── Submission_Figures/                 # Manuscript figures, journal numbering (Figure_1a … Figure_9, 650 dpi)
│   └── Supplementary_Figures/              # Supplementary figures (F1, F2, H1, I1, I2)
│
├── requirements.txt
├── CITATION.cff
└── LICENSE
```

## Methodology

| Phase | Method                     | Output                                          |
| ----- | -------------------------- | ----------------------------------------------- |
| 1     | Data ingestion             | Temporal indexing, integrity audit              |
| 2     | SARIMAX (baseline)         | 9 model summaries                               |
| 3     | Grid search (AIC)          | Optimal (p,d,q)(P,D,Q) orders                   |
| 4     | SARIMAX (optimized)        | Coefficients, diagnostics                       |
| 5     | Visualization              | Daily market profiles, hourly coefficient plots |
| 6.1   | XGBoost PDP                | Merit-order, balancing-cost and surplus PDPs    |
| 6.2   | XGBoost interaction        | Flexibility-trap regime figure                  |
| 7     | Quantile regression        | Q10/Q50/Q90 coefficient table & figure          |
| 8     | GAM (cubic spline)         | Flexibility-stress regime figure                |
| 9     | Framework diagram          | Methodological flowchart                        |
| 10    | Appendix generation        | Appendices A–I (incl. Botaş gas-tariff robustness, Appendix I) |
| 11    | Inflation robustness       | FE-OLS on a-FRR/MCP ratio & cap-normalised prices |

### Revision (Reviewer #2) — `Dual_Effect_Full_Pipeline_REVISED.ipynb`

The submitted notebook is kept unchanged. The REVISED notebook is a copy of it with the reviewer-response analyses
placed in their topical phases. Every added or changed block carries a `Revision_Review_Referee_2.x` tag
(2.x = Reviewer #2, comment x); the git history of branch `revision-referee-responses` records one commit per tag.

| Phase | Tag | Method | Output |
| ----- | --- | ------ | ------ |
| 6.4   | Referee_2.3 | Expanding-window (walk-forward) time-series CV of the Phase 6.1 XGBoost models — same features and estimator call — MAE/RMSE/R², Acc/F1/ROC-AUC, per-fold file | Appendix J.3 |
| 7     | Referee_2.5 | Quantile regression solved to convergence (standardised regressors) | Table 1 |
| 7.2–7.4 | Referee_2.5 | Solver iteration sensitivity, exact LP solution, day-clustered bootstrap SE | Appendix J.5 |
| 8.2   | Referee_2.4 | Regression-kink threshold (Hansen, 2017): γ with day-clustered bootstrap CI, kink coefficient δ (bootstrap SE), sup-F test of "no kink" (day-clustered wild-bootstrap p) | Appendix J.4 |
| 10 (J) | — | Assembles Tables J1–J5 | Appendix J |
| 11.2  | Referee_2.1 | Decision-time lags, TEİAŞ real-time data, confounding, net-load ramp | Appendix J.1 |
| 11.3  | Referee_2.2 | 2022–2023 vs 2024–2025 sub-period estimates | Appendix J.2 |
| figures | Referee_2.7 | a-FRR axes in TL/MW (capacity price); Figure 1a/1b: a-FRR on its own TL/MW axis (not shared with MCP); PDP axes labelled with units (`disp.axes_` fix in Phase 6.1); revision CSVs written with LF line endings | Figures 1, 4, 5, 6, 7, 8, 9, I.1, I.2 |

XGBoost settings (Phases 6.1, 6.2, 6.4): `XGBRegressor` / `XGBClassifier(n_estimators=200, random_state=42)`, every other
setting at the library default, no hyper-parameter tuning — recorded in `results/Phase_10/Appendix_E_XGBoost_Params.csv`.
Variance-inflation factors are reported by Phase 11.2 (`Phase_11_2_Confounding_Diagnostics.csv`, Appendix J.1); the
4-variable `Appendix_G_VIF` file of the submitted pipeline has been retired.

## Reproducibility

### Quick Start

```bash
git clone https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye.git
cd Solar-Dual-Impact-Turkiye
pip install -r requirements.txt
jupyter notebook notebooks/Dual_Effect_Full_Pipeline.ipynb
```

### Cache Mechanism

The notebook uses a built-in caching system:

- **Cache hit:** If `results/Phase_X/` already contains the expected CSV/PNG/TXT files, the notebook loads them and skips computation.
- **Cache miss:** The notebook runs the full estimation and saves outputs to `results/Phase_X/`.
- **Force re-run:** Delete the corresponding output file(s) and re-execute the cell. Two built-in switches automate this: `FORCE_FRESH` (setup of the robustness/appendix analyses) and `FORCE_FIGURES` (clears the cached figure PNGs so Phases 6.1/6.2/8 and Appendix I regenerate them at `FIG_DPI = 650`; Phase 5 figures are redrawn on every run).

Pre-computed results are included in this repository so that all figures and tables can be reproduced without re-running the computationally expensive SARIMAX grid search (~15 min) or XGBoost training.

**Revision phases are cached too.** Phases 6.4, 7.2–7.4, 8.2, 11.2 and 11.3 read their CSVs from `results/` when present, so a "clean" run of the REVISED notebook reproduces the tables from cache rather than recomputing them. To recompute a check, delete its CSV (e.g. `results/Phase_8/Phase_8_2_Hansen_Threshold.csv`) and re-run the cell; Phase 10 (Appendix J) then re-assembles Tables J1–J5 from the fresh files. The Phase 7.2 iteration-sensitivity table deliberately keeps the cached values: the *non-converged* IRLS fits it documents vary from machine to machine, whereas the converged estimates (7.3, 7.4, Table 1) do not. Bootstrap checks (7.4, 8.2) use `seed = 42` and 200 replications; Phase 8.2 takes ~3 min. XGBoost results (Phases 6.1, 6.2, 6.4) depend on the installed `xgboost` version — use the submission environment to reproduce the figures exactly.

### Data

All market data are sourced from the [EPİAŞ Transparency Platform](https://seffaflik.epias.com.tr/home) and are publicly available.

| Item         | Value                    |
| ------------ | ------------------------ |
| Observations | 35,064 (hourly)          |
| Period       | 1 Jan 2022 – 31 Dec 2025 |
| File         | `data/Model_Data.xlsx`   |

## Figure Map (manuscript ↔ pipeline)

| Manuscript | File in `results/Submission_Figures/` | Source output |
| --- | --- | --- |
| Figure 1a | `Figure_1a.png` | `Phase_5/Phase_5_Figure_1_Daily_Market_Profile.png` |
| Figure 1b | `Figure_1b.png` | `Phase_5/Phase_5_Figure_2_Daily_Market_Profile.png` |
| Figure 2 | `Figure_2.png` | `Phase_9/Figure_3_Methodological_Framework_Updated.png` |
| Figure 3 | `Figure_3.png` | `Phase_5/Phase_5_Figure_4_Hourly_Merit_Order_Effect_MCP.png` |
| Figure 4 | `Figure_4.png` | `Phase_6/Phase_6_Figure_5_PDP_Merit_Order_and_Volatility.png` |
| Figure 5 | `Figure_5.png` | `Phase_5/Phase_5_Figure_6_Hourly_Volatility_Effect_aFRR.png` |
| Figure 6 | `Figure_6.png` | `Phase_6/Phase_6_Figure_7_PDP_Merit_Order_and_Volatility.png` |
| Figure 7 | `Figure_7.png` | `Phase_6/Phase_6_Figure_8_Surplus_Probability_and_Distribution.png` |
| Figure 8 | `Figure_8.png` | `Phase_6/Phase_6_Figure_9_Flexibility_Trap.png` |
| Figure 9 | `Figure_9.png` | `Phase_8/Phase_8_Figure_10_GAM_Flexibility_Stress.png` |

Supplementary figures (F.1, F.2, H1, I.1, I.2) are exported with matching labels to `results/Supplementary_Figures/`.

## Citation

```bibtex
@unpublished{akkaya2026solar,
  title  = {Solar PV Penetration, Merit-Order Effects and Balancing Reserve Costs in T{\"u}rkiye's Electricity Market},
  author = {Akkaya, Mustafa An{\i}l and Yetgin, Recep U{\u{g}}ur and Kayal{\i}ca, Mehmet {\"O}zg{\"u}r},
  year   = {2026},
  note   = {Manuscript under review}
}
```

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgements

The authors thank Energy Exchange Istanbul (EPİAŞ) for providing transparent access to the Transparency Platform data.
