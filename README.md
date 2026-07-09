# Enterprise Risk Management (ERM) Platform

A web-based Enterprise Risk Management (ERM) platform built using **Python** and **Streamlit**. This project demonstrates risk management, compliance tracking, audit reporting, role-based authentication, interactive dashboards, data visualization, and report exporting.

---

## Overview

The Enterprise Risk Management Platform helps organizations identify, monitor, and manage risks while tracking compliance requirements and audit reports. The application uses interactive visualizations and role-based access control to provide different levels of functionality for administrators, managers, and viewers.

---

<img width="1919" height="632" alt="Screenshot 2026-07-09 142039" src="https://github.com/user-attachments/assets/e5b970a8-70cd-4d5a-8941-689ee25a40bb" />

<img width="1904" height="970" alt="Screenshot 2026-07-09 142117" src="https://github.com/user-attachments/assets/add9f9a2-156e-4baf-94ef-0c82acb47bb7" />

<img width="1908" height="856" alt="Screenshot 2026-07-09 142223" src="https://github.com/user-attachments/assets/f9bd7a07-ffb8-435b-a05e-c869c5ceb53b" />

<img width="1916" height="794" alt="Screenshot 2026-07-09 142346" src="https://github.com/user-attachments/assets/1be7bd7c-e05a-4237-bfdf-317f558e5a2c" />

<img width="1916" height="776" alt="Screenshot 2026-07-09 142443" src="https://github.com/user-attachments/assets/9042140b-8a19-4706-a60e-b5be161a2a5f" />


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
