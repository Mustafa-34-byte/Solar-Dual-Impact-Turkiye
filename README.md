# Solar PV Penetration, Merit-Order Effects and Balancing Reserve Costs in Türkiye's Electricity Market

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)

## Overview

Replication package for the manuscript:

> **Akkaya, M. A., Yetgin, R. U., & Kayalıca, M. Ö. (2026).** *Solar PV Penetration, Merit-Order Effects and Balancing
> Reserve Costs in Türkiye's Electricity Market.* Manuscript under review, *Renewable Energy* (RENE-D-26-09232).

Using hourly data for Türkiye (1 January 2022 – 31 December 2025, 35,064 observations), the study finds that solar
generation lowers day-ahead wholesale prices (merit-order effect) and raises balancing-reserve (a-FRR) capacity prices,
with a transition regime between about 20% and 34% solar share. The package holds the data file, one Jupyter notebook
that produces every result file from it (with the SARIMAX orders fixed from a preliminary grid search; see *Order
selection*), the result files, and the record of the final run. The final run, with Python 3.11.18 and the pinned
packages of `requirements.txt`, took 2 h 8 min on an Apple M2 with 8 logical CPUs (see *Run time of the final run*);
the two other runs took 7 h 18 min and 2 h 10 min (see *Reproducibility*).

**Headline results of this release** (read from `results/`):

- Merit-order effect (Model 4): solar-share coefficient −5,780.84 TL/MWh per unit share (standard error clustered by
  calendar day 207.70; p < 0.001), i.e. **−57.81 TL/MWh per percentage point** of solar share
  (`Phase_4/Phase4_All_Coefficients.csv`).
- Balancing-cost effect (Model 1): +2,015.70 TL/MW per unit share (day-clustered standard error 446.15; p < 0.001), i.e.
  **+20.16 TL/MW per percentage point** (same file).
- Onset of balancing-cost acceleration (regression kink): **20%** solar share, 90% bootstrap interval **18–28%**
  (`Phase_8/Phase_8_2_Hansen_Threshold.csv`). The point estimate is 22% with year effects and 28% and 29% in the
  samples 2024–2025 and 2025 (`Phase_8/Phase_8_2_Kink_Location_Checks.csv`).
- Upper crossover of the XGBoost interaction simulation: 34.34% solar share in the base case
  (`Phase_6/Phase_6_2_Flexibility_Trap_Crossover.csv`); with the BOTAŞ gas tariff as a control there is no sustained
  crossover (`Phase_10/Appendix_I_Flexibility_Trap_Crossover.csv`), and there is none either when the MCP is removed
  from the features of the simulation (`Phase_6/Phase_6_2_Crossover_Without_MCP.csv`). Only 729
  of the 35,064 hours (2.1%) have a solar share above 34%, 630 of them in 2025
  (`Phase_10/Appendix_J5_Threshold_Support.csv`); the crossover is therefore reported as descriptive and
  specification-sensitive.
- The a-FRR-to-MCP price ratio rises with solar share (+38.49 per unit share, p < 0.001;
  `Phase_11_Inflation/Inflation_Robustness_Results.csv`).

## Quick start

1. **Look at the results without running anything.** Every output is in `results/`; `results/RUN_REPORT.md` and
   `results/RUN_CHECKPOINTS.csv` are the record of the final run, and *Map from manuscript and Supplementary Material
   to the result files* names the file behind each table and figure. `shasum -a 256 -c MANIFEST_SHA256.txt`, run in
   the package root, checks every other file of the package (*Reproducibility*).
2. **Set up the environment** in the package root with Python 3.11 and `requirements.txt`, and add JupyterLab with
   `pip install jupyterlab -c requirements.txt` (*Environment*).
3. **Run the notebook on the shipped results**, on a copy of the package. It loads the stored outputs (`[CACHE]`)
   and estimates no SARIMAX model again; on the reference computer it took about one minute (*Running on the shipped
   results*).
4. **Run from scratch**, on a copy with an empty `results/` folder, in JupyterLab or headless with
   `tools/run_notebook_headless.py`. The final run took 2 h 8 min on an Apple M2 with 8 logical CPUs (*A fresh run*,
   *Run time of the final run*).
5. **Compare.** In your copy, `shasum -a 256 -c MANIFEST_SHA256.txt` lists the files that differ from the shipped
   ones; *Reproducibility* says which differences were found between the three computers.

## Versions

This package is release **`RENE-D-26-09232-R2`**: the code, data file and result files of the second revision (R2) of
manuscript RENE-D-26-09232 (*Renewable Energy*). The releases listed below are available under their own names.

| Release | What it contains |
| --- | --- |
| [RENE-D-26-09232-R2](https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye/releases/tag/RENE-D-26-09232-R2) | Second revision: data file, analysis notebook (SARIMAX models estimated by profile maximum likelihood, day-clustered inference, self-checks) and the record of the notebook's final run (run report, checkpoints, manifest, run log and every output file). This package. |
| [RENE-D-26-09232-R1](https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye/releases/tag/RENE-D-26-09232-R1) | First revision: code, data file and result files, including the Appendix J tables. |
| [RENE-D-26-09232-R0](https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye/releases/tag/RENE-D-26-09232-R0) | Original manuscript (*Renewable Energy*). |

## Package contents

