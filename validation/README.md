# Reference values of the independent pre-test (20 November 2026)

`pretest_reference_2026-11-20.csv` holds the values of an **independent recomputation of the R2 specification**:
a second implementation by a co-author, on the same data file (SHA-256 `71e299d3…a78c`), recorded in a workbook on
20 November 2026. The file has 4,536 rows: 4,530 values read from that workbook and six rows
(`ESIK.duzeltilmis.gt34.*`: hours with a solar generation share above 34%, in total, as a share and by year) supplied
by the corresponding author by message on 20 November 2026 (`value_kind` = `message`).

**Nothing is estimated from these values.** The notebook only compares its own results with them: after each phase that
has reference values, `compare_with_reference()` writes a table to `results/RUN_REPORT.md` with, per value, this run,
the reference, the difference, the tolerance and the status `match` or `DIFFERS`. A difference is recorded and never
stops the notebook; the total over all tables is checkpoint K90.

## What is compared

The notebook compares a subset of the file. In the final run of release `RENE-D-26-09232-R2` it made **655
comparisons in 24 tables: 651 match, 4 DIFFERS** (`RUN_REPORT.md`, checkpoint K90). The remaining rows are not compared;
among them are the 1,549 rows without a tolerance (1,541 p-values and 8 Hessian condition numbers), which the file
keeps for reference only. Phase 3, Phase 7.2, Phase 9 and the figure exports have no reference values.
The four DIFFERS rows of the final run and their explanation are in the main `README.md` (section *Comparison with the
independent pre-test*): three concern Model 5, for which the pre-test reports the non-invertible mirror image of the
seasonal MA term, and one the Figure I.1 crossover, which the pre-test defines as the last upward crossing.

## Columns

| Column | Meaning |
| --- | --- |
| `id` | key used by the notebook (families below) |
| `value` | reference value |
| `model` | model or series the value belongs to |
| `source_sheet`, `source_cell` | sheet and cell of the pre-test workbook (or the message, for the six `message` rows) |
| `value_kind` | `cell` (full precision, 3,573 rows), `derived` (829), `printed text` (rounded as printed, 128) or `message` (6) |
| `tolerance_class` | group of the tolerance |
| `tol_abs`, `tol_rel` | a value matches if the absolute difference is within `tol_abs` or within `tol_rel` times the absolute reference value; rows with neither are not compared |

## Tolerances

A value matches if `|this run − reference| ≤ tol_abs` or `≤ tol_rel · |reference|`. By class:

| Class | Rows | Tolerance |
| --- | ---: | --- |
| `deterministic` | 433 | absolute 1e-9 or relative 1e-6; five printed values of the GAM report: absolute 5.1e-5 or 0.0051 (half a unit of the last printed digit) |
| `data_summary` | 44 | absolute or relative 1e-9 |
| `logit` | 6 | absolute 1e-9 or relative 1e-6 |
| `sarimax_mcp` | 261 | coefficients relative 2e-4; log-likelihood 0.02, AIC and BIC 0.04, likelihood-ratio statistic 0.05 (absolute); root moduli 0.002; Ljung–Box statistics relative 0.002; Phase 2 / Phase 4 coefficient differences absolute 2e-4 |
| `sarimax_afrr` | 392 | coefficients relative 5e-3; log-likelihood 0.1, AIC and BIC 0.2, likelihood-ratio statistic 0.25 (absolute); root moduli 0.005; Ljung–Box statistics relative 0.01 |
| `sarimax_mcp_arma` / `sarimax_afrr_arma` | 48 / 74 | AR/MA parameters absolute 0.001 / 0.01; innovation variance relative 2e-4 / 2e-3 |
| `standard_error_mcp` / `standard_error_afrr` | 647 / 1,000 | relative 0.01 / 0.03 |
| `quantile_point` | 12 | absolute 1e-9 or relative 1e-4 |
| `quantile_bootstrap` | 12 | relative 0.05 |
| `kink_bootstrap` | 22 | absolute 0.5 or relative 0.05 |
| `specification_constant` | 36 | absolute 1e-9 (counts: observations, parameters, burn-in) |
| `p_value`, `sarimax_mcp_p_value`, `sarimax_afrr_p_value`, `not_compared` | 1,549 | none: not compared |

Printed values (`value_kind` = `printed text`) carry in addition half a unit of their last printed digit. The exact
tolerance of every row is in its `tol_abs` and `tol_rel` columns.

## Key families

`M<model>.tani.*` (Phase 4 diagnostics: log-likelihood, AIC, BIC, roots, observations), `M<model>.coef.<variable>`,
`M<model>.se.<kind>.<variable>` (kinds: OPG, GLS, Hessian, Robust, Cluster_Day, Cluster_Day_duz = with the factor
G/(G−1), HAC24, HAC48), `M<model>.z.*`, `M<model>.p.*`, `M<model>.p_turetilmis.<kind>.<variable>` (p-values derived from
the coefficient and each kind of standard error; 825 rows, not compared), `M<model>.yp.*` (effect per percentage point),
`M<model>.arma.<parameter>`, `P2.kars.*` (Phase 2 / Phase 4 comparison of Supplementary S1.5), `M1ikinci.kabul_edilen_yuksek_tepe.*` (Model 1, the accepted higher of two peaks found by
the pre-test; it is the point reported in Phase 4), `P2.M<model>.*` (Phase 2 baseline models), `LR.M<model>.*`
(likelihood-ratio tests), `LOJ.*` (logit Model 7.1), `C1.<row>.*` (Supplementary Table C.1), `ESIK.*` (hours above the
solar-share thresholds), `A1.*`, `B1.*`, `QR.*`, `KINK.*`, `J1.*`, `J2.*`, `J6.*`, `XGB.*`, `WF.*` (walk-forward
validation), `PDP.*`, `GAM.*`, `GAMRAPOR.*` (GAM report), `KESISIM.*` (crossover points), `OZET.*` (summary sheet).

## Turkish words in keys, sheet names and model labels

The keys, sheet names and model labels are those of the co-author's workbook, in Turkish: the notebook looks the values
up by these keys. Glossary: *tani* = diagnostics; *yp* (yüzde puan) = per percentage point;
*duz*, *duzeltilmis* = adjusted; *turetilmis* = derived; *ayna* = mirror image; *alt* / *ust* = lower /
upper; *basina* = per; *dagilim* = distribution; *en yuksek* = highest; *ESIK* = threshold; *Saat* = hours; *Pay* = share; *KESISIM* = crossover;
*LOJ*, *Lojistik* = logit; *OZET*, *Ozet* = summary; *deger* = value; *kars* = comparison; *fark* = difference; *GAMRAPOR* = GAM report; *ikinci tepe* = second
peak; *kabul edilen yüksek tepe* = accepted higher peak; *kosul sayisi* = condition number; *sabitli* / *sabitsiz* = with
/ without an intercept; sheets *Hizli_Analizler* = quick analyses, *Esik_Sayilari* = threshold counts.
