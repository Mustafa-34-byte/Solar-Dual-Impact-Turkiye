## 2026-11-21 02:40:14 | Setup (new run)

Data file: Model_Data.xlsx, SHA-256 71e299d35f23f818e059e7e952700fc669ac778823074f10ec68b3f35369a78c
Method: R2 final | profile ML (multi-start; certified maximum or plateau) | 12-month terms; Phase 2 (1,1,1) no intercept; Phase 4 MCP (2,0,2) intercept, a-FRR (1,1,2) no intercept | data 71e299d35f23
Python 3.11.18 on macOS-27.2-arm64-arm-64bit (8 logical CPUs); parallel SARIMAX jobs: 4
Packages: numpy 2.3.5, pandas 2.3.3, scipy 1.16.3, statsmodels 0.14.6, scikit-learn 1.8.0, xgboost 3.2.0, patsy 1.0.3, joblib 1.6.0, matplotlib 3.10.9, seaborn 0.13.2, openpyxl 3.1.5
Package versions equal the reference environment.

Checkpoints of this step:
[OK] K05 environment: package versions equal the reference environment: Python 3.11.18; all 11 packages equal the reference environment
[OK] K06 design: a constant for the MCP models only; SARIMAX orders as documented (SARIMAX_METHOD_TAG): Phase 2 (1,1,1) no intercept; MCP (2,0,2) with intercept; a-FRR (1,1,2) no intercept; a constant for the MCP models only; no intercept in a model with d > 0; seasonal part (1,0,1)24 in every model

Warnings raised in this step: none.

## 2026-11-21 02:40:21 | Phase 1: data ingestion and checks

35,064 hourly observations, 2022-01-01 00:00:00 .. 2025-12-31 23:00:00, 47 columns, 1,461 days.
[OK] 35,064 hourly observations on the complete grid 2022-01-01 00:00 .. 2025-12-31 23:00
[OK] no missing values
[OK] 1,461 calendar days
[OK] 'Date' equals the calendar day of the time index
[OK] Month_Sin / Month_Cos on a 12-month cycle (largest deviation 5.6e-17)
[OK] Weekend = Saturday or Sunday
[OK] solar generation share between 0 and 1
Solar generation share: mean 0.068781, standard deviation 0.097876, maximum 0.591603.

Checkpoints of this step:
[OK] K01 data: hourly time index, strictly increasing, no duplicate, no gap: 35,064 time stamps 2022-01-01 00:00:00 .. 2025-12-31 23:00:00 (35,064 hours from the first to the last): step 1 h, strictly increasing, no duplicate, no gap; verify_dataset, complete 2022-2025 grid: OK
[OK] K02 data: Solar_Generation_Share in [0, 1] and equal to solar generation / the total implied by the other shares: range 0.000003 .. 0.591603 (within [0, 1]); largest deviation from Solar_Generation / total generation 1.7e-16 (tolerance 1e-9, 35,064 hours); total generation is implied by the 5 other generation columns (generation / share), which agree to 1.1e-15 (relative); the 6 generation shares sum to at most 0.9682; the denominator itself is not a column of the data file, so a total shared by every share column is not verified here; verify_dataset: OK
[OK] K03 data: calendar terms follow the time index (weekend flag, weekday dummies, hour, month; 12-month and 24-hour cycles): Weekend, Hour, Month, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday equal the calendar of the time index; Month_Sin 5.6e-17, Month_Cos 5.6e-17, Hour_Sin 5.6e-17, Hour_Cos 5.6e-17 largest deviation from the cycle; verify_dataset: weekend OK, month terms OK
[OK] K04 data: no missing value in any column used by a model: no missing value in any of the 47 columns of the data file (they include every model column); verify_dataset: OK

Warnings raised in this step: none.

## 2026-11-21 02:40:21 | Phase 1: solar-share thresholds

16 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                    Quantity     This run    Reference Difference              Tolerance Status
hours with solar share > 20%         4154         4154          0 abs 1e-09 or rel 1e-09  match
            of which in 2022          125          125          0 abs 1e-09 or rel 1e-09  match
            of which in 2023          475          475          0 abs 1e-09 or rel 1e-09  match
            of which in 2024         1371         1371          0 abs 1e-09 or rel 1e-09  match
            of which in 2025         2183         2183          0 abs 1e-09 or rel 1e-09  match
hours with solar share > 34%          729          729          0 abs 1e-09 or rel 1e-09  match
            of which in 2022            0            0          0 abs 1e-09 or rel 1e-09  match
            of which in 2023           10           10          0 abs 1e-09 or rel 1e-09  match
            of which in 2024           89           89          0 abs 1e-09 or rel 1e-09  match
            of which in 2025          630          630          0 abs 1e-09 or rel 1e-09  match
hours with solar share > 45%           79           79          0 abs 1e-09 or rel 1e-09  match
            of which in 2022            0            0          0 abs 1e-09 or rel 1e-09  match
            of which in 2023            0            0          0 abs 1e-09 or rel 1e-09  match
            of which in 2024            4            4          0 abs 1e-09 or rel 1e-09  match
            of which in 2025           75           75          0 abs 1e-09 or rel 1e-09  match
         highest solar share 0.5916025611 0.5916025611          0 abs 1e-09 or rel 1e-09  match
```

Warnings raised in this step: none.

## 2026-11-21 02:59:04 | Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)

9 models. Status: certified: Model 1, Model 2, Model 3, Model 4, Model 5, Model 6, Model 7.2, Model 7.3; converged: Model 7.1.
Warnings stored with the 17 start records in Phase_2/starts: no warning for 17.

```
 Model_ID    Type    Status         LogLik           AIC Best_start  Starts_within_0.01  Iterations  Seconds
  Model 1 SARIMAX certified -258074.817455 516197.634910       grid                 2.0         730    414.6
  Model 2 SARIMAX certified -258104.918718 516271.837437     mirror                 3.0        1092    640.0
  Model 3 SARIMAX certified -258411.916232 516867.832465       grid                 2.0         867    464.4
  Model 4 SARIMAX certified -246142.187112 492332.374223    default                 2.0         650    372.9
  Model 5 SARIMAX certified -246173.768440 492409.536879       grid                 2.0         724    441.3
  Model 6 SARIMAX certified -246830.058956 493704.117913    default                 2.0         679    385.5
Model 7.1   LOGIT converged  -17975.307689  35986.615377        NaN                 NaN           6      0.0
Model 7.2 SARIMAX certified -258460.923000 516965.846000       grid                 2.0         850    441.2
Model 7.3 SARIMAX certified -258316.362744 516684.725488       grid                 2.0         730    387.9
```

- Phase_2/Model_1_summary.csv (9,600 bytes, sha256 95f45f55f0cb)
- Phase_2/Model_2_summary.csv (12,502 bytes, sha256 a05c64e6bee9)
- Phase_2/Model_3_summary.csv (8,736 bytes, sha256 7db53336c68b)
- Phase_2/Model_4_summary.csv (9,415 bytes, sha256 d477a1ea0558)
- Phase_2/Model_5_summary.csv (12,506 bytes, sha256 3dd1ded84853)
- Phase_2/Model_6_summary.csv (8,688 bytes, sha256 1f406e394cf2)
- Phase_2/Model_7.1_summary.csv (2,503 bytes, sha256 cab9459fc3c6)
- Phase_2/Model_7.2_summary.csv (8,718 bytes, sha256 dd21ea6e8b82)
- Phase_2/Model_7.3_summary.csv (10,324 bytes, sha256 7e358ad4200f)
- Phase_2/Phase2_Convergence.csv (11,569 bytes, sha256 3d2eca9e7996)

Checkpoints of this step:
[OK] K10 Phase 2: every reported model certified or plateau: 8 of 8 SARIMAX models certified maxima; Model 7.1 (logit): converged
[OK] K11 Phase 2: reported representation invertible: all 8 reported points invertible; smallest non-seasonal MA root modulus 1.00145, largest |ma.S.L24| 0.9304
[OK] K12 Phase 2: at least two starts within 0.01 of the reported log-likelihood: starts within 0.01 of the reported log-likelihood: Model 1 2, Model 2 3, Model 3 2, Model 4 2, Model 5 2, Model 6 2, Model 7.2 2, Model 7.3 2
[OK] K13 Phase 2: 'const' among the regressors exactly in the models with an intercept: 'const' among the regressors of: none; specification with an intercept: none
[OK] K14 Phase 2: day clusters = calendar days of the estimation sample: day clusters = calendar days of the estimation sample (1,461) for 8 of 8 models (from: day-cluster factor of the standard errors; fit record (n_days))
[OK] K16 Phase 2: no standard-error flag: SE_checks empty for all 8 SARIMAX models
[OK] K45 Phase 2: output files: 10 of 10 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 02:59:04 | Phase 2: baseline models

77 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                  Quantity      This run     Reference       Difference               Tolerance Status
                   Model 1: log-likelihood  -258074.8175  -258074.8175  1.236330718e-07                 abs 0.1  match
           Model 1: Solar_Generation_Share   2026.984825   2026.987113  -0.002288466191  abs 1e-09 or rel 0.005  match
         Model 1: Interaction_Solar_Sunday   3883.067171   3883.069154  -0.001983437284  abs 1e-09 or rel 0.005  match
        Model 1: Interaction_Solar_Holiday     792.01362   792.0155368   -0.00191678541  abs 1e-09 or rel 0.005  match
                            Model 1: ar.L1  0.8799831676  0.8799834899 -3.223156446e-07                abs 0.01  match
                            Model 1: ma.L1 -0.9985547964 -0.9985549024  1.060714417e-07                abs 0.01  match
                         Model 1: ar.S.L24  0.9825218102   0.982521786  2.417850875e-08                abs 0.01  match
                         Model 1: ma.S.L24 -0.8770475451 -0.8770476722  1.271659508e-07                abs 0.01  match
                   Model 2: log-likelihood  -258104.9187  -258104.9187  1.580337994e-08                 abs 0.1  match
             Model 2: Solar_Share_x_Hour_8   3567.360408   3567.361001 -0.0005929999143  abs 1e-09 or rel 0.005  match
             Model 2: Solar_Share_x_Hour_9   2133.151091   2133.154679  -0.003588070545  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_10   1603.660597   1603.665395  -0.004798190915  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_11   3921.152443   3921.152945 -0.0005016474829  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_12   3726.885083   3726.884207  0.0008762850121  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_13   3903.062986   3903.062516  0.0004700764234  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_14   4722.272672   4722.272157  0.0005145719615  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_15   4386.297889   4386.297751  0.0001386827289  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_16   1141.977864   1141.982591  -0.004726958432  abs 1e-09 or rel 0.005  match
            Model 2: Solar_Share_x_Hour_17   5524.577971   5524.579697  -0.001726071414  abs 1e-09 or rel 0.005  match
                            Model 2: ar.L1  0.8829539636  0.8829535901  3.735154709e-07                abs 0.01  match
                            Model 2: ma.L1 -0.9980027944 -0.9980027866 -7.785472822e-09                abs 0.01  match
                         Model 2: ar.S.L24  0.9860184162  0.9860182922  1.239908699e-07                abs 0.01  match
                         Model 2: ma.S.L24 -0.8836487558 -0.8836484838 -2.719681719e-07                abs 0.01  match
                   Model 3: log-likelihood  -258411.9162  -258411.9162  2.782326192e-08                 abs 0.1  match
           Model 3: Interaction_Solar_Peak   1541.246398   1541.242479   0.003919390347  abs 1e-09 or rel 0.005  match
                            Model 3: ar.L1  0.8816276522  0.8816276053  4.697539346e-08                abs 0.01  match
                            Model 3: ma.L1 -0.9978480512 -0.9978480663  1.509945224e-08                abs 0.01  match
                         Model 3: ar.S.L24  0.9866626415  0.9866623625  2.789671557e-07                abs 0.01  match
                         Model 3: ma.S.L24 -0.8830369762 -0.8830362766 -6.995893477e-07                abs 0.01  match
                   Model 4: log-likelihood  -246142.1871  -246142.1871  4.336470738e-09                abs 0.02  match
           Model 4: Solar_Generation_Share  -5835.146881  -5835.146773 -0.0001076236085 abs 1e-09 or rel 0.0002  match
         Model 4: Interaction_Solar_Sunday  -136.7729735  -136.7729644 -9.074276022e-06 abs 1e-09 or rel 0.0002  match
        Model 4: Interaction_Solar_Holiday   317.8442515   317.8444905 -0.0002390484739 abs 1e-09 or rel 0.0002  match
                            Model 4: ar.L1  0.5170757143  0.5170757923 -7.804951641e-08               abs 0.001  match
                            Model 4: ma.L1 -0.9473937294  -0.947393794  6.457657931e-08               abs 0.001  match
                         Model 4: ar.S.L24  0.9946636709  0.9946636065  6.441916278e-08               abs 0.001  match
                         Model 4: ma.S.L24 -0.9304239428 -0.9304238608 -8.201288959e-08               abs 0.001  match
                   Model 5: log-likelihood  -246173.7684  -246173.7684  7.596099749e-09                abs 0.02  match
             Model 5: Solar_Share_x_Hour_8  -6146.074463  -6146.071024    -0.0034387356 abs 1e-09 or rel 0.0002  match
             Model 5: Solar_Share_x_Hour_9  -5628.105773  -5628.103485  -0.002288419821 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_10  -5258.256105  -5258.255109 -0.0009961623455 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_11  -5285.721991  -5285.721395 -0.0005951503699 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_12  -4113.664706  -4113.667086   0.002380024786 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_13   -4404.81705  -4404.818341   0.001290733359 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_14  -5052.459648  -5052.459754  0.0001059459128 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_15   -5812.91272  -5812.912424 -0.0002966093298 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_16  -5468.934843  -5468.934324 -0.0005197865539 abs 1e-09 or rel 0.0002  match
            Model 5: Solar_Share_x_Hour_17  -4563.551443  -4563.550445 -0.0009971844856 abs 1e-09 or rel 0.0002  match
                            Model 5: ar.L1  0.5112523573  0.5112526112 -2.538461521e-07               abs 0.001  match
                            Model 5: ma.L1 -0.9455919001 -0.9455920162  1.161177833e-07               abs 0.001  match
                         Model 5: ar.S.L24  0.9964972185  0.9964971679  5.062153507e-08               abs 0.001  match
                         Model 5: ma.S.L24 -0.9200559789  -0.920055932 -4.692721467e-08               abs 0.001  match
                   Model 6: log-likelihood   -246830.059   -246830.059  4.831235856e-09                abs 0.02  match
           Model 6: Interaction_Solar_Peak  -2089.426731  -2089.426371 -0.0003600921864 abs 1e-09 or rel 0.0002  match
                            Model 6: ar.L1  0.5260426371  0.5260428833 -2.461866413e-07               abs 0.001  match
                            Model 6: ma.L1 -0.9456330739 -0.9456331689  9.506327259e-08               abs 0.001  match
                         Model 6: ar.S.L24  0.9940035234  0.9940034779  4.549963806e-08               abs 0.001  match
                         Model 6: ma.S.L24 -0.9203401829 -0.9203401522 -3.067109688e-08               abs 0.001  match
Model 7.1 (logit): solar share coefficient    8.22080941    8.22080941  3.552713679e-15  abs 1e-09 or rel 1e-06  match
         Model 7.1 (logit): standard error   0.266547132   0.266547132  7.549516567e-15  abs 1e-09 or rel 1e-06  match
         Model 7.1 (logit): log-likelihood  -17975.30769  -17975.30769  3.637978807e-12  abs 1e-09 or rel 1e-06  match
                 Model 7.2: log-likelihood   -258460.923   -258460.923  6.816117093e-08                 abs 0.1  match
          Model 7.2: System_Direction_Down  -16.19766346  -16.19763647 -2.699303801e-05  abs 1e-09 or rel 0.005  match
                          Model 7.2: ar.L1  0.8822372592  0.8822372729 -1.374315906e-08                abs 0.01  match
                          Model 7.2: ma.L1 -0.9977638377 -0.9977639262  8.853887123e-08                abs 0.01  match
                       Model 7.2: ar.S.L24  0.9863437899  0.9863434019  3.880066162e-07                abs 0.01  match
                       Model 7.2: ma.S.L24 -0.8826651048 -0.8826639992 -1.105639438e-06                abs 0.01  match
                 Model 7.3: log-likelihood  -258316.3627  -258316.3627  2.072192729e-08                 abs 0.1  match
         Model 7.3: Solar_Generation_Share   4482.966595   4482.968384  -0.001788533483  abs 1e-09 or rel 0.005  match
          Model 7.3: System_Direction_Down  -14.50793024  -14.50789711 -3.313166522e-05  abs 1e-09 or rel 0.005  match
            Model 7.3: System_Direction_Up  -15.59937248  -15.59937036 -2.112715068e-06  abs 1e-09 or rel 0.005  match
     Model 7.3: Interaction_Solar_Dir_Down  -39.04568459  -39.04563662 -4.796708594e-05  abs 1e-09 or rel 0.005  match
       Model 7.3: Interaction_Solar_Dir_Up    134.335065   134.3348677    0.00019726772  abs 1e-09 or rel 0.005  match
                          Model 7.3: ar.L1  0.8804571468  0.8804575819 -4.351375938e-07                abs 0.01  match
                          Model 7.3: ma.L1 -0.9978583173 -0.9978584113  9.401081136e-08                abs 0.01  match
                       Model 7.3: ar.S.L24  0.9830258987  0.9830256839   2.14865754e-07                abs 0.01  match
                       Model 7.3: ma.S.L24  -0.882112871 -0.8821121125 -7.585236181e-07                abs 0.01  match
```

Checkpoints of this step:
[OK] K17 Phase 2: comparison with the independent pre-test: 77 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 02:59:06 | Phase 3: seasonality diagnostics (ACF/PACF) and order selection note

Lag-24 autocorrelation on the representative subset (four one-week samples): Solar_Generation_Share 0.9135, a-FRR_Price 0.4095, Mcp 0.6626, Consumption 0.8128.
Orders fixed in Phase 4 (preliminary grid search, not re-run here): MCP SARIMAX(2,0,2)(1,0,1)24; a-FRR SARIMAX(1,1,2)(1,0,1)24.
No reference values for this phase in the independent pre-test: nothing to compare.

```
              Variable  Observations  Lag24_Autocorrelation
Solar_Generation_Share           672                 0.9135
           a-FRR_Price           672                 0.4095
                   Mcp           672                 0.6626
           Consumption           672                 0.8128
```

- Phase_3/Phase3_Seasonality_Diagnostics.png (1,574,392 bytes, sha256 65befd677827)
- Phase_3/Phase3_Lag24_Autocorrelation.csv (187 bytes, sha256 11417fee437d)

Checkpoints of this step:
[OK] K45 Phase 3: output files: 2 of 2 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:03:12 | Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)

Status: certified: Model 1, Model 2, Model 3, Model 7.2, Model 7.3, Model 4, Model 5, Model 6.
Likelihood-ratio tests of the solar coefficient: Model 4 LR = 1509.18 (p < 1e-300); Model 1 LR = 46.96 (p = 7.23e-12).
Warnings stored with the 33 start records in Phase_4/starts: no warning for 33.

