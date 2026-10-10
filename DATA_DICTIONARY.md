# Banking EDA Practice Dataset — Data Dictionary

This is a synthetic practice dataset. All records are fictional and intended for learning, not real credit decisions.

## Tables and grain
- customers.csv: one intended row per customer; contains a few exact duplicate rows.
- loans.csv: one intended row per loan; contains a few deliberate quality issues and a duplicate row.
- repayments.csv: one row per scheduled repayment; one loan can have many repayments.
- transactions.csv: one row per transaction; one customer can have many transactions.
- branches.csv: one intended row per branch.

## Join keys
- customers.customer_id -> loans.customer_id (one customer to many loans)
- loans.loan_id -> repayments.loan_id (one loan to many repayments)
- customers.customer_id -> transactions.customer_id (one customer to many transactions)
- branches.branch_id -> customers.branch_id and loans.branch_id (one branch to many records)

## Deliberate issues to discover
- Missing values in several columns.
- Numeric values stored as strings, including values with units or invalid text.
- Invalid dates.
- Inconsistent capitalization and whitespace in category fields.
- Implausible values, such as a negative loan amount or age outside a reasonable range.
- Exact duplicate rows and duplicate business keys.
- Some unmatched references may arise when records are filtered or cleaned.

Do not blindly clean everything. First profile the data, document the issue, and choose a defensible treatment.