```text
Replication_Package_R2/
├── README.md                     this file
├── LICENSE                       MIT licence
├── CITATION.cff                  citation metadata
├── requirements.txt              exact package versions of the reference environment (Python 3.11.18)
├── MANIFEST_SHA256.txt           SHA-256 of every other file of the package
├── RUN_LOG.txt                   run log of the final run: a start and a finish line (with duration) per code cell
│                                 of the run (cells 1–53)
├── data/
│   ├── README.md                 columns, sources and SHA-256 of the data file
│   └── Model_Data.xlsx           hourly dataset 2022–2025 (35,064 rows, 48 columns)
├── notebooks/
│   └── Dual_Effect_Full_Pipeline_REVISED.ipynb   the analysis notebook (without stored outputs)
├── validation/
│   ├── README.md                 what the reference file is and what the notebook compares
│   └── pretest_reference_2026-11-20.csv          values of the independent pre-test (4,536 rows)
├── tools/
│   └── run_notebook_headless.py  executes the notebook once, top to bottom, without a browser (used for the final run)
└── results/                      every output of the notebook (152 files)
    ├── RUN_REPORT.md             run report: per step the output files with checksums, the comparison with the
    │                             pre-test, the checkpoints and the warnings of that step
    ├── RUN_CHECKPOINTS.csv       all 92 checkpoints of the run with status and detail
    ├── RUN_MANIFEST.json         data checksum, method tag and environment of the run
    ├── Phase_2/                  baseline SARIMAX(1,1,1)(1,0,1)24 models and logit Model 7.1: 9 summaries,
    │                             Phase2_Convergence.csv; starts/ (17 start records and progress.log)
    ├── Phase_3/                  seasonality diagnostics (ACF/PACF figure, lag-24 autocorrelations)
    ├── Phase_4/                  the eight SARIMAX models with the selected orders: coefficients with eight kinds of
    │                             standard error, diagnostics, likelihood-ratio tests, full report, Phase 2/Phase 4
    │                             comparison; starts/ (33 start records and progress.log)
    ├── Phase_5/                  daily market profiles and hourly coefficient figures
    ├── Phase_6/                  XGBoost partial dependence, flexibility-trap simulation (also without the MCP),
    │                             walk-forward validation
    ├── Phase_7/                  quantile regression (Q10/Q50/Q90), solver checks, day-clustered bootstrap
    ├── Phase_8/                  GAM flexibility stress (Figure K.1), regression-kink threshold and its location checks
    ├── Phase_9/                  methodological framework flowchart (Figure 2)
    ├── Phase_10/                 Appendices A–J tables and figures (incl. BOTAŞ robustness, Appendix I; Figure K.1
    │                             is in Phase_8/); starts/ (11 start records of Table C.1 and progress.log)
    ├── Phase_11_Inflation/       ratio and cap-normalised fixed-effects OLS (Appendix J.6)
    ├── Phase_11_Robustness/      timing and confounding (Table J.1), sub-periods (Table J.2)
    ├── Submission_Figures/       PNG masters of the manuscript figures (Figure_1a … Figure_8) and Figure_9.png
    ├── Supplementary_Figures/    the six figures of the Supplementary Material (F1, F2, H1, I1, I2, K1)
    └── Supplementary_Metrics/    in-sample fit of the XGBoost and GAM models
```

Phase numbers, result folders and file names are those of release R1 and are kept unchanged. Phase 6.3 is not used (the
out-of-sample check keeps its R1 number 6.4). `RUN_LOG.txt` is the log that `tools/run_notebook_headless.py` writes next
to `notebooks/`; it lies outside `results/` because it is a record of the execution, not an output of the notebook.

## How to run

### Environment

In the package root (the folder that holds `requirements.txt`):

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is the complete package list of the environment in which the results were produced (Python 3.11.18;
numpy 2.3.5, pandas 2.3.3, scipy 1.16.3, statsmodels 0.14.6, scikit-learn 1.8.0, xgboost 3.2.0 and 65 further pinned
packages, including ipykernel, nbclient and nbconvert for the headless run). An interactive notebook interface was not
part of that environment. To add one without changing a pinned version, install it with the file as constraints:
`pip install jupyterlab -c requirements.txt` for JupyterLab, the interface we recommend for an interactive run, or
`pip install notebook -c requirements.txt` for the classic Notebook interface. On Windows the environment is created
with `py -3.11 -m venv .venv`; without activating it, its interpreter is `.venv\Scripts\python` (for example
`.venv\Scripts\python -m pip install -r requirements.txt`) and JupyterLab is started with `.venv\Scripts\jupyter-lab`.

The three lines of the code block and the two installations with the constraints file were run on 21 November 2026 in
a folder that held only `requirements.txt` (macOS, Python 3.11.18): the three lines installed the 71 pinned packages
in their pinned versions (`pip freeze` lists these and no other package), adding JupyterLab (4.6.6) and then the
Notebook interface (7.6.5) left all 71 versions unchanged, and `jupyter lab` started.

The notebook does not enforce this environment. Its setup cell compares the installed versions of eleven packages with
the reference environment, reports every difference (checkpoint K05, a WARNING) and continues. This README states where
the results of the package were produced; the notebook can be run elsewhere, and the results can then differ (see
*Reproducibility*).

### A fresh run

A complete record comes from one kernel session that starts from an **empty `results/` folder**. Work on a copy of the
package and empty its `results/` folder, but keep the folder itself: the notebook looks for `results/` and `data/` in
the working folder of the kernel and in its parent folder, and if it finds no `results/` it creates one in the working
folder of the kernel, normally `notebooks/`, and writes the run there (*Data guard* says what happens when the data
file is not in `data/`). Then run the notebook in one of two ways:

- **interactive, in JupyterLab (the route we recommend to readers):** start `jupyter lab` from the package root with
  the environment activated (the notebook asks for the kernel *Python 3 (ipykernel)*; checkpoint K05 of the setup cell
  shows whether the eleven packages it checks have the pinned versions), open
  `notebooks/Dual_Effect_Full_Pipeline_REVISED.ipynb` and press *Restart the kernel and run all cells* in the toolbar
  of the notebook (with the classic interface: `jupyter notebook notebooks/Dual_Effect_Full_Pipeline_REVISED.ipynb`,
  then *Run All* in a fresh kernel); or