```
 Model_ID                  Order    Status         LogLik           AIC           BIC Best_start  Starts_within_0.01  Burn  N_days
  Model 1 (1, 1, 2)(1, 0, 1, 24) certified -258034.074053 516118.148107 516329.751392       grid                   2    28    1461
  Model 2 (1, 1, 2)(1, 0, 1, 24) certified -258082.639956 516229.279912 516500.132116     mirror                   3    28    1461
  Model 3 (1, 1, 2)(1, 0, 1, 24) certified -258388.452098 516822.904196 517017.579218       grid                   2    28    1461
Model 7.2 (1, 1, 2)(1, 0, 1, 24) certified -258438.047256 516922.094512 517116.769534     mirror                   3    28    1461
Model 7.3 (1, 1, 2)(1, 0, 1, 24) certified -258288.489147 516630.978293 516859.509840       grid                   2    28    1461
  Model 4 (2, 0, 2)(1, 0, 1, 24) certified -246046.758766 492147.517533 492376.049851    default                   3    27    1461
  Model 5 (2, 0, 2)(1, 0, 1, 24) certified -246075.310471 492218.620941 492506.402378    default                   3    27    1461
  Model 6 (2, 0, 2)(1, 0, 1, 24) certified -246722.817678 493495.635357 493707.239355       grid                   3    27    1461
```

- Phase_4/Phase4_Full_Estimation_Report.txt (120,287 bytes, sha256 b87f93d6aade)
- Phase_4/Phase4_All_Coefficients.csv (77,379 bytes, sha256 5d90320c2a90)
- Phase_4/Phase4_Model_Diagnostics.csv (17,180 bytes, sha256 2ce856670970)
- Phase_4/Phase4_LR_Tests.csv (1,626 bytes, sha256 e3d700d5d36f)
- Phase_4/Phase4_Baseline_vs_Optimized_Solar.csv (1,607 bytes, sha256 c09e70e10059)

Checkpoints of this step:
[OK] K10 Phase 4: every reported model certified or plateau: 8 of 8 SARIMAX models certified maxima
[OK] K11 Phase 4: reported representation invertible: all 8 reported points invertible; smallest non-seasonal MA root modulus 1.00107, largest |ma.S.L24| 0.9249
[OK] K12 Phase 4: at least two starts within 0.01 of the reported log-likelihood: starts within 0.01 of the reported log-likelihood: Model 1 2, Model 2 3, Model 3 2, Model 7.2 3, Model 7.3 2, Model 4 3, Model 5 3, Model 6 3
[OK] K13 Phase 4: 'const' among the regressors exactly in the models with an intercept: 'const' among the regressors of: Model 4, Model 5, Model 6; specification with an intercept: Model 4, Model 5, Model 6
[OK] K14 Phase 4: day clusters = calendar days of the estimation sample: day clusters = calendar days of the estimation sample (1,461) for 8 of 8 models (from: N_days column; day-cluster factor of the standard errors)
[OK] K16 Phase 4: no standard-error flag: SE_checks empty for all 8 SARIMAX models
[OK] K15 Phase 4: likelihood-ratio tests (restricted and unrestricted estimates invertible, consistency flag True): Model 4 (Solar_Generation_Share = 0): unrestricted invertible, restricted invertible (start 'grid'), consistent True; Model 1 (Solar_Generation_Share = 0): unrestricted invertible, restricted invertible (start 'phase2'), consistent True
[OK] K45 Phase 4: output files: 5 of 5 listed files exist and are not empty

Warnings raised in this step (2; category | where | location | message | count; count: main process = times shown, a job = every occurrence):
- UserWarning | main | process_executor.py:787 | A worker stopped while some jobs were given to the executor. This can be caused by a too short worker timeout or by a memory leak. | x2

## 2026-11-21 04:03:12 | Phase 4: rows that differ from the pre-test (mirror image of the seasonal MA term)

Model 5: the pre-test value of ma.S.L24 (-1.0924) is the reciprocal of this run's -0.9154. The pre-test reports the non-invertible mirror image of the same model (higher log-likelihood through the initialisation), this run the invertible representation (setup cell).

Warnings raised in this step: none.

## 2026-11-21 04:03:12 | Phase 4: optimized models

128 match, 3 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                               Quantity       This run      Reference       Difference               Tolerance  Status
                                Model 1: log-likelihood   -258034.0741   -258034.0741  6.588525139e-07                 abs 0.1   match
                                           Model 1: AIC    516118.1481    516118.1481 -1.317588612e-06                 abs 0.2   match
           Model 1: Solar_Generation_Share, coefficient    2015.698036    2015.705747  -0.007710878733  abs 1e-09 or rel 0.005   match
      Model 1: Solar_Generation_Share, day-clustered SE    446.1543157    446.1555825  -0.001266871414                rel 0.03   match
         Model 1: Interaction_Solar_Sunday, coefficient     3881.34015    3881.352731   -0.01258053131  abs 1e-09 or rel 0.005   match
    Model 1: Interaction_Solar_Sunday, day-clustered SE    372.5818633    372.5874546  -0.005591229061                rel 0.03   match
        Model 1: Interaction_Solar_Holiday, coefficient    746.0282662    746.0381124  -0.009846175096  abs 1e-09 or rel 0.005   match
   Model 1: Interaction_Solar_Holiday, day-clustered SE    588.8522572    588.8592461  -0.006988885689                rel 0.03   match
                                         Model 1: ar.L1   0.8924752239   0.8924755357 -3.117410999e-07                abs 0.01   match
                                         Model 1: ma.L1   -1.050124896   -1.050125408  5.119835311e-07                abs 0.01   match
                                         Model 1: ma.L2  0.05114086887  0.05114085694  1.192735865e-08                abs 0.01   match
                                      Model 1: ar.S.L24   0.9824705056   0.9824700991  4.064810448e-07                abs 0.01   match
                                      Model 1: ma.S.L24  -0.8765406842  -0.8765398682 -8.159747644e-07                abs 0.01   match
                                Model 2: log-likelihood     -258082.64     -258082.64  9.243376553e-08                 abs 0.1   match
                                           Model 2: AIC    516229.2799    516229.2799 -1.847511157e-07                 abs 0.2   match
             Model 2: Solar_Share_x_Hour_8, coefficient    3686.865314    3686.872342  -0.007027746484  abs 1e-09 or rel 0.005   match
        Model 2: Solar_Share_x_Hour_8, day-clustered SE    787.3497044    787.3015768    0.04812752635                rel 0.03   match
             Model 2: Solar_Share_x_Hour_9, coefficient    2178.917943    2178.922122  -0.004178593429  abs 1e-09 or rel 0.005   match
        Model 2: Solar_Share_x_Hour_9, day-clustered SE    528.3235246    528.3125222    0.01100239387                rel 0.03   match
            Model 2: Solar_Share_x_Hour_10, coefficient    1623.012063    1623.016256  -0.004192954652  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_10, day-clustered SE    493.3338953    493.3312174   0.002677861167                rel 0.03   match
            Model 2: Solar_Share_x_Hour_11, coefficient    3934.353917    3934.353702  0.0002145774683  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_11, day-clustered SE    559.6058645    559.6017671   0.004097431064                rel 0.03   match
            Model 2: Solar_Share_x_Hour_12, coefficient    3733.593399    3733.592351    0.00104809172  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_12, day-clustered SE    580.3447658    580.3422693   0.002496565022                rel 0.03   match
            Model 2: Solar_Share_x_Hour_13, coefficient    3910.267122    3910.266382   0.000740624901  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_13, day-clustered SE    585.7558699    585.7534467   0.002423215824                rel 0.03   match
            Model 2: Solar_Share_x_Hour_14, coefficient    4732.710344    4732.709388  0.0009565734281  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_14, day-clustered SE    625.0202508    625.0168103   0.003440444535                rel 0.03   match
            Model 2: Solar_Share_x_Hour_15, coefficient    4391.015864    4391.015071  0.0007937557712  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_15, day-clustered SE    598.2398136    598.2397205  9.310486166e-05                rel 0.03   match
            Model 2: Solar_Share_x_Hour_16, coefficient    1165.331689     1165.33385  -0.002160899578  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_16, day-clustered SE    763.2368289    763.2406577  -0.003828790314                rel 0.03   match
            Model 2: Solar_Share_x_Hour_17, coefficient    5531.859221    5531.861499  -0.002277693382  abs 1e-09 or rel 0.005   match
       Model 2: Solar_Share_x_Hour_17, day-clustered SE    1160.550786    1160.551424  -0.000638006178                rel 0.03   match
                                         Model 2: ar.L1   0.8910340305   0.8910342646 -2.340971887e-07                abs 0.01   match
                                         Model 2: ma.L1   -1.032333809   -1.032334658  8.489605048e-07                abs 0.01   match
                                         Model 2: ma.L2  0.03403775294  0.03403853159 -7.786574177e-07                abs 0.01   match
                                      Model 2: ar.S.L24   0.9860351403   0.9860348775  2.628150215e-07                abs 0.01   match
                                      Model 2: ma.S.L24  -0.8835579048  -0.8835565212 -1.383534779e-06                abs 0.01   match
                                Model 3: log-likelihood   -258388.4521   -258388.4521  3.591412678e-08                 abs 0.1   match
                                           Model 3: AIC    516822.9042    516822.9042 -7.182825357e-08                 abs 0.2   match
           Model 3: Interaction_Solar_Peak, coefficient    1548.243698    1548.242355    0.00134261894  abs 1e-09 or rel 0.005   match
      Model 3: Interaction_Solar_Peak, day-clustered SE    294.7273921    294.7265981  0.0007939433136                rel 0.03   match
                                         Model 3: ar.L1   0.8901328289   0.8901328131  1.581106068e-08                abs 0.01   match
                                         Model 3: ma.L1   -1.033519649    -1.03352065  1.000633436e-06                abs 0.01   match
                                         Model 3: ma.L2  0.03533824711  0.03533920408  -9.56974567e-07                abs 0.01   match
                                      Model 3: ar.S.L24   0.9867143585   0.9867141439   2.14589117e-07                abs 0.01   match
                                      Model 3: ma.S.L24  -0.8828918829  -0.8828910947 -7.881843664e-07                abs 0.01   match
                              Model 7.2: log-likelihood   -258438.0473   -258438.0473  1.559383236e-07                 abs 0.1   match
                                         Model 7.2: AIC    516922.0945    516922.0945 -3.117602319e-07                 abs 0.2   match
          Model 7.2: System_Direction_Down, coefficient   -17.03566242   -17.03570783  4.540851883e-05  abs 1e-09 or rel 0.005   match
     Model 7.2: System_Direction_Down, day-clustered SE    6.506018822    6.505990696  2.812623401e-05                rel 0.03   match
                                       Model 7.2: ar.L1   0.8905591282   0.8905591807 -5.251996305e-08                abs 0.01   match
                                       Model 7.2: ma.L1   -1.032738977    -1.03274025  1.273367266e-06                abs 0.01   match
                                       Model 7.2: ma.L2  0.03463562742  0.03463687378 -1.246351544e-06                abs 0.01   match
                                    Model 7.2: ar.S.L24   0.9864095133   0.9864095083  4.986891566e-09                abs 0.01   match
                                    Model 7.2: ma.S.L24  -0.8825286942  -0.8825287538  5.960075278e-08                abs 0.01   match
                              Model 7.3: log-likelihood   -258288.4891   -258288.4894  0.0002401676902                 abs 0.1   match
                                         Model 7.3: AIC    516630.9783    516630.9788 -0.0004803353804                 abs 0.2   match
         Model 7.3: Solar_Generation_Share, coefficient    4474.231913    4474.210284    0.02162945549  abs 1e-09 or rel 0.005   match
    Model 7.3: Solar_Generation_Share, day-clustered SE    458.1058626    458.1214785   -0.01561589798                rel 0.03   match
          Model 7.3: System_Direction_Down, coefficient   -15.24561925   -15.24869576   0.003076508299  abs 1e-09 or rel 0.005   match
     Model 7.3: System_Direction_Down, day-clustered SE    7.991125134    7.991121126  4.007284041e-06                rel 0.03   match
            Model 7.3: System_Direction_Up, coefficient   -16.04452213   -16.04514267   0.000620537932  abs 1e-09 or rel 0.005   match
       Model 7.3: System_Direction_Up, day-clustered SE    6.220272934    6.220254214  1.872049511e-05                rel 0.03   match
     Model 7.3: Interaction_Solar_Dir_Down, coefficient   -46.71301297     -46.728814    0.01580102573  abs 1e-09 or rel 0.005   match
Model 7.3: Interaction_Solar_Dir_Down, day-clustered SE    80.82949162      80.831352  -0.001860378185                rel 0.03   match
       Model 7.3: Interaction_Solar_Dir_Up, coefficient    137.6934077    137.7004407  -0.007032995759  abs 1e-09 or rel 0.005   match
  Model 7.3: Interaction_Solar_Dir_Up, day-clustered SE     71.4124474    71.41342242 -0.0009750169265                rel 0.03   match
                                       Model 7.3: ar.L1   0.8900757471    0.890068997  6.750098546e-06                abs 0.01   match
                                       Model 7.3: ma.L1   -1.038083038   -1.038156996  7.395790538e-05                abs 0.01   match
                                       Model 7.3: ma.L2  0.03988713618  0.03996158125 -7.444506759e-05                abs 0.01   match
                                    Model 7.3: ar.S.L24   0.9829650272   0.9829679095 -2.882314378e-06                abs 0.01   match
                                    Model 7.3: ma.S.L24  -0.8819153288  -0.8819193443  4.015526048e-06                abs 0.01   match
                                Model 4: log-likelihood   -246046.7588   -246046.7588   5.76255843e-08                abs 0.02   match
                                           Model 4: AIC    492147.5175    492147.5175 -1.152511686e-07                abs 0.04   match
           Model 4: Solar_Generation_Share, coefficient   -5780.837983   -5780.836239     -0.001744557 abs 1e-09 or rel 0.0002   match
      Model 4: Solar_Generation_Share, day-clustered SE    207.6989414    207.6989447 -3.247207218e-06                rel 0.01   match
         Model 4: Interaction_Solar_Sunday, coefficient   -176.3133877   -176.3141335  0.0007458295856 abs 1e-09 or rel 0.0002   match
    Model 4: Interaction_Solar_Sunday, day-clustered SE    130.8956948    130.8956951 -3.449749499e-07                rel 0.01   match
        Model 4: Interaction_Solar_Holiday, coefficient     270.891011    270.8900305  0.0009805025351 abs 1e-09 or rel 0.0002   match
   Model 4: Interaction_Solar_Holiday, day-clustered SE    175.4970202    175.4970119  8.304721263e-06                rel 0.01   match
                                         Model 4: ar.L1    1.403872131    1.403867997  4.133639903e-06               abs 0.001   match
                                         Model 4: ar.L2  -0.4096271877  -0.4096232283 -3.959375283e-06               abs 0.001   match
                                         Model 4: ma.L1  -0.8184345437  -0.8184300698 -4.473922885e-06               abs 0.001   match
                                         Model 4: ma.L2 -0.09781123707 -0.09781443464   3.19756992e-06               abs 0.001   match
                                      Model 4: ar.S.L24   0.9939648115   0.9939647394  7.208648445e-08               abs 0.001   match
                                      Model 4: ma.S.L24  -0.9248834542   -0.924883277 -1.772402719e-07               abs 0.001   match
                                Model 5: log-likelihood   -246075.3105   -246075.2881   -0.02240588045                abs 0.02 DIFFERS
                                           Model 5: AIC    492218.6209    492218.5761    0.04481176101                abs 0.04 DIFFERS
             Model 5: Solar_Share_x_Hour_8, coefficient   -6133.939375   -6133.971559    0.03218329342 abs 1e-09 or rel 0.0002   match
        Model 5: Solar_Share_x_Hour_8, day-clustered SE    365.4564969    365.4568095 -0.0003126453423                rel 0.01   match
             Model 5: Solar_Share_x_Hour_9, coefficient   -5664.936843   -5664.949019    0.01217532312 abs 1e-09 or rel 0.0002   match
        Model 5: Solar_Share_x_Hour_9, day-clustered SE    285.3084647    285.3085688 -0.0001041591021                rel 0.01   match
            Model 5: Solar_Share_x_Hour_10, coefficient   -5303.235272   -5303.244288   0.009015456786 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_10, day-clustered SE    246.3766863     246.376826 -0.0001397583176                rel 0.01   match
            Model 5: Solar_Share_x_Hour_11, coefficient   -5343.636488   -5343.646328   0.009840413094 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_11, day-clustered SE    229.9234349    229.9236445 -0.0002096592386                rel 0.01   match
            Model 5: Solar_Share_x_Hour_12, coefficient   -4166.101733    -4166.08998   -0.01175343679 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_12, day-clustered SE    245.7452478    245.7482885  -0.003040716009                rel 0.01   match
            Model 5: Solar_Share_x_Hour_13, coefficient   -4458.831958   -4458.841887   0.009928659519 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_13, day-clustered SE    236.8349992    236.8369636  -0.001964465314                rel 0.01   match
            Model 5: Solar_Share_x_Hour_14, coefficient    -5102.14076   -5102.146693     0.0059324229 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_14, day-clustered SE    238.5480528    238.5485124 -0.0004596427019                rel 0.01   match
            Model 5: Solar_Share_x_Hour_15, coefficient   -5859.380028   -5859.379686 -0.0003417098778 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_15, day-clustered SE    271.3793892    271.3797322 -0.0003430236718                rel 0.01   match
            Model 5: Solar_Share_x_Hour_16, coefficient   -5513.908052   -5513.905917   -0.00213434457 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_16, day-clustered SE    330.2792804    330.2796509 -0.0003704836595                rel 0.01   match
            Model 5: Solar_Share_x_Hour_17, coefficient   -4532.468572   -4532.471108   0.002536413111 abs 1e-09 or rel 0.0002   match
       Model 5: Solar_Share_x_Hour_17, day-clustered SE    432.6077814     432.608789   -0.00100759493                rel 0.01   match
                                         Model 5: ar.L1    1.400545948    1.400551439 -5.491539754e-06               abs 0.001   match
                                         Model 5: ar.L2  -0.4068201786   -0.406825694  5.515452556e-06               abs 0.001   match
                                         Model 5: ma.L1  -0.8204957039  -0.8205024779  6.773936104e-06               abs 0.001   match
                                         Model 5: ma.L2 -0.09342299445 -0.09341751353 -5.480919648e-06               abs 0.001   match
                                      Model 5: ar.S.L24   0.9960951208   0.9960951113  9.509303012e-09               abs 0.001   match
                                      Model 5: ma.S.L24  -0.9154188313   -1.092397418     0.1769785863               abs 0.001 DIFFERS
                                Model 6: log-likelihood   -246722.8177   -246722.8177  5.614128895e-08                abs 0.02   match
                                           Model 6: AIC    493495.6354    493495.6354 -1.122243702e-07                abs 0.04   match
           Model 6: Interaction_Solar_Peak, coefficient   -2209.698315   -2209.701314   0.002999353034 abs 1e-09 or rel 0.0002   match
      Model 6: Interaction_Solar_Peak, day-clustered SE    177.8725408    177.8724657  7.507439406e-05                rel 0.01   match
                                         Model 6: ar.L1     1.40641267    1.406409477  3.193034604e-06               abs 0.001   match
                                         Model 6: ar.L2  -0.4120313473  -0.4120282702 -3.077086678e-06               abs 0.001   match
                                         Model 6: ma.L1  -0.8073640351  -0.8073605712 -3.463942079e-06               abs 0.001   match
                                         Model 6: ma.L2  -0.1063290134  -0.1063314505  2.437097799e-06               abs 0.001   match
                                      Model 6: ar.S.L24   0.9935003167   0.9935002182  9.851354277e-08               abs 0.001   match
                                      Model 6: ma.S.L24  -0.9155573338  -0.9155573984  6.464156754e-08               abs 0.001   match
            LR test, Model 4: restricted log-likelihood   -246801.3478   -246801.3478  1.282198355e-06                abs 0.02   match
                         LR test, Model 4: LR statistic    1509.178159    1509.178161 -2.449146905e-06                abs 0.05   match
            LR test, Model 1: restricted log-likelihood   -258057.5559   -258057.5576   0.001718294894                 abs 0.1   match
                         LR test, Model 1: LR statistic    46.96363242    46.96706769  -0.003435272083                abs 0.25   match
