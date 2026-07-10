# Data

## Source

All data are sourced from the **EPİAŞ (Energy Exchange Istanbul) Transparency Platform**:
https://seffaflik.epias.com.tr/home

## Dataset

**`Model_Data.xlsx`** — Hourly electricity market data for Türkiye, January 2022 – December 2025.

| Property | Value |
|----------|-------|
| Observations | 35,064 (hourly) |
| Columns | 46 |
| Temporal index | `Date_Hour` |

The workbook contains a single sheet (**`Sheet1`**) holding the hourly analysis dataset.
The `Public_Holiday` dummy is constructed from the official Turkish public-holiday
calendar (2022–2025).

## Key Variables

| Variable | Unit | Description |
|----------|------|-------------|
| `Mcp` | TL/MWh | Market Clearing Price (day-ahead) |
| `a-FRR_Price` | TL/MW | Automatic Frequency Restoration Reserve capacity price |
| `Solar_Generation_Share` | proportion (0–1) | Hourly solar generation / total generation |
| `Consumption` | MWh | Hourly electricity consumption |
| `System_Direction_Down` | 0/1 | 1 = Energy Surplus (down-regulation needed) |
| `System_Direction_Up` | 0/1 | 1 = Energy Deficit (up-regulation needed) |
| `Botas_Tariff` | TL/m³ | BOTAŞ natural gas tariff (Appendix I robustness) |
| `BPM_Down_Regulation_Volume` | MWh | Manual down-regulation volume (Appendix H) |

## Other Variables

Generation by fuel type (Solar, Wind, Natural Gas, Import Coal, Domestic Coal, Hydroelectric),
generation shares and first-differences, temporal features (`Hour_Sin`, `Hour_Cos`, `Month_Sin`,
`Month_Cos`), day-of-week dummies (`Monday`–`Saturday`), `Price_Cap`, and normalized price ratios.

## Path Resolution

The analysis notebook looks for the file at `data/Model_Data.xlsx` first, then
`../data/Model_Data.xlsx`, then the working directory — so it runs from either the
repository root or the `notebooks/` folder.

## Citation

> Enerji Piyasaları İşletme A.Ş. (EPİAŞ). (n.d.). *EPİAŞ Transparency Platform.* Retrieved March 5, 2026, from https://seffaflik.epias.com.tr/home