- **headless:** from the package root, with the environment activated (`python3` is the kernel that ipykernel installs
  into the environment; it starts the same interpreter as the script, unless a kernel of the same name is registered in
  your user Jupyter folder; checkpoint K05 shows the versions in use),

  ```bash
  python tools/run_notebook_headless.py notebooks/Dual_Effect_Full_Pipeline_REVISED.ipynb python3
  ```

  The script executes every code cell once in the notebook's own folder, saves the notebook with its outputs after
  every code cell and appends to `RUN_LOG.txt` a line when a cell starts, a line with its duration when it finishes
  and a line at the start and at the end of the run; its exit code is 0 if all cells ran and 1 if a cell raised.
  The equivalent call of nbconvert is

  ```bash
  jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 \
      --ExecutePreprocessor.kernel_name=python3 notebooks/Dual_Effect_Full_Pipeline_REVISED.ipynb
  ```

  Both overwrite the notebook with the new outputs, which is why they are run on a copy (delete the copy's
  `RUN_LOG.txt` first if the log should cover the new run only). Jupyter prints an
  `[IPKernelApp] WARNING | Kernel is running over TCP without encryption` line on the console when the kernel starts;
  it concerns the local kernel connection and is not part of the notebook record.

The setup cell writes a new `results/RUN_MANIFEST.json` for the run. A `results/` folder that holds outputs but no
manifest, or a manifest written for another data file or method, stops the notebook.

### Running on the shipped results

Run on the package as shipped, the notebook continues the stamped run instead of starting a new one: every phase whose
output files exist loads them (`[CACHE]`). Each start record under `results/Phase_2/starts`, `results/Phase_4/starts`
and `results/Phase_10/starts` holds the result of one start and is reloaded when its signature matches, so a SARIMAX
model is re-optimised only if the output files of its phase and its start records are deleted. The signature is built
from `SARIMAX_METHOD_TAG`
(which includes the first 12 characters of the SHA-256 of the data file), the parameter names, the number of
observations, the burn-in, the orders, the start and the search settings; a cached SARIMAX table of Phases 2, 4 and 10
is used when its `Method` column equals `SARIMAX_METHOD_TAG`. Neither check covers the series computed from the data
file, the name of the dependent variable or the notebook code, so results computed before a change to the code are
reused without a warning: after changing the code, start from an empty `results/` folder.

The outputs of Phase 3, the figures of Phases 5 and 9, the S1.5 table
(`Phase_4/Phase4_Baseline_vs_Optimized_Solar.csv`), the two Appendix D tables, the Appendix J tables and the figure
exports are redrawn or rebuilt on every run,
`RUN_REPORT.md` receives new sections (it is append-only), the cell that closes the run (cell 53) writes
`results/RUN_CHECKPOINTS.csv` anew, and the two check cells after it (*Phase 6.2 (check)* and *Phase 8.2 (check)*)
rewrite their tables whenever they are executed. Cell numbers in this README are the positions of the cells in the
notebook file, counted from 0 with the text cells included, as in `RUN_LOG.txt`.
Checks that need a quantity the result files do not store (iteration counts, iteration-limit marks and solver status
of the quantile regressions in Phase 7) are reported as NOT CHECKED. Checks that read the result files (for example
K10–K14 and K16 of Phase 2, and the comparisons with the pre-test, K17 and K90) are evaluated on the loaded files: an
OK there shows that the shipped files pass the check, not that anything was re-estimated. Run this mode on a copy of
the package as well; in the reference environment on an Apple M2 it took about one minute, gave 92 checkpoints (82 OK,
5 WARNING, 5 NOT CHECKED, 0 FAILED) and left every result file except `RUN_REPORT.md` and `RUN_CHECKPOINTS.csv`
byte-identical. Two switches, both `False` in the notebook, clear caches when set to `True`: `FORCE_FIGURES` (setup
cell, cell 1) deletes 10 cached figure files so that their phases redraw them, and `FORCE_FRESH` (cell 35, under the
heading *Recalculation switch*, before Appendix B) deletes four cached outputs (Appendix B stationarity tests, Appendix
J.6 inflation check, XGBoost and GAM fit metrics) so that they are recomputed. Phase 6.1 loads its figures and
`Phase_6_1_PDP_Values.csv` when all four files exist and otherwise refits the XGBoost models
(`n_estimators=200, random_state=42`). To recompute one step, delete its output files in a copy and run the setup cell,
Phase 1 and the cell of that step in one kernel session; some cells use a function of an earlier cell (Appendix I, for
example, needs the Phase 6.2 cell) and stop with a message that says so.

### Running on Google Colab (no code to add)

A local run as described above is the route we recommend. On Colab the notebook starts and estimates without any added
code, but slowly; the trial described at the end of this section was followed up to the end of Phase 2 only. The
steps are:

1. Open the notebook in Colab: *File → Upload notebook*, `notebooks/Dual_Effect_Full_Pipeline_REVISED.ipynb`.
2. In the *Files* panel on the left, upload `data/Model_Data.xlsx` and wait until the upload has finished. The file
   lands in the working folder of the runtime (`/content`), where the notebook also accepts the data file (see *Data
   guard*).
3. Optional: create a folder named `validation` in the same panel and upload
   `validation/pretest_reference_2026-11-20.csv` into it. Without it the setup cell prints `Reference file not found`
   and the comparisons with the independent pre-test are skipped.
4. *Runtime → Run all*.

The notebook then starts a new run: it creates a `results/` folder in the working folder and estimates everything from
scratch. Colab supplies its own Python and package versions, so the setup cell reports the differences from the
reference environment (checkpoint K05, a WARNING) and the run continues; results can differ from those in `results/`,
and the figures are drawn with another font if the runtime has no Times New Roman. Files in
the working folder are deleted when the runtime ends, and the *Files* panel downloads single files, not folders.