```

Checkpoints of this step:
[WARNING] K17 Phase 4: comparison with the independent pre-test (optimized models): 128 match, 3 DIFFERS, 0 reported without tolerance, 0 without reference; DIFFERS explained by the mirror image of the seasonal MA term in the pre-test: Model 5: log-likelihood, Model 5: AIC, Model 5: ma.S.L24

Warnings raised in this step: none.

## 2026-11-21 04:03:12 | Phase 4: standard errors of the solar coefficient (Models 1 and 4)

16 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                            Quantity    This run   Reference       Difference Tolerance Status
            Model 1: solar share, OPG standard error 220.7523411 220.7519871  0.0003540233751  rel 0.03  match
            Model 1: solar share, GLS standard error   284.02746 284.0267638  0.0006961900671  rel 0.03  match
        Model 1: solar share, Hessian standard error 288.9982594 288.9979459  0.0003135717028  rel 0.03  match
         Model 1: solar share, Robust standard error 403.2128584 403.2162169  -0.003358471998  rel 0.03  match
    Model 1: solar share, Cluster_Day standard error 446.1543157 446.1555825  -0.001266871414  rel 0.03  match
Model 1: solar share, Cluster_Day_adj standard error 446.3070821 446.3083494    -0.0012673052  rel 0.03  match
          Model 1: solar share, HAC24 standard error 440.9238376 440.9256093  -0.001771699705  rel 0.03  match
          Model 1: solar share, HAC48 standard error 460.7913584 460.7939128  -0.002554367248  rel 0.03  match
            Model 4: solar share, OPG standard error 130.4786774 130.4785471  0.0001303458153  rel 0.01  match
            Model 4: solar share, GLS standard error 144.0855862  144.085443  0.0001432124463  rel 0.01  match
        Model 4: solar share, Hessian standard error 144.8767594 144.8766106  0.0001488071907  rel 0.01  match
         Model 4: solar share, Robust standard error 164.1349454 164.1347768  0.0001685749384  rel 0.01  match
    Model 4: solar share, Cluster_Day standard error 207.6989414 207.6989447 -3.247207218e-06  rel 0.01  match
Model 4: solar share, Cluster_Day_adj standard error  207.770059 207.7700623 -3.248319132e-06  rel 0.01  match
          Model 4: solar share, HAC24 standard error 207.0687018 207.0686775  2.426432999e-05  rel 0.01  match
          Model 4: solar share, HAC48 standard error 226.9401773 226.9401679  9.377266991e-06  rel 0.01  match
```

Checkpoints of this step:
[OK] K17 Phase 4: comparison with the independent pre-test (standard errors of the solar coefficient): 16 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:03:16 | Phase 5: daily market profiles and hourly SARIMAX coefficients (figures)

Bar figures: hourly Solar_Share_x_Hour coefficients (hours 8-17) read from '../results/Phase_4/Phase4_All_Coefficients.csv'.
Model 5 (MCP): -6,134 to -4,166 TL/MWh per unit of solar share.
Model 2 (a-FRR): 1,165 to 5,532 TL/MW per unit of solar share.

```
 Hour      Model 5     Model 2
    8 -6133.939375 3686.865314
    9 -5664.936843 2178.917943
   10 -5303.235272 1623.012063
   11 -5343.636488 3934.353917
   12 -4166.101733 3733.593399
   13 -4458.831958 3910.267122
   14 -5102.140760 4732.710344
   15 -5859.380028 4391.015864
   16 -5513.908052 1165.331689
   17 -4532.468572 5531.859221
```

- Phase_5/Phase_5_Figure_1_Daily_Market_Profile.png (1,675,770 bytes, sha256 53d0e273c7ae)
- Phase_5/Phase_5_Figure_2_Daily_Market_Profile.png (1,734,534 bytes, sha256 517f99b35904)
- Phase_5/Phase_5_Figure_4_Hourly_Merit_Order_Effect_MCP.png (469,757 bytes, sha256 cbd2800ac1fe)
- Phase_5/Phase_5_Figure_6_Hourly_Volatility_Effect_aFRR.png (453,351 bytes, sha256 efaeaa0f8a82)
- Phase_4/Phase4_All_Coefficients.csv (77,379 bytes, sha256 5d90320c2a90)

Checkpoints of this step:
[OK] K45 Phase 5: output files: 5 of 5 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:03:16 | Phase 5: hourly coefficients drawn in the bar figures (Phase 4 file)

20 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                      Quantity     This run    Reference       Difference               Tolerance Status
 Model 5: Solar_Share_x_Hour_8 -6133.939375 -6133.971559    0.03218329342 abs 1e-09 or rel 0.0002  match
 Model 5: Solar_Share_x_Hour_9 -5664.936843 -5664.949019    0.01217532312 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_10 -5303.235272 -5303.244288   0.009015456786 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_11 -5343.636488 -5343.646328   0.009840413094 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_12 -4166.101733  -4166.08998   -0.01175343679 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_13 -4458.831958 -4458.841887   0.009928659519 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_14  -5102.14076 -5102.146693     0.0059324229 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_15 -5859.380028 -5859.379686 -0.0003417098778 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_16 -5513.908052 -5513.905917   -0.00213434457 abs 1e-09 or rel 0.0002  match
Model 5: Solar_Share_x_Hour_17 -4532.468572 -4532.471108   0.002536413111 abs 1e-09 or rel 0.0002  match
 Model 2: Solar_Share_x_Hour_8  3686.865314  3686.872342  -0.007027746484  abs 1e-09 or rel 0.005  match
 Model 2: Solar_Share_x_Hour_9  2178.917943  2178.922122  -0.004178593429  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_10  1623.012063  1623.016256  -0.004192954652  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_11  3934.353917  3934.353702  0.0002145774683  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_12  3733.593399  3733.592351    0.00104809172  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_13  3910.267122  3910.266382   0.000740624901  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_14  4732.710344  4732.709388  0.0009565734281  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_15  4391.015864  4391.015071  0.0007937557712  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_16  1165.331689   1165.33385  -0.002160899578  abs 1e-09 or rel 0.005  match
Model 2: Solar_Share_x_Hour_17  5531.859221  5531.861499  -0.002277693382  abs 1e-09 or rel 0.005  match
```

Checkpoints of this step:
[OK] K17 Phase 5: comparison with the independent pre-test: 20 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:03:24 | Phase 6.1: XGBoost partial dependence on the solar generation share

MCP (Figure 4): 2,626.029 at a solar share of 0.00% -> 1,294.868 at 27.69% (100 grid points).
a-FRR price (Figure 6): 1,277.781 at a solar share of 0.00% -> 3,768.265 at 27.69% (100 grid points).
P(surplus) (Figure 7, left): 0.179 at a solar share of 0.00% -> 0.518 at 27.69% (100 grid points).
xgboost 3.2.0 in this kernel (a cached file keeps the values of the session that fitted the models). Tree ensembles depend on library version and platform: agreement with the pre-test is expected in the reference environment only.

- Phase_6/Phase_6_Figure_5_PDP_Merit_Order_and_Volatility.png (722,050 bytes, sha256 a771556ea9ed)
- Phase_6/Phase_6_Figure_7_PDP_Merit_Order_and_Volatility.png (723,501 bytes, sha256 f0a1cc20d115)
- Phase_6/Phase_6_Figure_8_Surplus_Probability_and_Distribution.png (1,219,063 bytes, sha256 502199ef17c4)
- Phase_6/Phase_6_1_PDP_Values.csv (17,834 bytes, sha256 ce2148f3025f)

Checkpoints of this step:
[OK] K41 Phase 6.1: partial-dependence values: 3 of 3 curves present with finite values (300 grid points in all)
[OK] K45 Phase 6.1: output files: 4 of 4 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:03:24 | Phase 6.1: partial dependence, every 10th grid point of each curve

30 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                            Quantity     This run    Reference       Difference              Tolerance Status
               MCP (Figure 4), grid point 10 (2.52%)  2585.314209  2585.314209                0 abs 1e-09 or rel 1e-06  match
               MCP (Figure 4), grid point 20 (5.32%)  2479.120605  2479.120605                0 abs 1e-09 or rel 1e-06  match
               MCP (Figure 4), grid point 30 (8.11%)  2377.154541  2377.154541                0 abs 1e-09 or rel 1e-06  match
              MCP (Figure 4), grid point 40 (10.91%)  2220.447266  2220.447266                0 abs 1e-09 or rel 1e-06  match
              MCP (Figure 4), grid point 50 (13.71%)  2196.199463  2196.199463                0 abs 1e-09 or rel 1e-06  match
              MCP (Figure 4), grid point 60 (16.50%)  1899.437622  1899.437622  4.547473509e-13 abs 1e-09 or rel 1e-06  match
              MCP (Figure 4), grid point 70 (19.30%)  1778.732056  1778.732056  4.547473509e-13 abs 1e-09 or rel 1e-06  match
              MCP (Figure 4), grid point 80 (22.10%)  1616.597412  1616.597412                0 abs 1e-09 or rel 1e-06  match
              MCP (Figure 4), grid point 90 (24.90%)  1569.824463  1569.824463                0 abs 1e-09 or rel 1e-06  match
             MCP (Figure 4), grid point 100 (27.69%)  1294.867554  1294.867554 -4.547473509e-13 abs 1e-09 or rel 1e-06  match
       a-FRR price (Figure 6), grid point 10 (2.52%)  1466.623047  1466.623047                0 abs 1e-09 or rel 1e-06  match
       a-FRR price (Figure 6), grid point 20 (5.32%)  1541.898682  1541.898682                0 abs 1e-09 or rel 1e-06  match
       a-FRR price (Figure 6), grid point 30 (8.11%)  1650.873657  1650.873657  4.547473509e-13 abs 1e-09 or rel 1e-06  match
      a-FRR price (Figure 6), grid point 40 (10.91%)  1750.258911  1750.258911  4.547473509e-13 abs 1e-09 or rel 1e-06  match
      a-FRR price (Figure 6), grid point 50 (13.71%)  2003.627197  2003.627197                0 abs 1e-09 or rel 1e-06  match
      a-FRR price (Figure 6), grid point 60 (16.50%)  2114.184326  2114.184326                0 abs 1e-09 or rel 1e-06  match
      a-FRR price (Figure 6), grid point 70 (19.30%)  2388.750488  2388.750488                0 abs 1e-09 or rel 1e-06  match
      a-FRR price (Figure 6), grid point 80 (22.10%)  2833.238037  2833.238037                0 abs 1e-09 or rel 1e-06  match
      a-FRR price (Figure 6), grid point 90 (24.90%)  3477.756592  3477.756592                0 abs 1e-09 or rel 1e-06  match
     a-FRR price (Figure 6), grid point 100 (27.69%)  3768.265381  3768.265381                0 abs 1e-09 or rel 1e-06  match
  P(surplus) (Figure 7, left), grid point 10 (2.52%) 0.1608387381 0.1608387381  2.775557562e-17 abs 1e-09 or rel 1e-06  match
  P(surplus) (Figure 7, left), grid point 20 (5.32%) 0.2236743867 0.2236743867  2.775557562e-17 abs 1e-09 or rel 1e-06  match
  P(surplus) (Figure 7, left), grid point 30 (8.11%)  0.247823894  0.247823894  5.551115123e-17 abs 1e-09 or rel 1e-06  match
 P(surplus) (Figure 7, left), grid point 40 (10.91%) 0.2707384825 0.2707384825  5.551115123e-17 abs 1e-09 or rel 1e-06  match
 P(surplus) (Figure 7, left), grid point 50 (13.71%) 0.3163425326 0.3163425624 -2.980232239e-08 abs 1e-09 or rel 1e-06  match
 P(surplus) (Figure 7, left), grid point 60 (16.50%) 0.3257728815 0.3257728815  5.551115123e-17 abs 1e-09 or rel 1e-06  match
 P(surplus) (Figure 7, left), grid point 70 (19.30%) 0.4523549974 0.4523549676  2.980232244e-08 abs 1e-09 or rel 1e-06  match
 P(surplus) (Figure 7, left), grid point 80 (22.10%) 0.4107814729 0.4107814729  5.551115123e-17 abs 1e-09 or rel 1e-06  match
 P(surplus) (Figure 7, left), grid point 90 (24.90%) 0.4957985282 0.4957985282                0 abs 1e-09 or rel 1e-06  match
P(surplus) (Figure 7, left), grid point 100 (27.69%) 0.5177692771 0.5177692771                0 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Phase 6.1: comparison with the independent pre-test: 30 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:03:26 | Phase 6.2: flexibility trap (XGBoost interaction simulation)

Crossover (the surplus curve stays above the deficit/balanced curve from there to 45%): 34.34% solar share.
Upward crossings: 23.96; 28.35; 34.34 | downward crossings: 1.38; 27.84; 28.50 (% solar share).
Flexibility Trap zone: 37.3% of the 0-45% range; curves saved at 100 grid points.
xgboost 3.2.0 (version of the fit). Tree ensembles depend on library version and platform: agreement with the pre-test is expected in the reference environment only.

- Phase_6/Phase_6_Figure_9_Flexibility_Trap.png (1,529,362 bytes, sha256 3941fd4a75cd)
- Phase_6/Phase_6_2_Flexibility_Trap_Crossover.csv (398 bytes, sha256 688a13957131)
- Phase_6/Phase_6_2_Flexibility_Trap_Curves.csv (4,843 bytes, sha256 edd26ffcf944)

Checkpoints of this step:
[OK] K42 Phase 6.2: flexibility-trap crossover: crossover = the last upward crossing of the surplus curve over the deficit/balanced curve after which it stays above up to the end of the common range (0-45%; linear interpolation between the grid points): 34.34% solar share; upward crossings: 23.96; 28.35; 34.34; downward crossings: 1.38; 27.84; 28.50 (% solar share)
[OK] K45 Phase 6.2: output files: 3 of 3 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:03:26 | Phase 6.2: crossover of the flexibility-trap curves

1 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                Quantity    This run   Reference Difference              Tolerance Status
Crossover, % solar share 34.34155975 34.34155975          0 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Phase 6.2: comparison with the independent pre-test: 1 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:03:31 | Phase 6.4: out-of-sample validation of the XGBoost models (5-fold expanding window)

Out-of-sample R2 (mean of the held-out folds): MCP 0.539, a-FRR 0.426 (in-sample: 0.933 and 0.907).
System direction: accuracy 0.693 against a majority-class baseline of 0.722; ROC-AUC 0.654.
xgboost 3.2.0 in this kernel (a cached file keeps the values of the session that fitted the models). Tree ensembles depend on library version and platform: agreement with the pre-test is expected in the reference environment only.

```
                       Target        MAE        RMSE   R2_oos  Accuracy       F1  R2_insample  Accuracy_insample  ROC_AUC  Balanced_Acc  Majority_baseline_acc
                  MCP (price) 404.394409  521.597908 0.539240       NaN      NaN     0.932548                NaN      NaN           NaN                    NaN
                a-FRR (price) 653.312707 1036.891215 0.426276       NaN      NaN     0.907139                NaN      NaN           NaN                    NaN
System direction (classifier)        NaN         NaN      NaN  0.692813 0.357136          NaN            0.86037 0.654131       0.58043               0.721595
```

- Phase_6/Phase_6_4_Out_of_Sample_CV.csv (444 bytes, sha256 cefe37ddbde6)
- Phase_6/Phase_6_4_Out_of_Sample_CV_Folds.csv (2,283 bytes, sha256 da9f18263d10)

Checkpoints of this step:
[OK] K41 Phase 6.4: walk-forward folds and fit metrics: folds per target: MCP (price) 5, a-FRR (price) 5, System direction (classifier) 5 (configured: 5); every fit measure finite
[OK] K45 Phase 6.4: output files: 2 of 2 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:03:31 | Phase 6.4: walk-forward validation (fold averages)

14 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                            Quantity     This run    Reference       Difference              Tolerance Status
                                    MCP (price): MAE   404.394409   404.394409 -5.684341886e-14 abs 1e-09 or rel 1e-06  match
                                   MCP (price): RMSE   521.597908   521.597908                0 abs 1e-09 or rel 1e-06  match
                                 MCP (price): R2_oos 0.5392400176 0.5392400176                0 abs 1e-09 or rel 1e-06  match
                            MCP (price): R2_insample 0.9325476128 0.9325476128                0 abs 1e-09 or rel 1e-06  match
                                  a-FRR (price): MAE  653.3127075  653.3127075                0 abs 1e-09 or rel 1e-06  match
                                 a-FRR (price): RMSE  1036.891215  1036.891215  2.273736754e-13 abs 1e-09 or rel 1e-06  match
                               a-FRR (price): R2_oos  0.426275791  0.426275791                0 abs 1e-09 or rel 1e-06  match
                          a-FRR (price): R2_insample 0.9071390577 0.9071390577  1.110223025e-16 abs 1e-09 or rel 1e-06  match
             System direction (classifier): Accuracy 0.6928131417 0.6928131417                0 abs 1e-09 or rel 1e-06  match
                   System direction (classifier): F1 0.3571360761 0.3571360761  5.551115123e-17 abs 1e-09 or rel 1e-06  match
    System direction (classifier): Accuracy_insample 0.8603696099 0.8603696099                0 abs 1e-09 or rel 1e-06  match
              System direction (classifier): ROC_AUC 0.6541305485 0.6541305186  2.996317972e-08 abs 1e-09 or rel 1e-06  match
         System direction (classifier): Balanced_Acc 0.5804300781 0.5804300781                0 abs 1e-09 or rel 1e-06  match
System direction (classifier): Majority_baseline_acc 0.7215947981 0.7215947981                0 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Phase 6.4: comparison with the independent pre-test: 14 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:03:35 | Phase 7.1 - Quantile regression (Q10, Q50, Q90)

Solar coefficient per unit solar share (0-1): MCP Q10 -4,976.6; MCP Q50 -5,229.2; MCP Q90 -2,425.0; aFRR Q10 1,249.2; aFRR Q50 5,620.7; aFRR Q90 12,069.8.

```
Hypothesis  Quantile         Coef  Pval
       MCP       0.1 -4976.575266   0.0
       MCP       0.5 -5229.221625   0.0
       MCP       0.9 -2425.011092   0.0
      aFRR       0.1  1249.186905   0.0
      aFRR       0.5  5620.679588   0.0
      aFRR       0.9 12069.789174   0.0
```

- Phase_7/Phase_7_Robustness_Quantile_Regression_Results.txt (1,018 bytes, sha256 4a4d9a72235a)
- Phase_7/Phase_7_Quantile_Regression_Coefficients.csv (217 bytes, sha256 ad45a1a9302b)
- Phase_7/Phase_7_Figure_11_Quantile_Regression_Coefficient_Robustness.png (828,391 bytes, sha256 6c5926b4c7cd)

Checkpoints of this step:
[OK] K30 Phase 7.1: full-sample quantile regressions converged: 6 of 6 fits converged before the 5,000-iteration limit (IRLS iterations 275 to 834)
[OK] K45 Phase 7.1: output files: 3 of 3 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:03:35 | Phase 7.1 - quantile-regression point estimates

12 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                   Quantity     This run    Reference       Difference               Tolerance Status
 MCP Q10 solar coefficient (per unit share) -4976.575266 -4976.575266  3.847526386e-08 abs 1e-09 or rel 0.0001  match
 MCP Q50 solar coefficient (per unit share) -5229.221625 -5229.221625  -1.64883204e-07 abs 1e-09 or rel 0.0001  match
 MCP Q90 solar coefficient (per unit share) -2425.011092 -2425.012764   0.001672061513 abs 1e-09 or rel 0.0001  match
aFRR Q10 solar coefficient (per unit share)  1249.186905  1249.186901  3.618437177e-06 abs 1e-09 or rel 0.0001  match
aFRR Q50 solar coefficient (per unit share)  5620.679588   5620.67959 -1.706761395e-06 abs 1e-09 or rel 0.0001  match
aFRR Q90 solar coefficient (per unit share)  12069.78917  12069.78917   1.59479896e-07 abs 1e-09 or rel 0.0001  match
        MCP Q10 effect per percentage point -49.76575266 -49.76575266   3.84801524e-10 abs 1e-09 or rel 0.0001  match
        MCP Q50 effect per percentage point -52.29221625 -52.29221625  -1.64884284e-09 abs 1e-09 or rel 0.0001  match
        MCP Q90 effect per percentage point -24.25011092 -24.25012764  1.672061516e-05 abs 1e-09 or rel 0.0001  match
       aFRR Q10 effect per percentage point  12.49186905  12.49186901  3.618435329e-08 abs 1e-09 or rel 0.0001  match
       aFRR Q50 effect per percentage point  56.20679588   56.2067959   -1.7067606e-08 abs 1e-09 or rel 0.0001  match
       aFRR Q90 effect per percentage point  120.6978917  120.6978917  1.594386845e-09 abs 1e-09 or rel 0.0001  match
```

