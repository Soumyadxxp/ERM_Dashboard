# Enterprise Risk Management (ERM) Platform

A web-based Enterprise Risk Management (ERM) platform built using **Python** and **Streamlit**. This project demonstrates risk management, compliance tracking, audit reporting, role-based authentication, interactive dashboards, data visualization, and report exporting.

---

## Overview

The Enterprise Risk Management Platform helps organizations identify, monitor, and manage risks while tracking compliance requirements and audit reports. The application uses interactive visualizations and role-based access control to provide different levels of functionality for administrators, managers, and viewers.

---

## Features

### Authentication

- Secure login system
- Role-based access control
- Three predefined user roles:
  - Admin
  - Manager
  - Viewer

### Dashboard

- Displays key risk metrics
- Total number of risks
- High/Critical risks
- Medium risks
- Low risks
- Interactive Risk Heat Map
- Risk Category Distribution Pie Chart

### Risk Register

- View organizational risks
- Risk ID
- Category
- Description
- Likelihood
- Impact
- Risk Level
- Export to Excel
- Export to PDF

### Compliance Management

- Track compliance requirements
- Regulation
- Requirement
- Status
- Due Date
- Owner
- Export to Excel
- Export to PDF

### Audit Reports

- View audit reports
- Audit ID
- Audit Type
- Scope
- Date
- Status
- Findings
- Export to Excel
- Export to PDF

### Data Generation

- Automatic sample data generation using Faker
- Admin can regenerate all datasets with one click
- CSV-based storage

---

## User Roles

| Feature | Admin | Manager | Viewer |
|---------|:-----:|:-------:|:------:|
| Dashboard | Yes | Yes | Yes |
| Risk Register | Yes | Yes | No |
| Compliance | Yes | Yes | No |
| Audit Reports | Yes | No | No |
| Export Reports | Yes | Yes | No |
| Regenerate Data | Yes | No | No |

---

## Technologies Used

- Python 3
- Streamlit
- Pandas
- Plotly
- Faker
- ReportLab
- OpenPyXL

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ERM_dashboard.git
```

Navigate to the project directory:

```bash
cd ERM_dashboard
```

Install the required dependencies:

```bash
pip install streamlit pandas plotly openpyxl reportlab faker
```

Run the application:

```bash
streamlit run app.py
```

---

## Default Login Credentials

| Username | Password | Role |
|----------|----------|------|
| admin | pass | Admin |
| manager | pass | Manager |
| viewer | pass | Viewer |

---

## Data Storage

The application stores data in CSV files.

```
risks.csv
compliance.csv
audit.csv
```

If these files do not exist, they are automatically generated using the Faker library.

---

## Report Export

Authorized users can export reports in the following formats:

- Excel (.xlsx)
- PDF (.pdf)

---



## Future Enhancements

- Database integration (PostgreSQL/MySQL)
- User registration
- Password hashing
- Multi-factor authentication
- Risk mitigation workflow
- Risk approval process
- Email notifications
- AI-based risk prediction
- REST API integration
- Docker support
- Cloud deployment
- Audit logs
- User activity monitoring
- File upload support
- Dashboard report generation

---


## Acknowledgements

This project uses the following open-source libraries:

- Streamlit
- Pandas
- Plotly
- Faker
- ReportLab
- OpenPyXL

---
