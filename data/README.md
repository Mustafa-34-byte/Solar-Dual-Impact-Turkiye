# Dataset: `Model_Data.xlsx`

Hourly data for the Turkish electricity market, 1 January 2022 00:00 – 31 December 2025 23:00: 35,064 rows (1,461
calendar days) and 48 columns, no missing values. This file is the input of every result of release
`RENE-D-26-09232-R2`.

**SHA-256:** `71e299d35f23f818e059e7e952700fc669ac778823074f10ec68b3f35369a78c`

The notebook computes this checksum at start-up and stops if the file does not match it, so no result can be produced
from another file by accident. Phase 1 then checks the structure of the file (complete hourly grid, no missing values,
`Date` equal to the calendar day of `Date_Hour`, month terms on a 12-month cycle, `Weekend` equal to Saturday or Sunday,
solar share within [0, 1] and equal to solar generation divided by the total generation implied by the other share
columns, checkpoints K01–K04; total generation itself is not a column of the file) and stops if a check fails.

## Sources

As documented in the manuscript (data section and "Data and code availability") and the Supplementary Material:

- the market, generation and consumption series are publicly available from the
  [EPİAŞ Transparency Platform](https://seffaflik.epias.com.tr/home) (Energy Exchange Istanbul);
- the real-time series `RT_Solar_Generation_Share` and `RT_Consumption`, used only in the timing check of Supplementary
  Appendix J.1, are published by the system operator, TEİAŞ;
- `Botas_Tariff` is the regulated natural-gas tariff of BOTAŞ (Petroleum Pipeline Corporation), used as an additional
  control in Supplementary Appendix I and in the fixed-effects check of Appendix J.6.

The calendar, Fourier, share, ratio and difference columns are constructed from these series and from the time index
when the file is assembled. The data-assembly step (from the platform downloads to this workbook) is not part of this
package; the SHA-256 above identifies the file used for every result.

## Columns

| Group | Columns | Notes |
| --- | --- | --- |
| Time | `Date`, `Date_Hour` | `Date_Hour` is the hourly time index; `Date` is its calendar day |
| Calendar | `Hour`, `Month`, `Hour_Sin`, `Hour_Cos`, `Month_Sin`, `Month_Cos`, `Weekend`, `Public_Holiday`, `Monday` … `Saturday`, `Trend` | sine/cosine terms on a 24-hour and a 12-month cycle; day-of-week dummies Monday–Saturday; `Trend` counts the hours 1 … 35,064 and is not used by the notebook |
| System state | `System_Direction_Up`, `System_Direction_Down`, `System_Direction_Balanced` | 1 for an energy deficit (upward regulation), an energy surplus (downward regulation) or neither (balanced); Supplementary Table S2 |
| Prices | `Mcp`, `a-FRR_Price`, `Price_Cap`, `Mcp_Divide_Price_Cap`, `a-FRR_Price_Divide_Price_Cap` | day-ahead market clearing price (TL/MWh), a-FRR capacity price (TL/MW), day-ahead price cap and the two prices divided by it |
| Load and generation | `Consumption`, `Solar_Generation`, `Wind_Generation`, `Natural_Gas_Generation`, `Import_Coal_Generation`, `Hydroelectric_Generation`, `Domestic_Coal_Generation` | hourly values (MWh) |
| Generation shares | `Solar_Generation_Share`, `Wind_Generation_Share`, `Natural_Gas_Generation_Share`, `Import_Coal_Generation_Share`, `Hydroelectric_Generation_Share`, `Domestic_Coal_Generation_Share` | share of total generation (0–1); `Solar_Generation_Share` is the main explanatory variable |
| Differences | `Solar_Generation_Diff`, `Wind_Generation_Diff`, `Natural_Gas_Generation_Diff`, `Import_Coal_Generation_Diff`, `Hydroelectric_Generation_Diff`, `Domestic_Coal_Generation_Diff` | not used in any model |
| Balancing volume | `BPM_Down_Regulation_Volume` | manual down-regulation volume (Supplementary Figure H.1) |
| Gas tariff | `Botas_Tariff` | see Sources |
| Real-time series | `RT_Solar_Generation_Share`, `RT_Consumption` | Appendix J.1 only |

The variables that enter the models are listed in Supplementary Table S2. The notebook reports 47 data columns because
it uses `Date_Hour` as the index.