Trial of 21 November 2026 (a Colab Pro account; the runtime reported 2 logical CPUs and Python 3.13.18, with numpy
2.4.6, pandas 2.2.3, statsmodels 0.15.0, scikit-learn 1.6.1, xgboost 3.4.1 and matplotlib 3.10.0 in place of the
pinned versions): with the four steps above and no code added, the setup cell found and verified the data file, and
the comparisons with the independent pre-test gave 16 match, 0 differ in Phase 1 and 77 match, 0 differ in Phase 2,
as in the reference run. Two SARIMAX models were estimated at a time instead of four: the first 13 start records of
Phase 2 show the same log-likelihoods, at the four decimals of the progress log, and the same numbers of filter
passes as the reference run, one start took 10 to 17 minutes against 2.7 to 4.3 minutes, and Phase 2 took 2 h 8 min
against 18.7 min. The trial was followed only up to this point; extrapolated from Phase 2, a complete run would take
more than half a day (the reference run took 2 h 8 min in all). No result of this package was produced on Colab.

### Run time of the final run

The final run was one headless run of `tools/run_notebook_headless.py` from an empty `results/` folder on
21 November 2026, 02:40:12 – 04:48:02 (**2 h 7 min 50 s**), with the kernel name `rene-r2`, a kernel registered for
the pinned environment (see the docstring of the script). The machine was an Apple M2 (8 logical CPUs, 16 GB memory,
macOS 27.2, arm64, as reported by its operating system; `RUN_MANIFEST.json` records the platform and the number of
CPUs). Four SARIMAX models were estimated in parallel (`SARIMAX_N_JOBS = 4`, the default; the setup cell lowers it to
the number of logical CPUs or to one job per 2.5 GiB of memory where these are smaller, and the environment variable
`SARIMAX_N_JOBS`, set before the kernel starts, sets another value within the same limits). Durations per cell from
`RUN_LOG.txt`:

| Step (notebook cell) | Seconds | Minutes |
| --- | ---: | ---: |
| Phase 2: baseline SARIMAX models and logit (cell 5) | 1,123.5 | 18.7 |
| Phase 4: SARIMAX models with the selected orders, LR tests (cell 9) | 3,845.2 | 64.1 |
| Phase 7.2: QR solver iteration sensitivity (cell 21) | 87.3 | 1.5 |
| Phase 7.3: exact QR solution (cell 23) | 233.2 | 3.9 |
| Phase 7.4: day-clustered bootstrap of Table J.6 (cell 25) | 1,172.1 | 19.5 |
| Phase 8.2: regression kink with bootstrap (cell 29) | 77.2 | 1.3 |
| Phase 10: Appendices A–H, incl. the five SARIMAX fits of Table C.1 (cell 33) | 1,081.6 | 18.0 |
| all other 21 code cells of the run together (listed below the table) | 47.0 | 0.8 |

The other 21 code cells of the run are cells 1, 3, 7, 11, 13, 15, 17, 19, 27, 31, 35, 37, 39, 41, 42, 43, 45, 47, 49,
51 and 53 (setup, Phases 1, 3, 5, 6, 7.1, 8.1, 9 and 11, the `FORCE_FRESH` cell, Appendices B, I and J, the
supplementary XGBoost and GAM metrics, exports). The three SARIMAX cells (Phases 2, 4 and 10) took 6,050.3 s
(100.8 min) together. Fewer cores lengthen these steps. The times in the notebook's first cell are approximate; the
measured durations are those above.

## Map from manuscript and Supplementary Material to the result files

`results/Submission_Figures/` holds byte-identical copies of the source outputs listed in the table below. All PNGs
carry a 1000-dpi tag; the two large canvases, Figure 2 and the Phase 3 diagnostics, are rendered at 750 dpi and saved
with the same tag, which leaves them 9,450 and 9,790 pixels wide.

Manuscript figures:

| Manuscript | `Submission_Figures/` | Source output |
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
| *(Supplementary Figure K.1)* | `Figure_9.png` | `Phase_8/Phase_8_Figure_10_GAM_Flexibility_Stress.png` |

The manuscript has eight figures. `Figure_9.png` keeps its R1 name (template rule) and is **Supplementary
Figure K.1**, the base-case GAM figure; it is byte-identical to `Supplementary_Figures/Supplementary_Figure_K1.png` and
is not a manuscript figure. The figure files prepared for the journal upload are lossless TIFF conversions of
`Figure_1a.png` … `Figure_8.png` (same pixels, same 1000-dpi tag); the note above the notebook's export cell and the
message printed by that cell name the PNG files as the files to upload.

Supplementary Material:

| Supplementary | Result file(s) |
| --- | --- |
| Table A.1 | `Phase_10/Appendix_A_Descriptive_Statistics.csv` |
| Table B.1 | `Phase_10/Appendix_B_Stationarity_Tests.csv` (ADF and KPSS); `Phase_10/Appendix_B_ADF_Unit_Root_Tests.csv` (ADF) |
| Table C.1 | `Phase_10/Appendix_C_Model_Comparison.csv` (starts in `Phase_10/starts/`) |
| Table D.1 | `Phase_10/Appendix_D_Full_SARIMAX_Results.csv`; every hypothesis variable of the eight models (and the consumption control) with all standard errors: `Phase_10/Appendix_D_All_Hypothesis_Variables.csv`; full estimates: `Phase_4/` |
| Table E.1 | `Phase_10/Appendix_E_XGBoost_Params.csv` |
| Figures F.1, F.2 | `Phase_10/Appendix_F1_MCP_Correlation.png`, `Phase_10/Appendix_F2_aFRR_Correlation.png` (copies in `Supplementary_Figures/`) |
| Figure H.1 | `Phase_10/Appendix_H_Down_Regulation_Volume.png` (copy in `Supplementary_Figures/`) |
| Figures I.1, I.2 | `Phase_10/Appendix_I_Figure_I1_Flexibility_Trap_Botas.png`, `Phase_10/Appendix_I_Figure_I2_GAM_Flexibility_Stress_Botas.png`; crossover `Phase_10/Appendix_I_Flexibility_Trap_Crossover.csv`; report `Phase_10/Appendix_I_Botas_Report.txt` |
| Table J.1 | `Phase_10/Appendix_J1_Timing_Robustness.csv` (from `Phase_11_Robustness/Phase_11_2_Timing_Robustness.csv`); correlations and variance-inflation factors of Appendix J.1: `Phase_11_Robustness/Phase_11_2_Confounding_Diagnostics.csv` |
| Table J.2 | `Phase_10/Appendix_J2_SubPeriod.csv` (from `Phase_11_Robustness/Phase_11_3_SubPeriod.csv`) |
| Table J.3 | `Phase_10/Appendix_J3_OutOfSample.csv` (from `Phase_6/Phase_6_4_Out_of_Sample_CV.csv`; per fold: `Phase_6/Phase_6_4_Out_of_Sample_CV_Folds.csv`) |
| Table J.4 | `Phase_10/Appendix_J4_Threshold.csv` (from `Phase_8/Phase_8_2_Hansen_Threshold.csv` and `Phase_6/Phase_6_2_Flexibility_Trap_Crossover.csv`) |
| Table J.5 | `Phase_10/Appendix_J5_Threshold_Support.csv` and `Appendix_J5_Threshold_Support_Notes.csv` |
| Table J.6 | **`Phase_10/Appendix_J5_Clustered_QR.csv`** (R1 file name kept; from `Phase_7/Phase_7_4_QR_Clustered_Bootstrap_SE.csv`) |
| Appendix J.6 (inflation and currency effects) | `Phase_11_Inflation/Inflation_Robustness_Results.csv` |
| Figure K.1 | `Phase_8/Phase_8_Figure_10_GAM_Flexibility_Stress.png` (= `Supplementary_Figures/Supplementary_Figure_K1.png` = `Submission_Figures/Figure_9.png`) |
| Appendix L (reproducibility on other computers) | no result file of this package: the second and the third run listed under *Reproducibility* (their results are not part of this package) |
| S1.5 (baseline vs selected orders) | `Phase_4/Phase4_Baseline_vs_Optimized_Solar.csv` |
| S1.6 (in-sample fit) | `Supplementary_Metrics/XGBoost_Performance_Metrics.csv`, `Supplementary_Metrics/GAM_Performance_Metrics.csv` |

Further outputs that support these tables: `Phase_6/Phase_6_1_PDP_Values.csv` and `Phase_6_2_Flexibility_Trap_Curves.csv`
(curves of Figures 4, 6 and 8), `Phase_7/` (quantile-regression point estimates, solver sensitivity, exact LP solution, and
`Phase_7_Figure_11_Quantile_Regression_Coefficient_Robustness.png`, an output that is not a figure of the
manuscript or the Supplementary Material), `Phase_8/Phase_8_Flexibility_Stress_Report.txt` and `Phase_3/`.

Two statements of the manuscript rest on the two check cells at the end of the notebook, *Phase 6.2 (check)* (cell 55)
and *Phase 8.2 (check)* (cell 57). They come after the cell that closes the run, use only the setup cell and Phase 1,
make no entry in `RUN_REPORT.md` or `RUN_CHECKPOINTS.csv` and write one table each under `results/`.

First, Section 4.5 says that the crossover near 34% is also not reproduced when the MCP is removed from the features
of the simulation. *Phase 6.2 (check)* repeats the Phase 6.2 simulation with the statements of Phase 6.2 (in the
reference environment it gives the shipped crossover of 34.34% and the two shipped curves exactly) and then without
the MCP. Without it there is no upward crossing after which the surplus curve stays above the deficit/balanced curve
up to 45%: the upward crossings are at 19.11%, 23.24%, 24.93% and 27.21%, the downward crossings at 22.11%, 24.84%,
25.51% and 27.32%, and at the last grid point of the common range (44.85%) the surplus curve is at 7,676 TL/MW and
the deficit/balanced curve at 7,724 TL/MW (6,353 and 3,311 TL/MW with the MCP). The result table is
`Phase_6/Phase_6_2_Crossover_Without_MCP.csv`.

Second, Section 4.6 and Supplementary Appendix J.4 say that the location of the kink changes little when year effects
are added and rises when the sample is limited to the most recent years. *Phase 8.2 (check)* repeats the
point estimate of the Phase 8.2 kink model with the definitions of Phase 8.2 (in the reference environment it gives
the shipped threshold of 20% and the shipped slopes, 56.4 and 137.2 TL/MW per percentage point below and above the
threshold, exactly) and then three variants: with dummies for 2023, 2024 and 2025 added to the controls the threshold
is 22% (slopes 54.8 and 140.2); on the 17,544 hours of 2024–2025 it is 28% (62.1 and 140.1); and on the 8,760 hours
of 2025 it is 29% (59.6 and 137.8). These are point estimates of the least-squares grid search (5–44% in steps of
1); no bootstrap interval and no test was computed for the variants. The result table is
`Phase_8/Phase_8_2_Kink_Location_Checks.csv`.

## Data guard

The setup cell computes the SHA-256 of the data file (`data/Model_Data.xlsx`) before anything is estimated or loaded and
stops unless it is

`71e299d35f23f818e059e7e952700fc669ac778823074f10ec68b3f35369a78c`

(the data file of this release; see [`data/README.md`](data/README.md)). Phase 1 then verifies the structure of the file (complete hourly grid,
no missing values, 1,461 calendar days, `Date` equal to the calendar day of the time index, month terms on a 12-month
cycle, `Weekend` equal to Saturday or Sunday, solar share within [0, 1] and equal to solar generation divided by the
total generation implied by the other share columns, checkpoints K01–K04); a failed check stops the notebook.
`results/RUN_MANIFEST.json` ties the results folder to this checksum and to the estimation method.