Checkpoints of this step:
[OK] K17 Phase 7.1: comparison with the independent pre-test: 12 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:05:02 | Phase 7.2 - QR solver iteration sensitivity (unscaled regressors)

Fits stopped at the iteration limit: 6 of 6 at 1,000 iterations; 6 of 6 at 2,000 iterations; 6 of 6 at 5,000 iterations; 6 of 6 at 10,000 iterations.
Phase 7 call of the first submission, re-run (formula interface, unscaled regressors, 2,000 iterations): 6 of 6 fits stopped at the iteration limit (marked * in the printed table).
Largest spread of the solar coefficient across the iteration budgets: 3,157.1.
No reference values exist for this step (the pre-test file holds the converged estimates only).

```
Hypothesis  Quantile  Coef_iter1000  Converged_iter1000  Coef_iter2000  Converged_iter2000  Coef_iter5000  Converged_iter5000  Coef_iter10000  Converged_iter10000  Phase7_Code_Rerun
       MCP       0.1        -4905.1               False        -4928.3               False        -4963.7               False         -4953.0                False            -4943.0
       MCP       0.5        -5220.3               False        -4004.1               False        -3873.3               False         -5098.5                False            -5200.2
       MCP       0.9        -2403.0               False        -2345.8               False        -1882.0               False         -2378.6                False            -1213.4
      aFRR       0.1         1241.0               False          397.3               False          938.6               False          1239.7                False              431.6
      aFRR       0.5         2132.1               False         5119.5               False         3249.4               False          5013.0                False             5114.0
      aFRR       0.9        11424.7               False        10915.4               False         8851.0               False         12008.1                False            11553.1
```

- Phase_7/Phase_7_2_QR_Iteration_Sensitivity.csv (593 bytes, sha256 c599b5d8e723)

Checkpoints of this step:
[OK] K31 Phase 7.2: iteration-limit marks: fits at the iteration limit (by design, unscaled regressors): 6 of 6 at 1,000 iterations; 6 of 6 at 2,000 iterations; 6 of 6 at 5,000 iterations; 6 of 6 at 10,000 iterations; re-run of the first-submission call: 6 of 6 at 2,000 iterations; the marks agree with the iteration counts of the fits and with the CSV
[OK] K45 Phase 7.2: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:08:55 | Phase 7.3 - Exact QR solution (linear programming) vs IRLS

Largest absolute difference of the solar coefficient from the exact LP solution: scaled IRLS 0.0, unscaled IRLS (1,000 iterations) 3,488.6.
Fits that converged: scaled IRLS 6 of 6, unscaled IRLS 0 of 6.
Largest check loss relative to the exact LP solution: scaled IRLS 1.000000, unscaled IRLS 1.025770.

```
Hypothesis  Quantile  Coef_Exact_LP  Coef_Scaled_IRLS  Coef_Unscaled_IRLS_1000  Loss_Exact_LP  Loss_Scaled_IRLS  Loss_Unscaled_IRLS_1000  Scaled_IRLS_Converged  Unscaled_IRLS_Converged
       MCP       0.1        -4976.6           -4976.6                  -4905.1        2724428           2724428                  2725206                   True                    False
       MCP       0.5        -5229.2           -5229.2                  -5220.3        6062773           6062773                  6062778                   True                    False
       MCP       0.9        -2425.0           -2425.0                  -2403.0        2271294           2271294                  2271302                   True                    False
      aFRR       0.1         1249.2            1249.2                   1241.0        3076814           3076814                  3076818                   True                    False
      aFRR       0.5         5620.7            5620.7                   2132.1       10530518          10530518                 10801891                   True                    False
      aFRR       0.9        12069.8           12069.8                  11424.7        6294198           6294198                  6299176                   True                    False
```

- Phase_7/Phase_7_3_QR_Exact_Solution.csv (578 bytes, sha256 e474e36e8ec0)

Checkpoints of this step:
[OK] K30 Phase 7.3: exact LP solutions and scaled IRLS fits converged: scaled IRLS (5,000 iterations): 6 of 6 converged; exact LP (HiGHS): 6 of 6 solved
[OK] K45 Phase 7.3: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:08:55 | Phase 7.3 - exact (LP) quantile-regression point estimates

6 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                             Quantity This run    Reference     Difference               Tolerance Status
 MCP Q10 solar coefficient, exact LP (per unit share)  -4976.6 -4976.575266 -0.02473383266 abs 1e-09 or rel 0.0001  match
 MCP Q50 solar coefficient, exact LP (per unit share)  -5229.2 -5229.221625  0.02162472032 abs 1e-09 or rel 0.0001  match
 MCP Q90 solar coefficient, exact LP (per unit share)    -2425 -2425.012764  0.01276422324 abs 1e-09 or rel 0.0001  match
aFRR Q10 solar coefficient, exact LP (per unit share)   1249.2  1249.186901   0.0130989891 abs 1e-09 or rel 0.0001  match
aFRR Q50 solar coefficient, exact LP (per unit share)   5620.7   5620.67959  0.02041046376 abs 1e-09 or rel 0.0001  match
aFRR Q90 solar coefficient, exact LP (per unit share)  12069.8  12069.78917  0.01082656554 abs 1e-09 or rel 0.0001  match
```

Checkpoints of this step:
[OK] K17 Phase 7.3: comparison with the independent pre-test: 6 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:28:27 | Phase 7.4 - Day-clustered block-bootstrap QR standard errors (Supplementary Table J6)

Successful bootstrap replications per estimate: 200 to 200 of 200 (seed 42, whole days resampled).
Bootstrap replicates whose IRLS fit stopped at the 5,000-iteration limit (kept in the standard error): MCP Q10 0; MCP Q50 4; MCP Q90 3; aFRR Q10 6; aFRR Q50 1; aFRR Q90 1 (15 of 1,200 replicates).
Diagnostic (not used in Table J6): clustered SE with these replicates re-solved with up to 50,000 iterations: MCP Q10 142.1 (reported 142.1); MCP Q50 125.3 (reported 125.3); MCP Q90 122.1 (reported 122.1); aFRR Q10 154.8 (reported 154.8); aFRR Q50 377.2 (reported 377.2); aFRR Q90 641.3 (reported 641.3); re-solved replicates still at the limit: 0.
|t| of the solar coefficient: 8.07 to 41.72; |t| > 2.58 in 6 of 6 estimates.

```
Hypothesis  Quantile    Coef  Clustered_SE  t_stat Sig  Boot_OK
       MCP       0.1 -4976.6         142.1  -35.03 ***      200
       MCP       0.5 -5229.2         125.3  -41.72 ***      200
       MCP       0.9 -2425.0         122.1  -19.86 ***      200
      aFRR       0.1  1249.2         154.8    8.07 ***      200
      aFRR       0.5  5620.7         377.2   14.90 ***      200
      aFRR       0.9 12069.8         641.3   18.82 ***      200
```

- Phase_7/Phase_7_4_QR_Clustered_Bootstrap_SE.csv (275 bytes, sha256 38a5a9a5fb02)

Checkpoints of this step:
[OK] K30 Phase 7.4: full-sample quantile regressions converged: 6 of 6 fits converged before the 5,000-iteration limit (IRLS iterations 275 to 834)
[OK] K32 Phase 7.4: bootstrap replicates without an error: 200 of 200 replicates without an error for each of the 6 estimates
[WARNING] K32 Phase 7.4: bootstrap replicates at the iteration limit: 15 of 1,200 replicates (1.25%) stopped at the 5,000-iteration limit and are kept in the standard error: MCP Q10 0 of 200 (0.0%); MCP Q50 4 of 200 (2.0%); MCP Q90 3 of 200 (1.5%); aFRR Q10 6 of 200 (3.0%); aFRR Q50 1 of 200 (0.5%); aFRR Q90 1 of 200 (0.5%); diagnostic re-solve with up to 50,000 iterations: 0 still at the limit, largest change of the clustered SE 0.002% (Table J6 keeps the replicates as estimated)
[OK] K45 Phase 7.4: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:28:27 | Phase 7.4 - quantile regression with day-clustered bootstrap (Table J6)

30 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                   Quantity This run    Reference       Difference               Tolerance Status
 MCP Q10 solar coefficient (per unit share)  -4976.6 -4976.575266   -0.02473383266 abs 1e-09 or rel 0.0001  match
        MCP Q10 effect per percentage point  -49.766 -49.76575266 -0.0002473383265 abs 1e-09 or rel 0.0001  match
             MCP Q10 clustered bootstrap SE    142.1  142.0743211    0.02567891588                rel 0.05  match
                        MCP Q10 t statistic   -35.03 -35.02797147  -0.002028525685                rel 0.05  match
  MCP Q10 successful bootstrap replications      200          200                0  abs 1e-09 or rel 1e-09  match
 MCP Q50 solar coefficient (per unit share)  -5229.2 -5229.221625    0.02162472032 abs 1e-09 or rel 0.0001  match
        MCP Q50 effect per percentage point  -52.292 -52.29221625  0.0002162472032 abs 1e-09 or rel 0.0001  match
             MCP Q50 clustered bootstrap SE    125.3  125.3464227   -0.04642272832                rel 0.05  match
                        MCP Q50 t statistic   -41.72 -41.71815606  -0.001843941774                rel 0.05  match
  MCP Q50 successful bootstrap replications      200          200                0  abs 1e-09 or rel 1e-09  match
 MCP Q90 solar coefficient (per unit share)    -2425 -2425.012764    0.01276422324 abs 1e-09 or rel 0.0001  match
        MCP Q90 effect per percentage point   -24.25 -24.25012764  0.0001276422324 abs 1e-09 or rel 0.0001  match
             MCP Q90 clustered bootstrap SE    122.1  122.0966605   0.003339538308                rel 0.05  match
                        MCP Q90 t statistic   -19.86 -19.86141763   0.001417626439                rel 0.05  match
  MCP Q90 successful bootstrap replications      200          200                0  abs 1e-09 or rel 1e-09  match
aFRR Q10 solar coefficient (per unit share)   1249.2  1249.186901     0.0130989891 abs 1e-09 or rel 0.0001  match
       aFRR Q10 effect per percentage point   12.492  12.49186901   0.000130989891 abs 1e-09 or rel 0.0001  match
            aFRR Q10 clustered bootstrap SE    154.8  154.7280274     0.0719725973                rel 0.05  match
                       aFRR Q10 t statistic     8.07  8.073436481  -0.003436480643                rel 0.05  match
 aFRR Q10 successful bootstrap replications      200          200                0  abs 1e-09 or rel 1e-09  match
aFRR Q50 solar coefficient (per unit share)   5620.7   5620.67959    0.02041046376 abs 1e-09 or rel 0.0001  match
       aFRR Q50 effect per percentage point   56.207   56.2067959  0.0002041046376 abs 1e-09 or rel 0.0001  match
            aFRR Q50 clustered bootstrap SE    377.2   377.162201     0.0377990386                rel 0.05  match
                       aFRR Q50 t statistic     14.9  14.90255274   -0.00255273516                rel 0.05  match
 aFRR Q50 successful bootstrap replications      200          200                0  abs 1e-09 or rel 1e-09  match
aFRR Q90 solar coefficient (per unit share)  12069.8  12069.78917    0.01082656554 abs 1e-09 or rel 0.0001  match
       aFRR Q90 effect per percentage point  120.698  120.6978917   0.000108265655 abs 1e-09 or rel 0.0001  match
            aFRR Q90 clustered bootstrap SE    641.3  641.2529788    0.04702116614                rel 0.05  match
                       aFRR Q90 t statistic    18.82  18.82219588  -0.002195875618                rel 0.05  match
 aFRR Q90 successful bootstrap replications      200          200                0  abs 1e-09 or rel 1e-09  match
```

Checkpoints of this step:
[OK] K17 Phase 7.4: comparison with the independent pre-test: 30 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:28:29 | Phase 8.1 - GAM flexibility-stress pattern (Supplementary Figure K.1)

Fitted a-FRR price, deficit+balanced minus surplus: 147.28 TL/MW at the lowest solar share and -477.86 TL/MW at the highest (ratio -3.24x).
Read from the saved text report; the fitted curves and their 95% confidence bands are in the figure.

- Phase_8/Phase_8_Flexibility_Stress_Report.txt (336 bytes, sha256 5214a8bd89ba)
- Phase_8/Phase_8_Figure_10_GAM_Flexibility_Stress.png (1,344,798 bytes, sha256 65fc32b40770)

Checkpoints of this step:
[OK] K45 Phase 8.1: output files: 2 of 2 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:28:29 | Phase 8.1 - GAM report vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)

3 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                  Quantity This run Reference Difference               Tolerance Status
Starting price gap (TL/MW)   147.28    147.28          0 abs 0.0051 or rel 1e-06  match
  Ending price gap (TL/MW)  -477.86   -477.86          0 abs 0.0051 or rel 1e-06  match
  Gap expansion factor (x)    -3.24     -3.24          0 abs 0.0051 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Phase 8.1: comparison with the independent pre-test: 3 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:29:46 | Phase 8.2 - regression-kink threshold (Supplementary Table J4)

Threshold (gamma) = 20% solar share; 90% interval [18%, 28%] from the day-clustered bootstrap (200 replications, seed 42); N = 35,064.
Slope below / above the threshold: 56.37 / 137.19 TL/MW per percentage point (delta = 80.82, bootstrap SE 19.69, t = 4.10).
sup-F = 984.0; day-clustered wild-bootstrap p = 0.000 (resolution 1/200).

- Phase_8/Phase_8_2_Hansen_Threshold.csv (537 bytes, sha256 9e05969dce65)

Checkpoints of this step:
[OK] K40 Phase 8.2: kink bootstrap replicates: estimated in this kernel: 200 of 200 (gamma, delta) replicates and 200 of 200 sup-F replicates finite (N_BOOT_THR = 200)
[OK] K40 Phase 8.2: interval contains the threshold estimate: gamma = 20% solar share, 90% day-clustered bootstrap interval [18%, 28%]
[OK] K45 Phase 8.2: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:29:46 | Phase 8.2 - regression kink vs. pre-test (sheet Kink_J4)

11 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                    Quantity    This run   Reference       Difference              Tolerance Status
Threshold_Point_Estimate_pct          20          20                0 abs 1e-09 or rel 1e-06  match
              CI90_Lower_pct          18          18                0    abs 0.5 or rel 0.05  match
              CI90_Upper_pct          28          28                0    abs 0.5 or rel 0.05  match
        Bootstrap_Median_pct          21          21                0    abs 0.5 or rel 0.05  match
            slope_pre_kink_b 56.37223318 56.37223318  7.496225862e-12 abs 1e-09 or rel 1e-06  match
                       delta 80.82210396 80.82210396  -8.49809112e-12 abs 1e-09 or rel 1e-06  match
slope_post_kink_b_plus_delta 137.1943371 137.1943371 -1.051603249e-12 abs 1e-09 or rel 1e-06  match
                    delta_se 19.69299216 19.69299216 -2.280842182e-12               rel 0.05  match
                     delta_t 4.104104816 4.104104816  4.440892099e-14               rel 0.05  match
                   supF_stat 983.9881159 983.9881159  1.136868377e-13 abs 1e-09 or rel 1e-06  match
         supF_pval_bootstrap           0           0                0    abs 0.5 or rel 0.05  match
```

Checkpoints of this step:
[OK] K17 Phase 8.2: comparison with the independent pre-test: 11 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:29:47 | Phase 9: methodological framework (figure)

Flow chart of the analysis (manuscript Figure 2), saved at 750 dpi and tagged 1000 dpi; no numbers.

- Phase_9/Figure_3_Methodological_Framework_Updated.png (2,147,551 bytes, sha256 6825841b9283)

Checkpoints of this step:
[OK] K45 Phase 9: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:49 | Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)

Table A1: solar generation share, mean 0.0688, maximum 0.5916 (share, 0-1).
Table C1 (common likelihood sample, first 28 observations left out), AIC: MCP (Day-Ahead) (1,1,1) 492,318.2 [Rejected; certified]; MCP (Day-Ahead) (2,0,2) 492,133.3 [Selected; certified]; a-FRR (Balancing) (1,1,1) 516,183.0 [Rejected; certified]; a-FRR (Balancing) (1,1,2) 516,118.1 [Selected; certified]; a-FRR (Balancing) (1,0,2) 516,102.6 [Robustness check (d = 0); certified].
Table C1, AIC of the baseline minus the selected order: MCP 184.9, a-FRR 64.9.
Solar coefficient, selected rows of Table C1 against Phase 4: MCP -5,780.8320 (Model 4: -5,780.8380; one observation fewer in the Table C1 likelihood), a-FRR 2,015.6981 (Model 1: 2,015.6980; same likelihood function, estimated from the Phase 4 solution).
Table D1 (standard errors clustered by calendar day): 27 of the 34 hypothesis variables of the eight models are significant at 5%.
Warnings stored with the 11 start records in Phase_10/starts: no warning for 11.

```
           Market                 Model   Order  Intercept         LogLik  Parameters           AIC           BIC    MA_root_moduli  Solar_Coefficient                   Status Convergence     Best_start  Starts_within_0.01
  MCP (Day-Ahead)              Baseline (1,1,1)      False -246135.083689          24 492318.167378 492521.306531          [1.0555]       -5835.069582                 Rejected   certified phase estimate                   2
  MCP (Day-Ahead)             Optimized (2,0,2)       True -246039.636618          27 492133.273235 492361.804782  [1.0819, 9.4524]       -5780.832010                 Selected   certified        default                   2
