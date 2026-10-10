# Python EDA Practice Plan

## Phase 1 — Data loading and profiling
1. Load all five CSVs.
2. Print shape, head, sample, info, dtypes, describe(include='all').
3. Identify the grain and candidate keys for every table.
4. Compare memory usage before and after appropriate dtype conversions.

## Phase 2 — Data quality
5. Calculate missing counts, percentages and fill rates by column.
6. Find exact duplicate rows and duplicate keys.
7. Inspect unique values and category frequencies.
8. Identify invalid numeric strings, invalid dates, negative amounts and implausible ages.
9. Create a quality report before cleaning.

## Phase 3 — Cleaning and transformation
10. Convert numeric strings using pd.to_numeric(errors='coerce').
11. Convert dates with pd.to_datetime(errors='coerce', dayfirst=... as appropriate).
12. Standardize text with str.strip(), str.lower() or str.title().
13. Use replace(), map(), apply(), lambda, np.where(), cut() and qcut().
14. Compare missingness and row counts before/after each transformation.

## Phase 4 — Statistics and distributions
15. Calculate mean, median, mode, variance, standard deviation, quartiles, IQR, skew and kurtosis.
16. Compare mean and median for loan amounts and transaction amounts.
17. Detect potential outliers with IQR and Z-score; explain why a flagged value may be valid.
18. Compare metrics across product, region, customer segment and status.

## Phase 5 — Grouping and joins
19. Use groupby().agg() for multiple summary metrics.
20. Compare agg() versus transform() and filter().
21. Merge customers with loans and validate join cardinality.
22. Join loans to repayments; inspect row multiplication and reconcile totals.
23. Use merge(indicator=True) to inspect unmatched records.

## Phase 6 — Cumulative and time-based analysis
24. Sort transactions chronologically.
25. Calculate customer-level cumulative spending with groupby().cumsum().
26. Use shift(), diff(), pct_change(), rolling() and resample().
27. Create monthly loan originations and repayment trends.
28. Rank customers, loans, branches and merchant categories.

## Phase 7 — Visualization and storytelling
29. Draw histograms, box plots, bar charts, line charts, scatter plots and correlation heatmaps.
30. Write a short summary: three data-quality findings, three trends, two business risks and two recommendations.

## Important
The dataset is synthetic. Values and patterns are generated for practice and should not be treated as representative of real banking portfolios.