If `Model_Data.xlsx` is not in `data/`, the notebook also accepts it in the working folder of the kernel (Jupyter
normally starts the kernel in the folder of the notebook, and `tools/run_notebook_headless.py` does so) and checks the
same SHA-256. If the file is in neither place, the notebook stops with a message that says where to put it. Keep the
`data/` folder of the package: when there is no `data/` folder at all, the notebook looks for `validation/` in the
working folder of the kernel; if the reference file is not there, it skips the comparisons with the independent
pre-test (the setup cell prints `Reference file not found`).

## Estimator

The eight SARIMAX models are regressions with seasonal-ARMA errors, estimated with the statsmodels `SARIMAX` likelihood
by **profile maximum likelihood**: for given AR/MA parameters the regression coefficients are obtained in closed form by
generalised least squares, so the numerical search (Nelder–Mead search, then Newton polishing) runs over the AR/MA
parameters only. Regressors are rescaled for numerical conditioning and the coefficients and standard errors are
transformed back to the original units. Each model is estimated from **several starts** – statsmodels' default start,
the best point of a fixed grid and, in Phase 4, the Phase 2 estimate of the same model; when the best point is not
invertible, its mirror image is estimated as a further start – and every finished start is saved as a JSON record under
`results/Phase_*/starts/`. An estimate is **certified** when the profile Hessian at the point is negative definite and
the predicted remaining gain is below 10⁻⁸ log-likelihood units (a documented *plateau* rule exists for flat a-FRR
ridges; it was not needed: all 16 SARIMAX estimates of Phases 2 and 4 are certified, `Phase2_Convergence.csv` and
`Phase4_Model_Diagnostics.csv`, column `Status`; the five Table C.1 fits are certified as well). The **invertible
representation** of the best point is always reported, also where a non-invertible mirror image of the same model has a
slightly higher log-likelihood (for Model 5 the pre-test reports that mirror image, 0.0224 units higher; see the
comparison below). Orders: SARIMAX(2,0,2)(1,0,1)24 with
an intercept for the day-ahead price (MCP; Models 4–6) and SARIMAX(1,1,2)(1,0,1)24 without an intercept for the a-FRR
price (Models 1–3, 7.2, 7.3), whose regression error is integrated of order one; the log-likelihood leaves out the first
27 (MCP) or 28 (a-FRR) observations, so 35,037 and 35,036 observations enter it.

Eight kinds of standard error are written for every SARIMAX coefficient (Phase 2 summaries and
`Phase_4/Phase4_All_Coefficients.csv`): `Std_Error` (outer product of gradients, the statsmodels default), `GLS`
(conditional on the AR/MA parameters), `Hessian`, `Robust` (sandwich), `Cluster_Day` (sandwich clustered by calendar
day, 1,461 clusters), `Cluster_Day_adj` (the same with the factor G/(G−1)), `HAC24` and `HAC48`. **Inference in the
paper uses `Cluster_Day`** (Supplementary Table D.1). The columns are `std err` and `std err (<kind>)` in the Phase 2
summaries and `Std_Error` and `Std_Error_<kind>` in `Phase4_All_Coefficients.csv`; in
`Phase_10/Appendix_D_All_Hypothesis_Variables.csv`, `Std_Error` is the day-clustered standard error (see the column
`SE_Type`) and the OPG one is `Std_Error_OPG`. The residuals remain serially correlated (Ljung–Box Q(24) between
1,238.0 and 1,295.9 for the a-FRR models and between 184.5 and 222.4 for the MCP models, all p < 0.001;
`Phase4_Model_Diagnostics.csv`), which is why inference does not rely on white-noise residuals. For the solar coefficient
the HAC48 standard errors are of similar size (Model 4: 226.94; Model 1: 460.79). Likelihood-ratio tests of the solar
coefficient give LR = 1,509.18 (Model 4) and 46.96 (Model 1), both with p < 0.001, also after rescaling by the ratio of
Hessian to day-clustered variance (`Phase4_LR_Tests.csv`). The Model 4 statistic uses the restricted fit in the invertible
representation (start `grid`, log-likelihood −246,801.3478); the restricted fit from the start `default` is the
non-invertible mirror image (log-likelihood −246,801.3367).

## Order selection

The SARIMAX orders – SARIMAX(2,0,2)(1,0,1)24 for the MCP and SARIMAX(1,1,2)(1,0,1)24 for the a-FRR price – were taken
from a **preliminary AIC-minimising grid search** (216 combinations per model on a stratified four-week sample). That
search is **not part of this package and is not re-run**: the notebook takes the orders as fixed. Supplementary Table C.1
(`Phase_10/Appendix_C_Model_Comparison.csv`) compares, on a common likelihood sample, the baseline order (1,1,1)(1,0,1)24
with the selected orders and adds an a-FRR alternative in levels, SARIMAX(1,0,2)(1,0,1)24 with an intercept: on the full
sample that alternative has a lower AIC (by 15.5) and BIC (by 7.1) than the selected (1,1,2) model and an almost identical
solar coefficient (2,009.16 versus 2,015.70); it is reported as a robustness check.

## What the run checks about itself

- **Warning policy.** No blanket warning filter is installed. A recorder installed in the setup cell lists every
  warning raised in the main process and in the parallel jobs, by step, in `RUN_REPORT.md`; warnings of the main process
  are still shown in the cell output as Python shows them. The only filter that suppresses a warning is scoped to one
  call (the image-size warning of PIL when the notebook reads its own 1000-dpi figures in the export cell). In addition,
  numpy's floating-point warnings are switched off by `np.errstate(all='ignore')` for two lines of
  `sarimax_implied_clusters()` (setup cell), a check that recovers the number of day clusters from the stored standard
  errors; a parameter whose two standard errors coincide gives a division by zero and is dropped there. Two warnings
  are captured where they arise and reported as checkpoint results instead of being printed: the IterationLimitWarning of
  the quantile-regression solver (Phases 7.2–7.4; iteration-limit flags in the tables, checkpoints K30–K32) and the KPSS
  InterpolationWarning (Appendix B; checkpoint K43); they are therefore not part of the warning count of checkpoint K91.
  Any other warning raised in these steps is passed on unchanged.