a-FRR (Balancing)              Baseline (1,1,1)      False -258067.509784          24 516183.019567 516386.158721          [1.0014]        2026.815323                 Rejected   certified phase estimate                   2
a-FRR (Balancing)             Optimized (1,1,2)      False -258034.074053          25 516118.148107 516329.751392 [1.0011, 19.5329]        2015.698129                 Selected   certified phase estimate                   1
a-FRR (Balancing) Alternative in levels (1,0,2)       True -258025.310356          26 516102.620712 516322.688128  [6.2615, 9.4319]        2009.160641 Robustness check (d = 0)   certified        default                   4
```

- Phase_10/Appendix_A_Descriptive_Statistics.csv (535 bytes, sha256 7b6edf39388a)
- Phase_10/Appendix_B_ADF_Unit_Root_Tests.csv (253 bytes, sha256 9145170cf454)
- Phase_10/Appendix_C_Model_Comparison.csv (2,620 bytes, sha256 279afa201dad)
- Phase_10/Appendix_D_Full_SARIMAX_Results.csv (897 bytes, sha256 3299eba65a21)
- Phase_10/Appendix_D_All_Hypothesis_Variables.csv (18,184 bytes, sha256 c1a56645ef73)
- Phase_10/Appendix_E_XGBoost_Params.csv (673 bytes, sha256 f4e31beaec4e)
- Phase_10/Appendix_F1_MCP_Correlation.png (789,115 bytes, sha256 8202c5a9c578)
- Phase_10/Appendix_F2_aFRR_Correlation.png (821,315 bytes, sha256 b015180107b4)
- Phase_10/Appendix_H_Down_Regulation_Volume.png (513,881 bytes, sha256 45671af18979)

Checkpoints of this step:
[OK] K10 Table C1: convergence: (i) MCP (Day-Ahead) (1,1,1): certified; (ii) MCP (Day-Ahead) (2,0,2): certified; (iii) a-FRR (Balancing) (1,1,1): certified; (iv) a-FRR (Balancing) (1,1,2): certified; (v) a-FRR (Balancing) (1,0,2): certified
[OK] K11 Table C1: reported representation invertible: (i) MCP (Day-Ahead) (1,1,1): invertible; (ii) MCP (Day-Ahead) (2,0,2): invertible; (iii) a-FRR (Balancing) (1,1,1): invertible; (iv) a-FRR (Balancing) (1,1,2): invertible; (v) a-FRR (Balancing) (1,0,2): invertible
[OK] K12 Table C1: agreement of the starts: (i) MCP (Day-Ahead) (1,1,1): 2 start(s) within 0.01; (ii) MCP (Day-Ahead) (2,0,2): 2 start(s) within 0.01; (iii) a-FRR (Balancing) (1,1,1): 2 start(s) within 0.01; (v) a-FRR (Balancing) (1,0,2): 4 start(s) within 0.01; (iv) a-FRR (Balancing) (1,1,2): one start only (by design: estimated from the Phase 4 solution, whose starts are compared in Phase 4)
[OK] K13 Table C1: intercept and regressors: (i) MCP (Day-Ahead) (1,1,1): const no (design: no), 19 exogenous terms (expected 19); (ii) MCP (Day-Ahead) (2,0,2): const yes (design: yes), 20 exogenous terms (expected 20); (iii) a-FRR (Balancing) (1,1,1): const no (design: no), 19 exogenous terms (expected 19); (iv) a-FRR (Balancing) (1,1,2): const no (design: no), 19 exogenous terms (expected 19); (v) a-FRR (Balancing) (1,0,2): const yes (design: yes), 20 exogenous terms (expected 20)
[OK] K14 Table C1: estimation sample: Table C1 is estimated without standard errors (inference=False), so it has no day clusters; checked instead that every row uses the whole sample: (i) MCP (Day-Ahead) (1,1,1): 35,064 observations incl. burn-in (sample 35,064 hours, 1,461 calendar days); (ii) MCP (Day-Ahead) (2,0,2): 35,064 observations incl. burn-in (sample 35,064 hours, 1,461 calendar days); (iii) a-FRR (Balancing) (1,1,1): 35,064 observations incl. burn-in (sample 35,064 hours, 1,461 calendar days); (iv) a-FRR (Balancing) (1,1,2): 35,064 observations incl. burn-in (sample 35,064 hours, 1,461 calendar days); (v) a-FRR (Balancing) (1,0,2): 35,064 observations incl. burn-in (sample 35,064 hours, 1,461 calendar days)
[OK] K16 Table D1: standard-error flags of the Phase 4 models: Table C1 has no standard errors; Table D1 reports the day-clustered standard errors of Phase 4 for 8 models: no standard-error flag
[OK] K45 Phase 10: output files: 9 of 9 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:49 | Table A1 (solar generation share) and the ADF statistics of Table B1

13 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                       Quantity        This run       Reference       Difference              Tolerance Status
                           A1 solar share, Mean   0.06878131054   0.06878131054 -2.775557562e-17 abs 1e-09 or rel 1e-09  match
                      A1 solar share, Std. Dev.   0.09787574897   0.09787574897 -2.775557562e-17 abs 1e-09 or rel 1e-09  match
                            A1 solar share, Min 3.407438495e-06 3.407438495e-06                0 abs 1e-09 or rel 1e-09  match
                            A1 solar share, Max    0.5916025611    0.5916025611                0 abs 1e-09 or rel 1e-09  match
                         A1 solar share, Median  0.005001830458  0.005001830458 -3.469446952e-18 abs 1e-09 or rel 1e-09  match
       ADF MCP (Day-Ahead Price), ADF Statistic         -9.4138         -9.4138                0 abs 1e-09 or rel 1e-06  match
             ADF MCP (Day-Ahead Price), P-Value               0               0                0 abs 1e-09 or rel 1e-06  match
         ADF a-FRR Price (Level), ADF Statistic        -17.2104        -17.2104                0 abs 1e-09 or rel 1e-06  match
               ADF a-FRR Price (Level), P-Value               0               0                0 abs 1e-09 or rel 1e-06  match
ADF a-FRR Price (1st Difference), ADF Statistic        -32.6812        -32.6812                0 abs 1e-09 or rel 1e-06  match
      ADF a-FRR Price (1st Difference), P-Value               0               0                0 abs 1e-09 or rel 1e-06  match
      ADF Solar Generation Share, ADF Statistic          -7.848          -7.848                0 abs 1e-09 or rel 1e-06  match
            ADF Solar Generation Share, P-Value               0               0                0 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Table A1 / B1 (ADF): comparison with the independent pre-test: 13 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:49 | Supplementary Table C1 (model selection on a common likelihood sample)

50 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                              Quantity     This run    Reference       Difference               Tolerance Status
                C1 (i) MCP (Day-Ahead) (1,1,1): LogLik -246135.0837 -246135.0837  4.598405212e-09                abs 0.02  match
            C1 (i) MCP (Day-Ahead) (1,1,1): Parameters           24           24                0               abs 1e-09  match
                   C1 (i) MCP (Day-Ahead) (1,1,1): AIC  492318.1674  492318.1674 -9.196810424e-09                abs 0.04  match
                   C1 (i) MCP (Day-Ahead) (1,1,1): BIC  492521.3065  492521.3065 -9.196810424e-09                abs 0.04  match
          C1 (i) MCP (Day-Ahead) (1,1,1): LjungBox_Q24  257.7373133  257.7374717 -0.0001583419251               rel 0.002  match
          C1 (i) MCP (Day-Ahead) (1,1,1): LjungBox_Q48  379.3872874   379.387395 -0.0001075891764               rel 0.002  match
     C1 (i) MCP (Day-Ahead) (1,1,1): Solar_Coefficient -5835.069582 -5835.069727  0.0001451697408 abs 1e-09 or rel 0.0002  match
                  C1 (i) MCP (Day-Ahead) (1,1,1): Burn           28           28                0               abs 1e-09  match
    C1 (i) MCP (Day-Ahead) (1,1,1): MA root modulus #1       1.0555       1.0555                0               abs 0.002  match
               C1 (ii) MCP (Day-Ahead) (2,0,2): LogLik -246039.6366 -246039.6366   7.62520358e-09                abs 0.02  match
           C1 (ii) MCP (Day-Ahead) (2,0,2): Parameters           27           27                0               abs 1e-09  match
                  C1 (ii) MCP (Day-Ahead) (2,0,2): AIC  492133.2732  492133.2732 -1.525040716e-08                abs 0.04  match
                  C1 (ii) MCP (Day-Ahead) (2,0,2): BIC  492361.8048  492361.8048 -1.530861482e-08                abs 0.04  match
         C1 (ii) MCP (Day-Ahead) (2,0,2): LjungBox_Q24  198.3532774  198.3533799 -0.0001024984267               rel 0.002  match
         C1 (ii) MCP (Day-Ahead) (2,0,2): LjungBox_Q48   296.173689  296.1734609  0.0002281381493               rel 0.002  match
    C1 (ii) MCP (Day-Ahead) (2,0,2): Solar_Coefficient  -5780.83201 -5780.832041  3.105852011e-05 abs 1e-09 or rel 0.0002  match
                 C1 (ii) MCP (Day-Ahead) (2,0,2): Burn           28           28                0               abs 1e-09  match
   C1 (ii) MCP (Day-Ahead) (2,0,2): MA root modulus #1       1.0819       1.0819                0               abs 0.002  match
   C1 (ii) MCP (Day-Ahead) (2,0,2): MA root modulus #2       9.4524       9.4524                0               abs 0.002  match
            C1 (iii) a-FRR (Balancing) (1,1,1): LogLik -258067.5098 -258067.5098   5.53263817e-08                 abs 0.1  match
        C1 (iii) a-FRR (Balancing) (1,1,1): Parameters           24           24                0               abs 1e-09  match
               C1 (iii) a-FRR (Balancing) (1,1,1): AIC  516183.0196  516183.0196 -1.107109711e-07                 abs 0.2  match
               C1 (iii) a-FRR (Balancing) (1,1,1): BIC  516386.1587  516386.1587 -1.107109711e-07                 abs 0.2  match
      C1 (iii) a-FRR (Balancing) (1,1,1): LjungBox_Q24  1333.463426  1333.456344   0.007081171525                rel 0.01  match
      C1 (iii) a-FRR (Balancing) (1,1,1): LjungBox_Q48  1449.712916  1449.707301   0.005615957888                rel 0.01  match
 C1 (iii) a-FRR (Balancing) (1,1,1): Solar_Coefficient  2026.815323  2026.815263   6.02833336e-05  abs 1e-09 or rel 0.005  match
              C1 (iii) a-FRR (Balancing) (1,1,1): Burn           28           28                0               abs 1e-09  match
C1 (iii) a-FRR (Balancing) (1,1,1): MA root modulus #1       1.0014       1.0014                0               abs 0.005  match
             C1 (iv) a-FRR (Balancing) (1,1,2): LogLik -258034.0741 -258034.0741  6.530899554e-07                 abs 0.1  match
         C1 (iv) a-FRR (Balancing) (1,1,2): Parameters           25           25                0               abs 1e-09  match
                C1 (iv) a-FRR (Balancing) (1,1,2): AIC  516118.1481  516118.1481 -1.306063496e-06                 abs 0.2  match
                C1 (iv) a-FRR (Balancing) (1,1,2): BIC  516329.7514  516329.7514 -1.306121703e-06                 abs 0.2  match
       C1 (iv) a-FRR (Balancing) (1,1,2): LjungBox_Q24  1238.001886  1238.002986  -0.001100212038                rel 0.01  match
       C1 (iv) a-FRR (Balancing) (1,1,2): LjungBox_Q48  1354.687199  1354.689552  -0.002353080896                rel 0.01  match
  C1 (iv) a-FRR (Balancing) (1,1,2): Solar_Coefficient  2015.698129  2015.705747  -0.007617674994  abs 1e-09 or rel 0.005  match
               C1 (iv) a-FRR (Balancing) (1,1,2): Burn           28           28                0               abs 1e-09  match
 C1 (iv) a-FRR (Balancing) (1,1,2): MA root modulus #1       1.0011       1.0011                0               abs 0.005  match
 C1 (iv) a-FRR (Balancing) (1,1,2): MA root modulus #2      19.5329      19.5329                0               abs 0.005  match
              C1 (v) a-FRR (Balancing) (1,0,2): LogLik -258025.3104 -258025.3104  1.688022166e-09                 abs 0.1  match
          C1 (v) a-FRR (Balancing) (1,0,2): Parameters           26           26                0               abs 1e-09  match
                 C1 (v) a-FRR (Balancing) (1,0,2): AIC  516102.6207  516102.6207 -3.376044333e-09                 abs 0.2  match
                 C1 (v) a-FRR (Balancing) (1,0,2): BIC  516322.6881  516322.6881 -3.434251994e-09                 abs 0.2  match
        C1 (v) a-FRR (Balancing) (1,0,2): LjungBox_Q24  1237.374433  1237.374323  0.0001099595147                rel 0.01  match
        C1 (v) a-FRR (Balancing) (1,0,2): LjungBox_Q48  1355.781074  1355.780978  9.574624801e-05                rel 0.01  match
   C1 (v) a-FRR (Balancing) (1,0,2): Solar_Coefficient  2009.160641   2009.16343  -0.002788862765  abs 1e-09 or rel 0.005  match
                C1 (v) a-FRR (Balancing) (1,0,2): Burn           28           28                0               abs 1e-09  match
  C1 (v) a-FRR (Balancing) (1,0,2): MA root modulus #1       6.2615       6.2615                0               abs 0.005  match
  C1 (v) a-FRR (Balancing) (1,0,2): MA root modulus #2       9.4319       9.4319                0               abs 0.005  match
                   C1 AIC, MCP baseline minus selected   184.894143   184.894143  6.053596735e-09                abs 0.04  match
                 C1 AIC, a-FRR baseline minus selected  64.87146049   64.8714593  1.195352525e-06                 abs 0.2  match
```

Checkpoints of this step:
[OK] K17 Table C1: comparison with the independent pre-test: 50 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:49 | Supplementary Table D1: hypothesis variables of the eight models (coefficient; standard error clustered by calendar day)

68 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                                Quantity     This run    Reference       Difference               Tolerance Status
             Model 1 Solar_Generation_Share: coefficient  2015.698036  2015.705747  -0.007710878733  abs 1e-09 or rel 0.005  match
      Model 1 Solar_Generation_Share: SE (day-clustered)  446.1543157  446.1555825  -0.001266871414                rel 0.03  match
           Model 1 Interaction_Solar_Sunday: coefficient   3881.34015  3881.352731   -0.01258053131  abs 1e-09 or rel 0.005  match
    Model 1 Interaction_Solar_Sunday: SE (day-clustered)  372.5818633  372.5874546  -0.005591229061                rel 0.03  match
          Model 1 Interaction_Solar_Holiday: coefficient  746.0282662  746.0381124  -0.009846175096  abs 1e-09 or rel 0.005  match
   Model 1 Interaction_Solar_Holiday: SE (day-clustered)  588.8522572  588.8592461  -0.006988885689                rel 0.03  match
               Model 2 Solar_Share_x_Hour_8: coefficient  3686.865314  3686.872342  -0.007027746484  abs 1e-09 or rel 0.005  match
        Model 2 Solar_Share_x_Hour_8: SE (day-clustered)  787.3497044  787.3015768    0.04812752635                rel 0.03  match
               Model 2 Solar_Share_x_Hour_9: coefficient  2178.917943  2178.922122  -0.004178593429  abs 1e-09 or rel 0.005  match
        Model 2 Solar_Share_x_Hour_9: SE (day-clustered)  528.3235246  528.3125222    0.01100239387                rel 0.03  match
              Model 2 Solar_Share_x_Hour_10: coefficient  1623.012063  1623.016256  -0.004192954652  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_10: SE (day-clustered)  493.3338953  493.3312174   0.002677861167                rel 0.03  match
              Model 2 Solar_Share_x_Hour_11: coefficient  3934.353917  3934.353702  0.0002145774683  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_11: SE (day-clustered)  559.6058645  559.6017671   0.004097431064                rel 0.03  match
              Model 2 Solar_Share_x_Hour_12: coefficient  3733.593399  3733.592351    0.00104809172  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_12: SE (day-clustered)  580.3447658  580.3422693   0.002496565022                rel 0.03  match
              Model 2 Solar_Share_x_Hour_13: coefficient  3910.267122  3910.266382   0.000740624901  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_13: SE (day-clustered)  585.7558699  585.7534467   0.002423215824                rel 0.03  match
              Model 2 Solar_Share_x_Hour_14: coefficient  4732.710344  4732.709388  0.0009565734281  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_14: SE (day-clustered)  625.0202508  625.0168103   0.003440444535                rel 0.03  match
              Model 2 Solar_Share_x_Hour_15: coefficient  4391.015864  4391.015071  0.0007937557712  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_15: SE (day-clustered)  598.2398136  598.2397205  9.310486166e-05                rel 0.03  match
              Model 2 Solar_Share_x_Hour_16: coefficient  1165.331689   1165.33385  -0.002160899578  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_16: SE (day-clustered)  763.2368289  763.2406577  -0.003828790314                rel 0.03  match
              Model 2 Solar_Share_x_Hour_17: coefficient  5531.859221  5531.861499  -0.002277693382  abs 1e-09 or rel 0.005  match
       Model 2 Solar_Share_x_Hour_17: SE (day-clustered)  1160.550786  1160.551424  -0.000638006178                rel 0.03  match
             Model 3 Interaction_Solar_Peak: coefficient  1548.243698  1548.242355    0.00134261894  abs 1e-09 or rel 0.005  match
      Model 3 Interaction_Solar_Peak: SE (day-clustered)  294.7273921  294.7265981  0.0007939433136                rel 0.03  match
             Model 4 Solar_Generation_Share: coefficient -5780.837983 -5780.836239     -0.001744557 abs 1e-09 or rel 0.0002  match
      Model 4 Solar_Generation_Share: SE (day-clustered)  207.6989414  207.6989447 -3.247207218e-06                rel 0.01  match
           Model 4 Interaction_Solar_Sunday: coefficient -176.3133877 -176.3141335  0.0007458295856 abs 1e-09 or rel 0.0002  match
    Model 4 Interaction_Solar_Sunday: SE (day-clustered)  130.8956948  130.8956951 -3.449749499e-07                rel 0.01  match
          Model 4 Interaction_Solar_Holiday: coefficient   270.891011  270.8900305  0.0009805025351 abs 1e-09 or rel 0.0002  match
   Model 4 Interaction_Solar_Holiday: SE (day-clustered)  175.4970202  175.4970119  8.304721263e-06                rel 0.01  match
               Model 5 Solar_Share_x_Hour_8: coefficient -6133.939375 -6133.971559    0.03218329342 abs 1e-09 or rel 0.0002  match
        Model 5 Solar_Share_x_Hour_8: SE (day-clustered)  365.4564969  365.4568095 -0.0003126453423                rel 0.01  match
               Model 5 Solar_Share_x_Hour_9: coefficient -5664.936843 -5664.949019    0.01217532312 abs 1e-09 or rel 0.0002  match
        Model 5 Solar_Share_x_Hour_9: SE (day-clustered)  285.3084647  285.3085688 -0.0001041591021                rel 0.01  match
              Model 5 Solar_Share_x_Hour_10: coefficient -5303.235272 -5303.244288   0.009015456786 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_10: SE (day-clustered)  246.3766863   246.376826 -0.0001397583176                rel 0.01  match
              Model 5 Solar_Share_x_Hour_11: coefficient -5343.636488 -5343.646328   0.009840413094 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_11: SE (day-clustered)  229.9234349  229.9236445 -0.0002096592386                rel 0.01  match
              Model 5 Solar_Share_x_Hour_12: coefficient -4166.101733  -4166.08998   -0.01175343679 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_12: SE (day-clustered)  245.7452478  245.7482885  -0.003040716009                rel 0.01  match
              Model 5 Solar_Share_x_Hour_13: coefficient -4458.831958 -4458.841887   0.009928659519 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_13: SE (day-clustered)  236.8349992  236.8369636  -0.001964465314                rel 0.01  match
              Model 5 Solar_Share_x_Hour_14: coefficient  -5102.14076 -5102.146693     0.0059324229 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_14: SE (day-clustered)  238.5480528  238.5485124 -0.0004596427019                rel 0.01  match
              Model 5 Solar_Share_x_Hour_15: coefficient -5859.380028 -5859.379686 -0.0003417098778 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_15: SE (day-clustered)  271.3793892  271.3797322 -0.0003430236718                rel 0.01  match
              Model 5 Solar_Share_x_Hour_16: coefficient -5513.908052 -5513.905917   -0.00213434457 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_16: SE (day-clustered)  330.2792804  330.2796509 -0.0003704836595                rel 0.01  match
              Model 5 Solar_Share_x_Hour_17: coefficient -4532.468572 -4532.471108   0.002536413111 abs 1e-09 or rel 0.0002  match
       Model 5 Solar_Share_x_Hour_17: SE (day-clustered)  432.6077814   432.608789   -0.00100759493                rel 0.01  match
             Model 6 Interaction_Solar_Peak: coefficient -2209.698315 -2209.701314   0.002999353034 abs 1e-09 or rel 0.0002  match
      Model 6 Interaction_Solar_Peak: SE (day-clustered)  177.8725408  177.8724657  7.507439406e-05                rel 0.01  match
            Model 7.2 System_Direction_Down: coefficient -17.03566242 -17.03570783  4.540851883e-05  abs 1e-09 or rel 0.005  match
     Model 7.2 System_Direction_Down: SE (day-clustered)  6.506018822  6.505990696  2.812623401e-05                rel 0.03  match
           Model 7.3 Solar_Generation_Share: coefficient  4474.231913  4474.210284    0.02162945549  abs 1e-09 or rel 0.005  match
    Model 7.3 Solar_Generation_Share: SE (day-clustered)  458.1058626  458.1214785   -0.01561589798                rel 0.03  match
            Model 7.3 System_Direction_Down: coefficient -15.24561925 -15.24869576   0.003076508299  abs 1e-09 or rel 0.005  match
     Model 7.3 System_Direction_Down: SE (day-clustered)  7.991125134  7.991121126  4.007284041e-06                rel 0.03  match
              Model 7.3 System_Direction_Up: coefficient -16.04452213 -16.04514267   0.000620537932  abs 1e-09 or rel 0.005  match
       Model 7.3 System_Direction_Up: SE (day-clustered)  6.220272934  6.220254214  1.872049511e-05                rel 0.03  match
       Model 7.3 Interaction_Solar_Dir_Down: coefficient -46.71301297   -46.728814    0.01580102573  abs 1e-09 or rel 0.005  match
