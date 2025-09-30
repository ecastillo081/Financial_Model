# Financial Model v1.0

This repository contains a traditional **3-statement financial model** built in Excel and exported to PDF for review.  
All figures are **synthetic** and represent a fictional startup — created for portfolio and demonstration purposes only.

## What’s Included
- **Financial Model.xlsx** → full Excel model (3-Statement, Drivers, CapEx ROI, KPIs, Headcount, Marketing, etc.).
- **Financial Model.pdf** → [Viewable PDF export](Financial Model.pdf) for quick browsing without Excel.
- **export_to_pdf.py** → Python script to automate PDF export of all tabs.

## Key Features
- **3-Statement Forecast**: Integrated P&L, Balance Sheet, and Cash Flow.  
- **Drivers & Assumptions**: Revenue growth, COGS %, OpEx, headcount, rent, marketing.  
- **CapEx ROI Analysis**: Links capital spending to returns and cash runway.  
- **Headcount & Operating Expense Planning**: Modeled salaries, benefits, and overhead.  
- **KPI Tracking**: Revenue per employee, EBITDA margin, and growth efficiency.  
- **Scenario-Ready**: Structure supports toggling key drivers (growth, margins, CapEx) for sensitivity analysis.

## Folder Structure
```
financial-model-project/
├─ financial_model/             # Excel model (.xlsx)
├─ pdf/                         # PDF exports of model
├─ scripts/                     # Python helpers (export script)
└─ README.md                    # Project overview
```

## Future Enhancements

Planned updates and improvements for future versions of this model include:

- **Prepaid User Discounts** – add % discount logic for prepaid contracts.  
- **Credit vs. Non-Credit Users** – bifurcate revenue and cost assumptions by payment terms.  
- **Inflation Impact** – incorporate inflation factors into expense and revenue growth.  
- **Net Revenue Retention (NRR)** – track expansion, contraction, and churn to show net retention.  
- **Gross Revenue Retention (GRR)** – highlight customer stickiness and gross retention trends.  
- **Take Rate** – introduce take rate assumptions for marketplace/transaction-driven revenue.  
- **Executive Dashboard** – build a high-level KPI dashboard for quick insights and presentation.

## Disclaimer
All data in this model is **synthetic**.

No license is granted for commercial or reproduction.