- **Checkpoints.** The self-checks (K01–K91; 92 entries in this run) print `[OK]`, `[WARNING]`, `[FAILED]` or
  `[NOT CHECKED]` with what was checked; all are listed in `results/RUN_CHECKPOINTS.csv` and at the end of `RUN_REPORT.md`. A failed check of the data
  or of the design (setup cell, Phase 1) stops the notebook at once; any other failed check is reported, the run
  continues, and **cell 53 raises an error after writing the summary if a checkpoint FAILED**. WARNING marks a
  documented property of the results or a difference that can occur between machines; NOT CHECKED means the quantity
  was not available (for example because it was loaded from the results folder or, for K17 and K90, because the
  reference file of the pre-test was not found).
- **Result of the final run: 92 checkpoints, 85 OK, 7 WARNING, 0 FAILED, 0 NOT CHECKED.** The seven WARNING entries:
  1. *K17 Phase 4* – 128 match, 3 DIFFERS with the pre-test: Model 5 log-likelihood, AIC and `ma.S.L24`, explained
     below (mirror image of the seasonal MA term).
  2. *K32 Phase 7.4* – 15 of the 1,200 bootstrap replicates (six estimates × 200) stopped at the 5,000-iteration limit of
     the quantile-regression solver and are kept in the standard errors; re-solved with up to 50,000 iterations (a
     diagnostic, not used in Table J.6) none stays at the limit and the largest change of a clustered standard error is
     0.002%. The count can differ between machines: in the second and the third run listed under *Reproducibility* it
     was 16 and 17 of 1,200 (largest change 0.001% and 0.003%).
  3. *K43 Appendix B* – all four KPSS p-values are bounds of the look-up table: p < 0.01 for the MCP, the a-FRR price in
     levels and the solar share, p > 0.10 for the differenced a-FRR price. `Appendix_B_Stationarity_Tests.csv` writes these
     bounds as 0.01 and 0.1; the ADF p-values written as 0.0 are below 0.001.
  4. *K42 Appendix I* – with the BOTAŞ tariff as a control the surplus curve does not stay above the deficit/balanced curve
     up to 45%: no sustained crossover (upward crossings at 2.16%, 23.96% and 35.70%, downward at 1.16%, 4.06%, 29.00% and
     36.44% solar share); the crossover field of `Appendix_I_Flexibility_Trap_Crossover.csv` is therefore empty.
  5. *K17 Appendix I* – 2 match, 1 DIFFERS: the Figure I.1 crossover, explained below.
  6. *K90* – total of all comparison tables: 24 tables, 651 match, 4 DIFFERS.
  7. *K91* – warnings recorded: 2 (one distinct warning).
- **The recorded warning.** One infrastructure warning of the parallel-execution library was recorded, twice, in
  Phase 4 (main process): `UserWarning: A worker stopped while some jobs were given to the executor. This can be caused
  by a too short worker timeout or by a memory leak.` (joblib, `externals/loky/process_executor.py:787`). It was shown
  as two stderr outputs of the Phase 4 cell during the run and is recorded in `RUN_REPORT.md`. It means that the executor
  retired a worker process in its regular way – a loky worker leaves only between tasks, after its idle time-out or after
  the library's check of the worker's memory growth – while further jobs were queued, and started a replacement worker;
  no job is dropped or repeated with another input. The eight SARIMAX models reach the same maximum in the two other
  runs listed under *Reproducibility*, whose run reports record no such warning.

## Comparison with the independent pre-test

`validation/pretest_reference_2026-11-20.csv` holds 4,536 reference values of an independent recomputation of the final
specification (see [`validation/README.md`](validation/README.md)). After each phase that has reference values, `compare_with_reference()` writes a
table to `RUN_REPORT.md` with the status `match` or `DIFFERS` per value and the tolerance used; a difference is recorded
and never stops the run. The final run made **655 comparisons in 24 tables: 651 match, 4 DIFFERS**. 655 counts
comparisons, not distinct rows: some rows are compared in more than one table (for example, the Appendix J table
compares rows that the Phase 1 threshold table and the Table J1 and Table J2 comparisons also compare). Most rows of
the file are not compared, including many that carry a tolerance; the p-values and condition numbers carry none.
Phase 3,
Phase 7.2, Phase 9 and the figure exports have no reference values. The workbook of the pre-test and the code of that
recomputation are not part of the package, only the values read from the workbook. Six rows
(`ESIK.duzeltilmis.gt34.*`) come from a message of the corresponding author, not from the workbook (`value_kind` =
`message`); they enter 11 of the 651 matches (5 in the Phase 1 threshold table, 6 in the Appendix J table). The
Phase 1 threshold table has no K17 checkpoint of its own; its 16 comparisons are counted in K90. The four DIFFERS rows:

| Row | This run | Pre-test | Explanation |
| --- | ---: | ---: | --- |
| Model 5 log-likelihood | −246,075.3105 | −246,075.2881 | The pre-test reports the non-invertible mirror image of the same Model 5 (seasonal MA term −1.0924, the reciprocal of this run's −0.9154), whose log-likelihood is 0.0224 units higher (tolerance 0.02); the notebook reports the invertible representation. Regression coefficients and standard errors of Model 5 match. |
| Model 5 AIC | 492,218.6209 | 492,218.5761 | Same cause (difference 0.0448, tolerance 0.04). |
| Model 5 `ma.S.L24` | −0.9154 | −1.0924 | Same cause: the two values are reciprocals. |
| Figure I.1 crossover (% solar share) | none | 35.70 | Definition: the notebook reports a crossover only if the surplus curve stays above the deficit/balanced curve up to 45%; the pre-test value is the last upward crossing, which this run also finds at 35.70%, after which the surplus curve falls below again at 36.44%. |

## Reproducibility

The analysis was run in full on three computers, each from an empty `results/` folder and with the same data file.
The result files of this package come from the reference computer.

| Run | Computer (logical CPUs) | System | Python | Duration | Checkpoints |
| --- | --- | --- | --- | --- | --- |
| Reference (final run) | Apple M2 (8) | macOS 27.2 | 3.11.18 | 2 h 8 min | 92: 85 OK, 7 WARNING, 0 FAILED |
| Second | Intel Core i7-7700HQ (8) | Windows 10 | 3.11.18 | 7 h 18 min | 92: 86 OK, 6 WARNING, 0 FAILED |
| Third | AMD Ryzen 7 7800X3D (16) | Windows 11 | 3.11.9 | 2 h 10 min | 92: 65 OK, 3 WARNING, 0 FAILED, 24 NOT CHECKED |

All three runs were made on 21 November 2026, with the versions of `requirements.txt` for the eleven packages that the
notebook checks. Every run finished without an error and without a failed checkpoint. The WARNING entries are among the
documented ones listed under *What the run checks about itself*; the 24 NOT CHECKED entries of the third run are the
comparisons with the pre-test, which need the `validation/` folder that this run did not have.

Compared with the reference run, in both other runs:

- the eight SARIMAX models, in their baseline and selected orders, and the logit model reach the same maximum: the
  log-likelihoods agree within 1.2·10⁻⁸ and the coefficients within 3.4·10⁻⁶ Hessian standard errors;
- no value printed in the article, the Supplementary Material or the response to the reviewers was found to change at
  its printed precision, with one exception: the number of bootstrap replicates that stop at the iteration limit,
  which Supplementary Appendix J.5 gives as 15 of 1,200 (the reference run), is 16 and 17 of 1,200 in the second and
  the third run (Table J.6 is the same in all three);
- the XGBoost results differ by about 2·10⁻⁷ or less, relative;
- 41 of the 150 output files that all three runs wrote are byte-identical, among them the CSV tables of Appendices A,
  B, E, I and J; of the 33 figures 23 are byte-identical and the others differ in at most a few hundred pixels (one
  figure that the article does not use differs in a border line).

Apart from that count, the larger differences are all in outputs that the article does not report, for example fits
that are stopped before they converge (the unscaled solver of Phases 7.2 and 7.3), iteration counts of the
quantile-regression solver and the convergence diagnostics of the SARIMAX fits. Time stamps and durations differ in
every run.

These differences are of the size expected between platforms: numpy and scipy use the linear-algebra library of the
platform (Apple Accelerate on the reference computer, OpenBLAS on the second), and XGBoost tree ensembles depend on the
library version and the platform. On one machine the run is deterministic: the bootstrap and resampling steps use fixed
seeds, and the SARIMAX results do not depend on the number of parallel jobs.

`MANIFEST_SHA256.txt` lists the SHA-256 of every file of the package except itself; check it from the package root with
`shasum -a 256 -c MANIFEST_SHA256.txt` (or `sha256sum -c MANIFEST_SHA256.txt`). In your copy, after a run, the same
command lists the files that differ from the shipped ones: after a run on the shipped results only the notebook,
`RUN_REPORT.md`, `RUN_CHECKPOINTS.csv` and, after a headless run, `RUN_LOG.txt`; after a fresh run also every file
that records time stamps or durations and the files that differ between platforms (see above).

The text files are stored with LF line endings; a Git checkout that converts them to CRLF (`core.autocrlf=true`)
changes their checksums, so check a clone made with

```bash
git clone -c core.autocrlf=false --branch RENE-D-26-09232-R2 https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye.git
```

## Data

| Item | Value |
| --- | --- |
| File | `data/Model_Data.xlsx` |
| Observations | 35,064 (hourly), 1 January 2022 00:00 – 31 December 2025 23:00 |
| Columns | 48 (including `Date` and `Date_Hour`, the time index) |
| SHA-256 | `71e299d35f23f818e059e7e952700fc669ac778823074f10ec68b3f35369a78c` |

The market data are publicly available from the [EPİAŞ Transparency Platform](https://seffaflik.epias.com.tr/home); the
real-time generation series used in the timing check (Appendix J.1) are published by the system operator (TEİAŞ). See
[`data/README.md`](data/README.md) for the sources, a summary of the columns and the checksum.

## Licence

MIT – see [LICENSE](LICENSE). The licence text covers the software and its documentation; this package states no
separate terms for the data file, whose series come from the public platforms named in [`data/README.md`](data/README.md). The
`license: MIT` entry of `CITATION.cff` refers to the same software licence and does not cover the data file.

## How to cite

Please cite the article; `CITATION.cff` gives the article and the release (name and repository address) in
machine-readable form.

```bibtex
@unpublished{akkaya2026solar,
  title  = {Solar PV Penetration, Merit-Order Effects and Balancing Reserve Costs in T{\"u}rkiye's Electricity Market},
  author = {Akkaya, Mustafa An{\i}l and Yetgin, Recep U{\u{g}}ur and Kayal{\i}ca, Mehmet {\"O}zg{\"u}r},
  year   = {2026},
  note   = {Manuscript under review, Renewable Energy (RENE-D-26-09232). Replication package: release RENE-D-26-09232-R2,
            https://github.com/Mustafa-34-byte/Solar-Dual-Impact-Turkiye}
}
```

## Acknowledgements

The authors thank Energy Exchange Istanbul (EPİAŞ) for providing transparent access to the Transparency Platform data.