Model 7.3 Interaction_Solar_Dir_Down: SE (day-clustered)  80.82949162    80.831352  -0.001860378185                rel 0.03  match
         Model 7.3 Interaction_Solar_Dir_Up: coefficient  137.6934077  137.7004407  -0.007032995759  abs 1e-09 or rel 0.005  match
  Model 7.3 Interaction_Solar_Dir_Up: SE (day-clustered)   71.4124474  71.41342242 -0.0009750169265                rel 0.03  match
```

Checkpoints of this step:
[OK] K17 Table D1: comparison with the independent pre-test: 68 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:54 | Appendix B - ADF and KPSS stationarity tests (Supplementary Table B1)

MCP (Day-Ahead Price): Long memory / persistence (tests diverge)
a-FRR Price (Level): Long memory / persistence (tests diverge)
a-FRR Price (1st Difference): I(0) - Stationary (both)
Solar Generation Share: Long memory / persistence (tests diverge)
KPSS p-values are interpolated in the statsmodels table, which covers 0.01-0.10: 0.01 means p < 0.01 and 0.10 means p > 0.10. ADF p-values are rounded to four decimals (0.0 = below 0.00005).

```
                    Variable  ADF Statistic  ADF P-Value  KPSS Statistic  KPSS P-Value  KPSS 5% Crit.
       MCP (Day-Ahead Price)        -9.4138          0.0          2.1447          0.01          0.463
         a-FRR Price (Level)       -17.2104          0.0          0.7479          0.01          0.463
a-FRR Price (1st Difference)       -32.6812          0.0          0.0045          0.10          0.463
      Solar Generation Share        -7.8480          0.0         19.5317          0.01          0.463
```

- Phase_10/Appendix_B_Stationarity_Tests.csv (454 bytes, sha256 8cd18825eca0)

Checkpoints of this step:
[WARNING] K43 Appendix B: KPSS p-values at the table bounds: 4 of 4 KPSS p-values are bounds of the table, reported as bounds: MCP (Day-Ahead Price): p < 0.01 (statistic 2.1447); a-FRR Price (Level): p < 0.01 (statistic 0.7479); a-FRR Price (1st Difference): p > 0.10 (statistic 0.0045); Solar Generation Share: p < 0.01 (statistic 19.5317)
[OK] K45 Appendix B: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:54 | Table B1 vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)

20 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                    Quantity This run Reference Difference              Tolerance Status
        MCP (Day-Ahead Price): ADF Statistic  -9.4138   -9.4138          0 abs 1e-09 or rel 1e-06  match
          MCP (Day-Ahead Price): ADF P-Value        0         0          0 abs 1e-09 or rel 1e-06  match
       MCP (Day-Ahead Price): KPSS Statistic   2.1447    2.1447          0 abs 1e-09 or rel 1e-06  match
         MCP (Day-Ahead Price): KPSS P-Value     0.01      0.01          0 abs 1e-09 or rel 1e-06  match
        MCP (Day-Ahead Price): KPSS 5% Crit.    0.463     0.463          0 abs 1e-09 or rel 1e-06  match
          a-FRR Price (Level): ADF Statistic -17.2104  -17.2104          0 abs 1e-09 or rel 1e-06  match
            a-FRR Price (Level): ADF P-Value        0         0          0 abs 1e-09 or rel 1e-06  match
         a-FRR Price (Level): KPSS Statistic   0.7479    0.7479          0 abs 1e-09 or rel 1e-06  match
           a-FRR Price (Level): KPSS P-Value     0.01      0.01          0 abs 1e-09 or rel 1e-06  match
          a-FRR Price (Level): KPSS 5% Crit.    0.463     0.463          0 abs 1e-09 or rel 1e-06  match
 a-FRR Price (1st Difference): ADF Statistic -32.6812  -32.6812          0 abs 1e-09 or rel 1e-06  match
   a-FRR Price (1st Difference): ADF P-Value        0         0          0 abs 1e-09 or rel 1e-06  match
a-FRR Price (1st Difference): KPSS Statistic   0.0045    0.0045          0 abs 1e-09 or rel 1e-06  match
  a-FRR Price (1st Difference): KPSS P-Value      0.1       0.1          0 abs 1e-09 or rel 1e-06  match
 a-FRR Price (1st Difference): KPSS 5% Crit.    0.463     0.463          0 abs 1e-09 or rel 1e-06  match
       Solar Generation Share: ADF Statistic   -7.848    -7.848          0 abs 1e-09 or rel 1e-06  match
         Solar Generation Share: ADF P-Value        0         0          0 abs 1e-09 or rel 1e-06  match
      Solar Generation Share: KPSS Statistic  19.5317   19.5317          0 abs 1e-09 or rel 1e-06  match
        Solar Generation Share: KPSS P-Value     0.01      0.01          0 abs 1e-09 or rel 1e-06  match
       Solar Generation Share: KPSS 5% Crit.    0.463     0.463          0 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Appendix B: comparison with the independent pre-test: 20 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:56 | Appendix I: flexibility trap and GAM flexibility-stress with the Botas tariff as a control

Figure I.1 crossover (the surplus curve stays above the deficit/balanced curve from there to 45%): none. The surplus curve rises above the deficit/balanced curve at 2.16, 23.96, 35.70% solar share and falls below it at 1.16, 4.06, 29.00, 36.44% solar share; at the end of the 0-45% range it is below it (above over 20.0% of the range).
The pre-test value 35.70% coincides with the last upward crossing; the surplus curve falls below the deficit/balanced curve again at 36.44%, so the comparison row below shows DIFFERS.
Figure I.2 GAM R2: deficit/balanced 0.4053, surplus 0.5928.
xgboost 3.2.0 (version of the fit). Tree ensembles depend on library version and platform: agreement with the pre-test is expected in the reference environment only.

- Phase_10/Appendix_I_Figure_I1_Flexibility_Trap_Botas.png (1,353,784 bytes, sha256 89d53ee0aab9)
- Phase_10/Appendix_I_Flexibility_Trap_Crossover.csv (377 bytes, sha256 dc5ace02f7b4)
- Phase_10/Appendix_I_Figure_I2_GAM_Flexibility_Stress_Botas.png (1,158,707 bytes, sha256 9b5e8aede4a5)
- Phase_10/Appendix_I_Botas_Report.txt (112 bytes, sha256 9955602adb4a)

Checkpoints of this step:
[WARNING] K42 Appendix I: flexibility-trap crossover: crossover = the last upward crossing of the surplus curve over the deficit/balanced curve after which it stays above up to the end of the common range (0-45%): none (no sustained crossover); upward crossings: 2.16, 23.96, 35.70% solar share; downward crossings: 1.16, 4.06, 29.00, 36.44% solar share
[OK] K45 Appendix I: output files: 4 of 4 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:56 | Appendix I: crossover (Figure I.1) and GAM fit (Figure I.2)

2 match, 1 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                           Quantity This run   Reference Difference                Tolerance  Status
Figure I.1 crossover, % solar share      nan 35.70039733        nan   abs 1e-09 or rel 1e-06 DIFFERS
           GAM R2, deficit/balanced   0.4053      0.4053          0 abs 5.1e-05 or rel 1e-06   match
                    GAM R2, surplus   0.5928      0.5928          0 abs 5.1e-05 or rel 1e-06   match
```

Checkpoints of this step:
[WARNING] K17 Appendix I: comparison with the independent pre-test: 2 match, 1 DIFFERS, 0 reported without tolerance, 0 without reference; DIFFERS explained by the pre-test value being the last upward crossing, after which the surplus curve falls below again (section above): Figure I.1 crossover, % solar share

Warnings raised in this step: none.

## 2026-11-21 04:47:57 | Phase 11.1 - inflation robustness, ratio and cap-normalised FE-OLS (Supplementary Appendix J.6)

Hour, month and year fixed effects; standard errors clustered by calendar day (day_key of the time index).
Day clusters: MCP (level) = 1,461, a-FRR (level) = 1,461, a-FRR / MCP ratio = 1,461, MCP / Price Cap = 1,461, a-FRR / Price Cap = 1,461.

```
Dependent Variable  Solar Coef (per unit share)  Effect per +1pp  Std. Error  P-Value  R-squared     N  Clusters (days)
       MCP (level)                   -6884.8726         -68.8487    142.8372      0.0      0.801 35064             1461
     a-FRR (level)                   10955.5788         109.5558    447.2910      0.0      0.585 35064             1461
 a-FRR / MCP ratio                      38.4936           0.3849      3.3309      0.0      0.309 34995             1461
   MCP / Price Cap                      -1.9264          -0.0193      0.0412      0.0      0.703 35064             1461
 a-FRR / Price Cap                       3.4687           0.0347      0.1401      0.0      0.568 35064             1461
```

- Phase_11_Inflation/Inflation_Robustness_Results.csv (416 bytes, sha256 35ee35fd1f5b)

Checkpoints of this step:
[OK] K44 Appendix J.6: day clusters: MCP (level): 1,461 clusters for 1,461 calendar days, N = 35,064 of 35,064 hours; a-FRR (level): 1,461 clusters for 1,461 calendar days, N = 35,064 of 35,064 hours; a-FRR / MCP ratio: 1,461 clusters for 1,461 calendar days, N = 34,995 of 34,995 hours; MCP / Price Cap: 1,461 clusters for 1,461 calendar days, N = 35,064 of 35,064 hours; a-FRR / Price Cap: 1,461 clusters for 1,461 calendar days, N = 35,064 of 35,064 hours
[OK] K45 Appendix J.6: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:57 | Appendix J.6 vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)

30 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                      Quantity   This run  Reference Difference              Tolerance Status
      MCP (level): Solar Coef (per unit share) -6884.8726 -6884.8726          0 abs 1e-09 or rel 1e-06  match
                  MCP (level): Effect per +1pp   -68.8487   -68.8487          0 abs 1e-09 or rel 1e-06  match
                       MCP (level): Std. Error   142.8372   142.8372          0 abs 1e-09 or rel 1e-06  match
                          MCP (level): P-Value          0          0          0 abs 1e-09 or rel 1e-06  match
                        MCP (level): R-squared      0.801      0.801          0 abs 1e-09 or rel 1e-06  match
                                MCP (level): N      35064      35064          0 abs 1e-09 or rel 1e-09  match
    a-FRR (level): Solar Coef (per unit share) 10955.5788 10955.5788          0 abs 1e-09 or rel 1e-06  match
                a-FRR (level): Effect per +1pp   109.5558   109.5558          0 abs 1e-09 or rel 1e-06  match
                     a-FRR (level): Std. Error    447.291    447.291          0 abs 1e-09 or rel 1e-06  match
                        a-FRR (level): P-Value          0          0          0 abs 1e-09 or rel 1e-06  match
                      a-FRR (level): R-squared      0.585      0.585          0 abs 1e-09 or rel 1e-06  match
                              a-FRR (level): N      35064      35064          0 abs 1e-09 or rel 1e-09  match
a-FRR / MCP ratio: Solar Coef (per unit share)    38.4936    38.4936          0 abs 1e-09 or rel 1e-06  match
            a-FRR / MCP ratio: Effect per +1pp     0.3849     0.3849          0 abs 1e-09 or rel 1e-06  match
                 a-FRR / MCP ratio: Std. Error     3.3309     3.3309          0 abs 1e-09 or rel 1e-06  match
                    a-FRR / MCP ratio: P-Value          0          0          0 abs 1e-09 or rel 1e-06  match
                  a-FRR / MCP ratio: R-squared      0.309      0.309          0 abs 1e-09 or rel 1e-06  match
                          a-FRR / MCP ratio: N      34995      34995          0 abs 1e-09 or rel 1e-09  match
  MCP / Price Cap: Solar Coef (per unit share)    -1.9264    -1.9264          0 abs 1e-09 or rel 1e-06  match
              MCP / Price Cap: Effect per +1pp    -0.0193    -0.0193          0 abs 1e-09 or rel 1e-06  match
                   MCP / Price Cap: Std. Error     0.0412     0.0412          0 abs 1e-09 or rel 1e-06  match
                      MCP / Price Cap: P-Value          0          0          0 abs 1e-09 or rel 1e-06  match
                    MCP / Price Cap: R-squared      0.703      0.703          0 abs 1e-09 or rel 1e-06  match
                            MCP / Price Cap: N      35064      35064          0 abs 1e-09 or rel 1e-09  match
a-FRR / Price Cap: Solar Coef (per unit share)     3.4687     3.4687          0 abs 1e-09 or rel 1e-06  match
            a-FRR / Price Cap: Effect per +1pp     0.0347     0.0347          0 abs 1e-09 or rel 1e-06  match
                 a-FRR / Price Cap: Std. Error     0.1401     0.1401          0 abs 1e-09 or rel 1e-06  match
                    a-FRR / Price Cap: P-Value          0          0          0 abs 1e-09 or rel 1e-06  match
                  a-FRR / Price Cap: R-squared      0.568      0.568          0 abs 1e-09 or rel 1e-06  match
                          a-FRR / Price Cap: N      35064      35064          0 abs 1e-09 or rel 1e-09  match
```

Checkpoints of this step:
[OK] K17 Appendix J.6: comparison with the independent pre-test: 30 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Supplementary: in-sample fit of the XGBoost models (Phase 6.1 and Phase 6.2)

In-sample R2 (accuracy for the system-direction classifier) of the five XGBoost models, rounded as stored in the file.
xgboost 3.2.0 in this kernel (a cached file keeps the values of the session that fitted the models). Tree ensembles depend on library version and platform: agreement with the pre-test is expected in the reference environment only.

```
                       Metric  Value
           MCP Model R2 Score  0.933
  a-FRR (Volatility) R2 Score  0.907
System Direction Accuracy (%) 86.000
      Deficit Regime Model R2  0.899
      Surplus Regime Model R2  0.970
```

- Supplementary_Metrics/XGBoost_Performance_Metrics.csv (166 bytes, sha256 db898d1e4b86)

Checkpoints of this step:
[OK] K41 Supplementary metrics: XGBoost in-sample fit: 5 of 5 metrics finite
[OK] K45 Supplementary XGBoost metrics: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | XGBoost performance metrics (in-sample)

5 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                     Quantity This run Reference Difference              Tolerance Status
           MCP Model R2 Score    0.933     0.933          0 abs 1e-09 or rel 1e-06  match
  a-FRR (Volatility) R2 Score    0.907     0.907          0 abs 1e-09 or rel 1e-06  match
System Direction Accuracy (%)       86        86          0 abs 1e-09 or rel 1e-06  match
      Deficit Regime Model R2    0.899     0.899          0 abs 1e-09 or rel 1e-06  match
      Surplus Regime Model R2     0.97      0.97          0 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Supplementary XGBoost metrics: comparison with the independent pre-test: 5 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Supplementary metrics - GAM fit by regime (R-squared)

Energy DEFICIT (Up-Regulation): R-squared = 0.3599, N = 25,902
Energy SURPLUS (Down-Regulation): R-squared = 0.5765, N = 9,162

- Supplementary_Metrics/GAM_Performance_Metrics.csv (107 bytes, sha256 bd1d777eece8)

Checkpoints of this step:
[OK] K45 Supplementary GAM metrics: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | GAM fit metrics vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)

4 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                   Quantity This run Reference Difference              Tolerance Status
  Energy DEFICIT (Up-Regulation): R-squared   0.3599    0.3599          0 abs 1e-09 or rel 1e-06  match
          Energy DEFICIT (Up-Regulation): N    25902     25902          0 abs 1e-09 or rel 1e-09  match
Energy SURPLUS (Down-Regulation): R-squared   0.5765    0.5765          0 abs 1e-09 or rel 1e-06  match
        Energy SURPLUS (Down-Regulation): N     9162      9162          0 abs 1e-09 or rel 1e-09  match
```

Checkpoints of this step:
[OK] K17 Supplementary GAM metrics: comparison with the independent pre-test: 4 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Phase 11.2 - timing, decision-time information and confounding (Supplementary Table J1)

Correlation between the real-time (ex-ante) and the settlement (ex-post) solar share, all hours: r = 0.9976.
Correlation between solar share and consumption, all hours: r = 0.2922; largest VIF = 3.70 (Consumption).

```
                                        Specification                 Regressor         Beta     t_stat     N
                            MCP - realised, same hour    Solar_Generation_Share -5149.820212 -42.859591 35064
                     MCP - solar lagged one day (D-1)               solar_lag24 -4020.721173 -31.026676 35040
                          a-FRR - realised, same hour    Solar_Generation_Share  8888.802241  26.033855 35064
                  a-FRR - solar lagged two days (D-2)               solar_lag48  6620.557940  20.628626 35016
  MCP - real-time solar (D-1) + real-time consumption            rt_solar_lag24 -3830.625236 -30.245730 35040
     MCP - fully ex-ante (real-time consumption, D-1)            rt_solar_lag24 -2958.701208 -23.541375 35040
a-FRR - real-time solar (D-2) + real-time consumption            rt_solar_lag48  6524.450735  20.809658 35016
   a-FRR - fully ex-ante (real-time consumption, D-2)            rt_solar_lag48  5032.470911  17.051472 35016
                    a-FRR ~ RT solar + RT consumption RT_Solar_Generation_Share  8492.470223  25.523850 35064
                    a-FRR ~ RT solar + RT consumption            RT_Consumption    -0.109596 -19.263245 35064
                          a-FRR ~ solar + consumption    Solar_Generation_Share  8888.802241  26.033855 35064
                          a-FRR ~ solar + consumption               Consumption    -0.110562 -18.781649 35064
                                     a-FRR ~ net load                  Net_Load    -0.139250 -22.466247 35064
                        a-FRR ~ net-load ramp + solar             Net_Load_Ramp     0.091625  16.020986 35063
```

- Phase_11_Robustness/Phase_11_2_Timing_Robustness.csv (2,148 bytes, sha256 ad33853afaa7)
- Phase_11_Robustness/Phase_11_2_Confounding_Diagnostics.csv (1,010 bytes, sha256 da075b09a69d)

Checkpoints of this step:
[OK] K45 Phase 11.2: output files: 2 of 2 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Table J1 vs. pre-test (sheet J1_J2)

42 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                                                       Quantity         This run        Reference        Difference              Tolerance Status
                       MCP - realised, same hour | Solar_Generation_Share: Beta     -5149.820212     -5149.820212   5.406764103e-08 abs 1e-09 or rel 1e-06  match
                     MCP - realised, same hour | Solar_Generation_Share: t_stat     -42.85959144     -42.85959145   2.592123849e-09 abs 1e-09 or rel 1e-06  match
                    MCP - realised, same hour | Solar_Generation_Share: p_value                0                0                 0 abs 1e-09 or rel 1e-06  match
                           MCP - solar lagged one day (D-1) | solar_lag24: Beta     -4020.721173     -4020.721173   1.136868377e-09 abs 1e-09 or rel 1e-06  match
                         MCP - solar lagged one day (D-1) | solar_lag24: t_stat     -31.02667586     -31.02667586   -9.02034003e-11 abs 1e-09 or rel 1e-06  match
                        MCP - solar lagged one day (D-1) | solar_lag24: p_value 2.354839017e-211 2.354839024e-211 -6.597554019e-220 abs 1e-09 or rel 1e-06  match
                     a-FRR - realised, same hour | Solar_Generation_Share: Beta      8888.802241      8888.802241   -9.33323463e-08 abs 1e-09 or rel 1e-06  match
                   a-FRR - realised, same hour | Solar_Generation_Share: t_stat      26.03385478      26.03385478   2.593058213e-09 abs 1e-09 or rel 1e-06  match
                  a-FRR - realised, same hour | Solar_Generation_Share: p_value 2.049759051e-149 2.049759189e-149 -1.385773876e-156 abs 1e-09 or rel 1e-06  match
                        a-FRR - solar lagged two days (D-2) | solar_lag48: Beta       6620.55794      6620.557939   3.709828889e-08 abs 1e-09 or rel 1e-06  match
                      a-FRR - solar lagged two days (D-2) | solar_lag48: t_stat      20.62862617      20.62862617   1.069182076e-09 abs 1e-09 or rel 1e-06  match
                     a-FRR - solar lagged two days (D-2) | solar_lag48: p_value  1.519046112e-94  1.519046145e-94 -3.358186422e-102 abs 1e-09 or rel 1e-06  match
     MCP - real-time solar (D-1) + real-time consumption | rt_solar_lag24: Beta     -3830.625236     -3830.625236  -2.253091225e-08 abs 1e-09 or rel 1e-06  match
   MCP - real-time solar (D-1) + real-time consumption | rt_solar_lag24: t_stat     -30.24573027     -30.24573027   3.409788008e-10 abs 1e-09 or rel 1e-06  match
  MCP - real-time solar (D-1) + real-time consumption | rt_solar_lag24: p_value 5.937376144e-201 5.937376083e-201  6.130090584e-209 abs 1e-09 or rel 1e-06  match
        MCP - fully ex-ante (real-time consumption, D-1) | rt_solar_lag24: Beta     -2958.701208     -2958.701208   1.187208909e-08 abs 1e-09 or rel 1e-06  match
      MCP - fully ex-ante (real-time consumption, D-1) | rt_solar_lag24: t_stat     -23.54137527     -23.54137527   1.650946047e-11 abs 1e-09 or rel 1e-06  match
     MCP - fully ex-ante (real-time consumption, D-1) | rt_solar_lag24: p_value 1.538579224e-122 1.538579223e-122  5.990252198e-132 abs 1e-09 or rel 1e-06  match
   a-FRR - real-time solar (D-2) + real-time consumption | rt_solar_lag48: Beta      6524.450735      6524.450735  -1.267380867e-08 abs 1e-09 or rel 1e-06  match
 a-FRR - real-time solar (D-2) + real-time consumption | rt_solar_lag48: t_stat      20.80965751      20.80965751   1.032827157e-09 abs 1e-09 or rel 1e-06  match
a-FRR - real-time solar (D-2) + real-time consumption | rt_solar_lag48: p_value  3.538636597e-96  3.538636673e-96  -7.62298708e-104 abs 1e-09 or rel 1e-06  match
      a-FRR - fully ex-ante (real-time consumption, D-2) | rt_solar_lag48: Beta      5032.470911      5032.470911   -8.96579877e-09 abs 1e-09 or rel 1e-06  match
    a-FRR - fully ex-ante (real-time consumption, D-2) | rt_solar_lag48: t_stat      17.05147154      17.05147153   1.124337956e-09 abs 1e-09 or rel 1e-06  match
   a-FRR - fully ex-ante (real-time consumption, D-2) | rt_solar_lag48: p_value  3.408431282e-65  3.408431348e-65  -6.556833403e-73 abs 1e-09 or rel 1e-06  match
            a-FRR ~ RT solar + RT consumption | RT_Solar_Generation_Share: Beta      8492.470223      8492.470223   1.296775736e-07 abs 1e-09 or rel 1e-06  match
          a-FRR ~ RT solar + RT consumption | RT_Solar_Generation_Share: t_stat      25.52384983      25.52384983   7.668674584e-10 abs 1e-09 or rel 1e-06  match
         a-FRR ~ RT solar + RT consumption | RT_Solar_Generation_Share: p_value 1.071735583e-143 1.071735604e-143 -2.100955747e-151 abs 1e-09 or rel 1e-06  match
                       a-FRR ~ RT solar + RT consumption | RT_Consumption: Beta    -0.1095957684    -0.1095957684  -4.234501638e-12 abs 1e-09 or rel 1e-06  match
                     a-FRR ~ RT solar + RT consumption | RT_Consumption: t_stat     -19.26324526     -19.26324526  -3.711875252e-11 abs 1e-09 or rel 1e-06  match
                    a-FRR ~ RT solar + RT consumption | RT_Consumption: p_value  1.093082224e-82  1.093082225e-82   -7.83591776e-92 abs 1e-09 or rel 1e-06  match
                     a-FRR ~ solar + consumption | Solar_Generation_Share: Beta      8888.802241      8888.802241   -9.33323463e-08 abs 1e-09 or rel 1e-06  match
                   a-FRR ~ solar + consumption | Solar_Generation_Share: t_stat      26.03385478      26.03385478   2.593058213e-09 abs 1e-09 or rel 1e-06  match
                  a-FRR ~ solar + consumption | Solar_Generation_Share: p_value 2.049759051e-149 2.049759189e-149 -1.385773876e-156 abs 1e-09 or rel 1e-06  match
                                a-FRR ~ solar + consumption | Consumption: Beta    -0.1105620446    -0.1105620446   1.730504628e-12 abs 1e-09 or rel 1e-06  match
                              a-FRR ~ solar + consumption | Consumption: t_stat     -18.78164905     -18.78164905    2.95859337e-10 abs 1e-09 or rel 1e-06  match
                             a-FRR ~ solar + consumption | Consumption: p_value  1.067137698e-78  1.067137692e-78   5.946479956e-87 abs 1e-09 or rel 1e-06  match
                                              a-FRR ~ net load | Net_Load: Beta    -0.1392502362    -0.1392502362  -4.163336342e-16 abs 1e-09 or rel 1e-06  match
                                            a-FRR ~ net load | Net_Load: t_stat     -22.46624707     -22.46624707  -3.304023721e-13 abs 1e-09 or rel 1e-06  match
                                           a-FRR ~ net load | Net_Load: p_value 8.878429957e-112 8.878429957e-112 -6.624292839e-123 abs 1e-09 or rel 1e-06  match
                            a-FRR ~ net-load ramp + solar | Net_Load_Ramp: Beta    0.09162458383    0.09162458383   1.749989043e-14 abs 1e-09 or rel 1e-06  match
                          a-FRR ~ net-load ramp + solar | Net_Load_Ramp: t_stat      16.02098574      16.02098574   6.916067719e-11 abs 1e-09 or rel 1e-06  match
                         a-FRR ~ net-load ramp + solar | Net_Load_Ramp: p_value  9.119306161e-58  9.119306171e-58  -1.014292089e-66 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Phase 11.2: comparison with the independent pre-test: 42 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Phase 11.3 - sub-period parameter stability (Supplementary Table J2)

MCP (merit-order), solar coefficient per unit share: Full sample -5,150 (t = -42.9); 2022-2023 -5,781 (t = -25.8); 2024-2025 -5,245 (t = -39.7)
a-FRR (balancing), solar coefficient per unit share: Full sample 8,889 (t = 26.0); 2022-2023 5,731 (t = 12.6); 2024-2025 7,894 (t = 15.8)

```
        Dependent      Period         Beta     t_stat     N
MCP (merit-order) Full sample -5149.820212 -42.859591 35064
MCP (merit-order)   2022-2023 -5780.578238 -25.803617 17520
MCP (merit-order)   2024-2025 -5245.027292 -39.720380 17544
a-FRR (balancing) Full sample  8888.802241  26.033855 35064
a-FRR (balancing)   2022-2023  5730.889786  12.580743 17520
a-FRR (balancing)   2024-2025  7894.186830  15.776282 17544
```

- Phase_11_Robustness/Phase_11_3_SubPeriod.csv (461 bytes, sha256 422b49f5188f)

Checkpoints of this step:
[OK] K45 Phase 11.3: output files: 1 of 1 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Table J2 vs. pre-test (sheet J1_J2)

12 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                              Quantity     This run    Reference       Difference              Tolerance Status
  MCP (merit-order), Full sample: Beta -5149.820212 -5149.820212  5.406764103e-08 abs 1e-09 or rel 1e-06  match
MCP (merit-order), Full sample: t_stat -42.85959144 -42.85959145  2.592123849e-09 abs 1e-09 or rel 1e-06  match
    MCP (merit-order), 2022-2023: Beta -5780.578238 -5780.578238  -7.19774107e-09 abs 1e-09 or rel 1e-06  match
  MCP (merit-order), 2022-2023: t_stat -25.80361654 -25.80361654  1.854871812e-11 abs 1e-09 or rel 1e-06  match
    MCP (merit-order), 2024-2025: Beta -5245.027292 -5245.027292 -1.625267032e-09 abs 1e-09 or rel 1e-06  match
  MCP (merit-order), 2024-2025: t_stat -39.72038033 -39.72038033  6.001243946e-11 abs 1e-09 or rel 1e-06  match
  a-FRR (balancing), Full sample: Beta  8888.802241  8888.802241  -9.33323463e-08 abs 1e-09 or rel 1e-06  match
a-FRR (balancing), Full sample: t_stat  26.03385478  26.03385478  2.593058213e-09 abs 1e-09 or rel 1e-06  match
    a-FRR (balancing), 2022-2023: Beta  5730.889786  5730.889786  7.130438462e-09 abs 1e-09 or rel 1e-06  match
  a-FRR (balancing), 2022-2023: t_stat  12.58074273  12.58074273  3.959002015e-10 abs 1e-09 or rel 1e-06  match
    a-FRR (balancing), 2024-2025: Beta   7894.18683   7894.18683  2.455635695e-09 abs 1e-09 or rel 1e-06  match
  a-FRR (balancing), 2024-2025: t_stat  15.77628212  15.77628212  3.247286884e-10 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Phase 11.3: comparison with the independent pre-test: 12 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Phase 10 (Appendix J): Supplementary Tables J1-J6

Table J4: onset threshold 20% solar share; upper crossover 34.3% solar share (XGBoost interaction simulation, Phase 6.2; descriptive, no confidence interval).
Table J5, hours above each solar share: > 20% 4,154 (11.8%); > 34% 729 (2.1%); Hours above 45% solar share: 79 (0.2%); maximum observed share 59.2%.

```
Solar share  2022  2023  2024  2025  Total % of sample
      > 20%   125   475  1371  2183   4154       11.8%
      > 34%     0    10    89   630    729        2.1%
```

- Phase_10/Appendix_J1_Timing_Robustness.csv (564 bytes, sha256 38ba6c242563)
- Phase_10/Appendix_J2_SubPeriod.csv (200 bytes, sha256 25aa3a1ef1a9)
- Phase_10/Appendix_J3_OutOfSample.csv (300 bytes, sha256 9c693cdeb41a)
- Phase_10/Appendix_J4_Threshold.csv (638 bytes, sha256 eb206561211a)
- Phase_10/Appendix_J5_Threshold_Support.csv (115 bytes, sha256 8992a0657927)
- Phase_10/Appendix_J5_Threshold_Support_Notes.csv (154 bytes, sha256 fd366911eac9)
- Phase_10/Appendix_J5_Clustered_QR.csv (196 bytes, sha256 355171cf7352)
- Phase_11_Robustness/Phase_11_2_Timing_Robustness.csv (2,148 bytes, sha256 ad33853afaa7)
- Phase_11_Robustness/Phase_11_3_SubPeriod.csv (461 bytes, sha256 422b49f5188f)
- Phase_6/Phase_6_4_Out_of_Sample_CV.csv (444 bytes, sha256 cefe37ddbde6)
- Phase_8/Phase_8_2_Hansen_Threshold.csv (537 bytes, sha256 9e05969dce65)
- Phase_6/Phase_6_2_Flexibility_Trap_Crossover.csv (398 bytes, sha256 688a13957131)
- Phase_7/Phase_7_4_QR_Clustered_Bootstrap_SE.csv (275 bytes, sha256 38a5a9a5fb02)

Checkpoints of this step:
[OK] K45 Appendix J: output files: 13 of 13 listed files exist and are not empty

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Supplementary Tables J1, J2 (unrounded source values) and J5 (hours above the thresholds)

41 match, 0 differ, 0 reported without tolerance, 0 without reference (independent pre-test of 20 November 2026).

```
                                                        Quantity      This run     Reference       Difference              Tolerance Status
                                            J5 hours > 20%, 2022           125           125                0 abs 1e-09 or rel 1e-09  match
                                            J5 hours > 20%, 2023           475           475                0 abs 1e-09 or rel 1e-09  match
                                            J5 hours > 20%, 2024          1371          1371                0 abs 1e-09 or rel 1e-09  match
                                            J5 hours > 20%, 2025          2183          2183                0 abs 1e-09 or rel 1e-09  match
                                           J5 hours > 20%, total          4154          4154                0 abs 1e-09 or rel 1e-09  match
                                    J5 share of the sample > 20%  0.1184690851  0.1184690851  2.775557562e-17 abs 1e-09 or rel 1e-09  match
                                            J5 hours > 34%, 2022             0             0                0 abs 1e-09 or rel 1e-09  match
                                            J5 hours > 34%, 2023            10            10                0 abs 1e-09 or rel 1e-09  match
                                            J5 hours > 34%, 2024            89            89                0 abs 1e-09 or rel 1e-09  match
                                            J5 hours > 34%, 2025           630           630                0 abs 1e-09 or rel 1e-09  match
                                           J5 hours > 34%, total           729           729                0 abs 1e-09 or rel 1e-09  match
                                    J5 share of the sample > 34% 0.02079055441 0.02079055441                0 abs 1e-09 or rel 1e-09  match
                           J5 notes: Hours above 45% solar share            79            79                0 abs 1e-09 or rel 1e-09  match
                              J1 MCP - realised, same hour: Beta  -5149.820212  -5149.820212  5.406764103e-08 abs 1e-09 or rel 1e-06  match
                            J1 MCP - realised, same hour: t_stat  -42.85959144  -42.85959145  2.592123849e-09 abs 1e-09 or rel 1e-06  match
                       J1 MCP - solar lagged one day (D-1): Beta  -4020.721173  -4020.721173  1.136868377e-09 abs 1e-09 or rel 1e-06  match
                     J1 MCP - solar lagged one day (D-1): t_stat  -31.02667586  -31.02667586  -9.02034003e-11 abs 1e-09 or rel 1e-06  match
                            J1 a-FRR - realised, same hour: Beta   8888.802241   8888.802241  -9.33323463e-08 abs 1e-09 or rel 1e-06  match
                          J1 a-FRR - realised, same hour: t_stat   26.03385478   26.03385478  2.593058213e-09 abs 1e-09 or rel 1e-06  match
                    J1 a-FRR - solar lagged two days (D-2): Beta    6620.55794   6620.557939  3.709828889e-08 abs 1e-09 or rel 1e-06  match
                  J1 a-FRR - solar lagged two days (D-2): t_stat   20.62862617   20.62862617  1.069182076e-09 abs 1e-09 or rel 1e-06  match
    J1 MCP - real-time solar (D-1) + real-time consumption: Beta  -3830.625236  -3830.625236 -2.253091225e-08 abs 1e-09 or rel 1e-06  match
  J1 MCP - real-time solar (D-1) + real-time consumption: t_stat  -30.24573027  -30.24573027  3.409788008e-10 abs 1e-09 or rel 1e-06  match
       J1 MCP - fully ex-ante (real-time consumption, D-1): Beta  -2958.701208  -2958.701208  1.187208909e-08 abs 1e-09 or rel 1e-06  match
     J1 MCP - fully ex-ante (real-time consumption, D-1): t_stat  -23.54137527  -23.54137527  1.650946047e-11 abs 1e-09 or rel 1e-06  match
  J1 a-FRR - real-time solar (D-2) + real-time consumption: Beta   6524.450735   6524.450735 -1.267380867e-08 abs 1e-09 or rel 1e-06  match
J1 a-FRR - real-time solar (D-2) + real-time consumption: t_stat   20.80965751   20.80965751  1.032827157e-09 abs 1e-09 or rel 1e-06  match
     J1 a-FRR - fully ex-ante (real-time consumption, D-2): Beta   5032.470911   5032.470911  -8.96579877e-09 abs 1e-09 or rel 1e-06  match
   J1 a-FRR - fully ex-ante (real-time consumption, D-2): t_stat   17.05147154   17.05147153  1.124337956e-09 abs 1e-09 or rel 1e-06  match
                         J2 MCP (merit-order), Full sample: Beta  -5149.820212  -5149.820212  5.406764103e-08 abs 1e-09 or rel 1e-06  match
                       J2 MCP (merit-order), Full sample: t_stat  -42.85959144  -42.85959145  2.592123849e-09 abs 1e-09 or rel 1e-06  match
                           J2 MCP (merit-order), 2022-2023: Beta  -5780.578238  -5780.578238  -7.19774107e-09 abs 1e-09 or rel 1e-06  match
                         J2 MCP (merit-order), 2022-2023: t_stat  -25.80361654  -25.80361654  1.854871812e-11 abs 1e-09 or rel 1e-06  match
                           J2 MCP (merit-order), 2024-2025: Beta  -5245.027292  -5245.027292 -1.625267032e-09 abs 1e-09 or rel 1e-06  match
                         J2 MCP (merit-order), 2024-2025: t_stat  -39.72038033  -39.72038033  6.001243946e-11 abs 1e-09 or rel 1e-06  match
                         J2 a-FRR (balancing), Full sample: Beta   8888.802241   8888.802241  -9.33323463e-08 abs 1e-09 or rel 1e-06  match
                       J2 a-FRR (balancing), Full sample: t_stat   26.03385478   26.03385478  2.593058213e-09 abs 1e-09 or rel 1e-06  match
                           J2 a-FRR (balancing), 2022-2023: Beta   5730.889786   5730.889786  7.130438462e-09 abs 1e-09 or rel 1e-06  match
                         J2 a-FRR (balancing), 2022-2023: t_stat   12.58074273   12.58074273  3.959002015e-10 abs 1e-09 or rel 1e-06  match
                           J2 a-FRR (balancing), 2024-2025: Beta    7894.18683    7894.18683  2.455635695e-09 abs 1e-09 or rel 1e-06  match
                         J2 a-FRR (balancing), 2024-2025: t_stat   15.77628212   15.77628212  3.247286884e-10 abs 1e-09 or rel 1e-06  match
```

Checkpoints of this step:
[OK] K17 Appendix J: comparison with the independent pre-test: 41 match, 0 DIFFERS, 0 reported without tolerance, 0 without reference

Warnings raised in this step: none.

## 2026-11-21 04:47:59 | Submission figures: manuscript-numbered export (Figure_1a ... Figure_9)

10 figures copied to '../results/Submission_Figures' under their manuscript numbers (Figure_9.png, the base-case GAM, is Supplementary Figure K.1 since R2 and keeps its R1 name; it is not a manuscript figure).
Copies of figures produced by Phases 5, 6.1, 6.2, 8 and 9: nothing to compare with the independent pre-test.

- Submission_Figures/Figure_1a.png (1,675,770 bytes, sha256 53d0e273c7ae)
- Submission_Figures/Figure_1b.png (1,734,534 bytes, sha256 517f99b35904)
- Submission_Figures/Figure_2.png (2,147,551 bytes, sha256 6825841b9283)
- Submission_Figures/Figure_3.png (469,757 bytes, sha256 cbd2800ac1fe)
- Submission_Figures/Figure_4.png (722,050 bytes, sha256 a771556ea9ed)
- Submission_Figures/Figure_5.png (453,351 bytes, sha256 efaeaa0f8a82)
- Submission_Figures/Figure_6.png (723,501 bytes, sha256 f0a1cc20d115)
- Submission_Figures/Figure_7.png (1,219,063 bytes, sha256 502199ef17c4)
- Submission_Figures/Figure_8.png (1,529,362 bytes, sha256 3941fd4a75cd)
- Submission_Figures/Figure_9.png (1,344,798 bytes, sha256 65fc32b40770)

Checkpoints of this step:
[OK] K45 Submission figures: output files: 10 of 10 listed files exist and are not empty
[OK] K45 Submission figures: dpi tag: 10 of 10 exported figures tagged 1000 dpi

Warnings raised in this step: none.

## 2026-11-21 04:48:00 | Supplementary figures: labelled export (F1, F2, H1, I1, I2, K1)

6 figures copied to '../results/Supplementary_Figures' under their Supplementary labels.
Copies of figures produced by Phase 8.1, Phase 10 (Appendices F and H) and Appendix I: nothing to compare with the independent pre-test.

- Supplementary_Figures/Supplementary_Figure_F1.png (789,115 bytes, sha256 8202c5a9c578)
- Supplementary_Figures/Supplementary_Figure_F2.png (821,315 bytes, sha256 b015180107b4)
- Supplementary_Figures/Supplementary_Figure_H1.png (513,881 bytes, sha256 45671af18979)
- Supplementary_Figures/Supplementary_Figure_I1.png (1,353,784 bytes, sha256 89d53ee0aab9)
- Supplementary_Figures/Supplementary_Figure_I2.png (1,158,707 bytes, sha256 9b5e8aede4a5)
- Supplementary_Figures/Supplementary_Figure_K1.png (1,344,798 bytes, sha256 65fc32b40770)

Checkpoints of this step:
[OK] K45 Supplementary figures: output files: 6 of 6 listed files exist and are not empty
[OK] K45 Supplementary figures: dpi tag: 6 of 6 exported figures tagged 1000 dpi

Warnings raised in this step: none.

## 2026-11-21 04:48:00 | End of run: checkpoints and recorded warnings

Checkpoints: 85 ok, 7 warning, 0 failed, 0 not checked; warnings recorded: 2 (1 distinct entries).
The record covers this kernel session (setup cell executed 2026-11-21 02:40:14). A check that needs a value of the estimation itself is NOT CHECKED when that result was loaded from the results folder; a complete record needs one kernel session that starts from an empty results folder.

Checkpoints that are not OK (step | [status] name: detail):
- Phase 4: optimized models | [WARNING] K17 Phase 4: comparison with the independent pre-test (optimized models): 128 match, 3 DIFFERS, 0 reported without tolerance, 0 without reference; DIFFERS explained by the mirror image of the seasonal MA term in the pre-test: Model 5: log-likelihood, Model 5: AIC, Model 5: ma.S.L24
- Phase 7.4 - Day-clustered block-bootstrap QR standard errors (Supplementary Table J6) | [WARNING] K32 Phase 7.4: bootstrap replicates at the iteration limit: 15 of 1,200 replicates (1.25%) stopped at the 5,000-iteration limit and are kept in the standard error: MCP Q10 0 of 200 (0.0%); MCP Q50 4 of 200 (2.0%); MCP Q90 3 of 200 (1.5%); aFRR Q10 6 of 200 (3.0%); aFRR Q50 1 of 200 (0.5%); aFRR Q90 1 of 200 (0.5%); diagnostic re-solve with up to 50,000 iterations: 0 still at the limit, largest change of the clustered SE 0.002% (Table J6 keeps the replicates as estimated)
- Appendix B - ADF and KPSS stationarity tests (Supplementary Table B1) | [WARNING] K43 Appendix B: KPSS p-values at the table bounds: 4 of 4 KPSS p-values are bounds of the table, reported as bounds: MCP (Day-Ahead Price): p < 0.01 (statistic 2.1447); a-FRR Price (Level): p < 0.01 (statistic 0.7479); a-FRR Price (1st Difference): p > 0.10 (statistic 0.0045); Solar Generation Share: p < 0.01 (statistic 19.5317)
- Appendix I: flexibility trap and GAM flexibility-stress with the Botas tariff as a control | [WARNING] K42 Appendix I: flexibility-trap crossover: crossover = the last upward crossing of the surplus curve over the deficit/balanced curve after which it stays above up to the end of the common range (0-45%): none (no sustained crossover); upward crossings: 2.16, 23.96, 35.70% solar share; downward crossings: 1.16, 4.06, 29.00, 36.44% solar share
- Appendix I: crossover (Figure I.1) and GAM fit (Figure I.2) | [WARNING] K17 Appendix I: comparison with the independent pre-test: 2 match, 1 DIFFERS, 0 reported without tolerance, 0 without reference; DIFFERS explained by the pre-test value being the last upward crossing, after which the surplus curve falls below again (section above): Figure I.1 crossover, % solar share
- End of run: checkpoints and recorded warnings | [WARNING] K90 run: comparison with the independent pre-test, total of all comparison tables: 24 tables: 651 match, 4 DIFFERS, 0 reported without tolerance, 0 without reference; DIFFERS in: 'Phase 4: optimized models' (3); 'Appendix I: crossover (Figure I.1) and GAM fit (Figure I.2)' (1)
- End of run: checkpoints and recorded warnings | [WARNING] K91 run: warnings recorded: 2 warning(s) in 1 distinct entries: UserWarning x2 (Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept); main; process_executor.py:787)

All recorded warnings (step | category | where | location | message | count):
- Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept) | UserWarning | main | process_executor.py:787 | A worker stopped while some jobs were given to the executor. This can be caused by a too short worker timeout or by a memory leak. | x2

```
                                                                                                                    step                                                                                                                     name  status
                                                                                                         Setup (new run)                                                        K05 environment: package versions equal the reference environment      OK
                                                                                                         Setup (new run)                        K06 design: a constant for the MCP models only; SARIMAX orders as documented (SARIMAX_METHOD_TAG)      OK
                                                                                      Phase 1: data ingestion and checks                                                   K01 data: hourly time index, strictly increasing, no duplicate, no gap      OK
                                                                                      Phase 1: data ingestion and checks         K02 data: Solar_Generation_Share in [0, 1] and equal to solar generation / the total implied by the other shares      OK
                                                                                      Phase 1: data ingestion and checks K03 data: calendar terms follow the time index (weekend flag, weekday dummies, hour, month; 12-month and 24-hour cycles)      OK
                                                                                      Phase 1: data ingestion and checks                                                                 K04 data: no missing value in any column used by a model      OK
                                   Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)                                                                   K10 Phase 2: every reported model certified or plateau      OK
                                   Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)                                                                          K11 Phase 2: reported representation invertible      OK
                                   Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)                                              K12 Phase 2: at least two starts within 0.01 of the reported log-likelihood      OK
                                   Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)                                        K13 Phase 2: 'const' among the regressors exactly in the models with an intercept      OK
                                   Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)                                                       K14 Phase 2: day clusters = calendar days of the estimation sample      OK
                                   Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)                                                                                      K16 Phase 2: no standard-error flag      OK
                                   Phase 2: baseline models (SARIMAX(1,1,1)(1,0,1)24 without intercept; logit Model 7.1)                                                                                                K45 Phase 2: output files      OK
                                                                                                Phase 2: baseline models                                                                    K17 Phase 2: comparison with the independent pre-test      OK
                                                    Phase 3: seasonality diagnostics (ACF/PACF) and order selection note                                                                                                K45 Phase 3: output files      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)                                                                   K10 Phase 4: every reported model certified or plateau      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)                                                                          K11 Phase 4: reported representation invertible      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)                                              K12 Phase 4: at least two starts within 0.01 of the reported log-likelihood      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)                                        K13 Phase 4: 'const' among the regressors exactly in the models with an intercept      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)                                                       K14 Phase 4: day clusters = calendar days of the estimation sample      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)                                                                                      K16 Phase 4: no standard-error flag      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)            K15 Phase 4: likelihood-ratio tests (restricted and unrestricted estimates invertible, consistency flag True)      OK
 Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept)                                                                                                K45 Phase 4: output files      OK
                                                                                               Phase 4: optimized models                                                 K17 Phase 4: comparison with the independent pre-test (optimized models) WARNING
                                                      Phase 4: standard errors of the solar coefficient (Models 1 and 4)                         K17 Phase 4: comparison with the independent pre-test (standard errors of the solar coefficient)      OK
                                                Phase 5: daily market profiles and hourly SARIMAX coefficients (figures)                                                                                                K45 Phase 5: output files      OK
                                                    Phase 5: hourly coefficients drawn in the bar figures (Phase 4 file)                                                                    K17 Phase 5: comparison with the independent pre-test      OK
                                                     Phase 6.1: XGBoost partial dependence on the solar generation share                                                                                 K41 Phase 6.1: partial-dependence values      OK
                                                     Phase 6.1: XGBoost partial dependence on the solar generation share                                                                                              K45 Phase 6.1: output files      OK
                                                      Phase 6.1: partial dependence, every 10th grid point of each curve                                                                  K17 Phase 6.1: comparison with the independent pre-test      OK
                                                            Phase 6.2: flexibility trap (XGBoost interaction simulation)                                                                                K42 Phase 6.2: flexibility-trap crossover      OK
                                                            Phase 6.2: flexibility trap (XGBoost interaction simulation)                                                                                              K45 Phase 6.2: output files      OK
                                                                     Phase 6.2: crossover of the flexibility-trap curves                                                                  K17 Phase 6.2: comparison with the independent pre-test      OK
                                     Phase 6.4: out-of-sample validation of the XGBoost models (5-fold expanding window)                                                                        K41 Phase 6.4: walk-forward folds and fit metrics      OK
                                     Phase 6.4: out-of-sample validation of the XGBoost models (5-fold expanding window)                                                                                              K45 Phase 6.4: output files      OK
                                                                      Phase 6.4: walk-forward validation (fold averages)                                                                  K17 Phase 6.4: comparison with the independent pre-test      OK
                                                                         Phase 7.1 - Quantile regression (Q10, Q50, Q90)                                                                K30 Phase 7.1: full-sample quantile regressions converged      OK
                                                                         Phase 7.1 - Quantile regression (Q10, Q50, Q90)                                                                                              K45 Phase 7.1: output files      OK
                                                                         Phase 7.1 - quantile-regression point estimates                                                                  K17 Phase 7.1: comparison with the independent pre-test      OK
                                                       Phase 7.2 - QR solver iteration sensitivity (unscaled regressors)                                                                                     K31 Phase 7.2: iteration-limit marks      OK
                                                       Phase 7.2 - QR solver iteration sensitivity (unscaled regressors)                                                                                              K45 Phase 7.2: output files      OK
                                                              Phase 7.3 - Exact QR solution (linear programming) vs IRLS                                                         K30 Phase 7.3: exact LP solutions and scaled IRLS fits converged      OK
                                                              Phase 7.3 - Exact QR solution (linear programming) vs IRLS                                                                                              K45 Phase 7.3: output files      OK
                                                              Phase 7.3 - exact (LP) quantile-regression point estimates                                                                  K17 Phase 7.3: comparison with the independent pre-test      OK
                                   Phase 7.4 - Day-clustered block-bootstrap QR standard errors (Supplementary Table J6)                                                                K30 Phase 7.4: full-sample quantile regressions converged      OK
                                   Phase 7.4 - Day-clustered block-bootstrap QR standard errors (Supplementary Table J6)                                                                     K32 Phase 7.4: bootstrap replicates without an error      OK
                                   Phase 7.4 - Day-clustered block-bootstrap QR standard errors (Supplementary Table J6)                                                               K32 Phase 7.4: bootstrap replicates at the iteration limit WARNING
                                   Phase 7.4 - Day-clustered block-bootstrap QR standard errors (Supplementary Table J6)                                                                                              K45 Phase 7.4: output files      OK
                                                 Phase 7.4 - quantile regression with day-clustered bootstrap (Table J6)                                                                  K17 Phase 7.4: comparison with the independent pre-test      OK
                                                   Phase 8.1 - GAM flexibility-stress pattern (Supplementary Figure K.1)                                                                                              K45 Phase 8.1: output files      OK
                                    Phase 8.1 - GAM report vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)                                                                  K17 Phase 8.1: comparison with the independent pre-test      OK
                                                          Phase 8.2 - regression-kink threshold (Supplementary Table J4)                                                                                 K40 Phase 8.2: kink bootstrap replicates      OK
                                                          Phase 8.2 - regression-kink threshold (Supplementary Table J4)                                                                  K40 Phase 8.2: interval contains the threshold estimate      OK
                                                          Phase 8.2 - regression-kink threshold (Supplementary Table J4)                                                                                              K45 Phase 8.2: output files      OK
                                                                Phase 8.2 - regression kink vs. pre-test (sheet Kink_J4)                                                                  K17 Phase 8.2: comparison with the independent pre-test      OK
                                                                              Phase 9: methodological framework (figure)                                                                                                K45 Phase 9: output files      OK
                                 Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)                                                                                                K10 Table C1: convergence      OK
                                 Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)                                                                         K11 Table C1: reported representation invertible      OK
                                 Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)                                                                                    K12 Table C1: agreement of the starts      OK
                                 Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)                                                                                   K13 Table C1: intercept and regressors      OK
                                 Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)                                                                                          K14 Table C1: estimation sample      OK
                                 Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)                                                                 K16 Table D1: standard-error flags of the Phase 4 models      OK
                                 Phase 10: Appendices A-F and H (Tables A1, B1 (ADF), C1, D1, E1; Figures F.1, F.2, H.1)                                                                                               K45 Phase 10: output files      OK
                                                    Table A1 (solar generation share) and the ADF statistics of Table B1                                                        K17 Table A1 / B1 (ADF): comparison with the independent pre-test      OK
                                                  Supplementary Table C1 (model selection on a common likelihood sample)                                                                   K17 Table C1: comparison with the independent pre-test      OK
Supplementary Table D1: hypothesis variables of the eight models (coefficient; standard error clustered by calendar day)                                                                   K17 Table D1: comparison with the independent pre-test      OK
                                                   Appendix B - ADF and KPSS stationarity tests (Supplementary Table B1)                                                                        K43 Appendix B: KPSS p-values at the table bounds WARNING
                                                   Appendix B - ADF and KPSS stationarity tests (Supplementary Table B1)                                                                                             K45 Appendix B: output files      OK
                                                  Table B1 vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)                                                                 K17 Appendix B: comparison with the independent pre-test      OK
                              Appendix I: flexibility trap and GAM flexibility-stress with the Botas tariff as a control                                                                               K42 Appendix I: flexibility-trap crossover WARNING
                              Appendix I: flexibility trap and GAM flexibility-stress with the Botas tariff as a control                                                                                             K45 Appendix I: output files      OK
                                                             Appendix I: crossover (Figure I.1) and GAM fit (Figure I.2)                                                                 K17 Appendix I: comparison with the independent pre-test WARNING
                         Phase 11.1 - inflation robustness, ratio and cap-normalised FE-OLS (Supplementary Appendix J.6)                                                                                           K44 Appendix J.6: day clusters      OK
                         Phase 11.1 - inflation robustness, ratio and cap-normalised FE-OLS (Supplementary Appendix J.6)                                                                                           K45 Appendix J.6: output files      OK
                                              Appendix J.6 vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)                                                               K17 Appendix J.6: comparison with the independent pre-test      OK
                                            Supplementary: in-sample fit of the XGBoost models (Phase 6.1 and Phase 6.2)                                                                         K41 Supplementary metrics: XGBoost in-sample fit      OK
                                            Supplementary: in-sample fit of the XGBoost models (Phase 6.1 and Phase 6.2)                                                                          K45 Supplementary XGBoost metrics: output files      OK
                                                                                 XGBoost performance metrics (in-sample)                                              K17 Supplementary XGBoost metrics: comparison with the independent pre-test      OK
                                                                   Supplementary metrics - GAM fit by regime (R-squared)                                                                              K45 Supplementary GAM metrics: output files      OK
                                           GAM fit metrics vs. pre-test (pre-test sheet Hizli_Analizler, quick analyses)                                                  K17 Supplementary GAM metrics: comparison with the independent pre-test      OK
                                 Phase 11.2 - timing, decision-time information and confounding (Supplementary Table J1)                                                                                             K45 Phase 11.2: output files      OK
                                                                                     Table J1 vs. pre-test (sheet J1_J2)                                                                 K17 Phase 11.2: comparison with the independent pre-test      OK
                                                    Phase 11.3 - sub-period parameter stability (Supplementary Table J2)                                                                                             K45 Phase 11.3: output files      OK
                                                                                     Table J2 vs. pre-test (sheet J1_J2)                                                                 K17 Phase 11.3: comparison with the independent pre-test      OK
                                                                       Phase 10 (Appendix J): Supplementary Tables J1-J6                                                                                             K45 Appendix J: output files      OK
                               Supplementary Tables J1, J2 (unrounded source values) and J5 (hours above the thresholds)                                                                 K17 Appendix J: comparison with the independent pre-test      OK
                                                 Submission figures: manuscript-numbered export (Figure_1a ... Figure_9)                                                                                     K45 Submission figures: output files      OK
                                                 Submission figures: manuscript-numbered export (Figure_1a ... Figure_9)                                                                                          K45 Submission figures: dpi tag      OK
                                                         Supplementary figures: labelled export (F1, F2, H1, I1, I2, K1)                                                                                  K45 Supplementary figures: output files      OK
                                                         Supplementary figures: labelled export (F1, F2, H1, I1, I2, K1)                                                                                       K45 Supplementary figures: dpi tag      OK
                                                                           End of run: checkpoints and recorded warnings                                        K90 run: comparison with the independent pre-test, total of all comparison tables WARNING
                                                                           End of run: checkpoints and recorded warnings                                                                                               K91 run: warnings recorded WARNING
```

- RUN_CHECKPOINTS.csv (22,855 bytes, sha256 676c7b45dbf9)

Checkpoints of this step:
[WARNING] K90 run: comparison with the independent pre-test, total of all comparison tables: 24 tables: 651 match, 4 DIFFERS, 0 reported without tolerance, 0 without reference; DIFFERS in: 'Phase 4: optimized models' (3); 'Appendix I: crossover (Figure I.1) and GAM fit (Figure I.2)' (1)
[WARNING] K91 run: warnings recorded: 2 warning(s) in 1 distinct entries: UserWarning x2 (Phase 4: optimized models (MCP SARIMAX(2,0,2)(1,0,1)24 with intercept; a-FRR SARIMAX(1,1,2)(1,0,1)24 without intercept); main; process_executor.py:787)

Warnings raised in this step: none.

