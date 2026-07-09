import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO
import base64
from datetime import datetime, timedelta
import random
import os
from faker import Faker

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="ERM Platform", layout="wide")

# ---------- SESSION STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = "Viewer"
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"
if "logout_clicked" not in st.session_state:
    st.session_state.logout_clicked = False
if "regenerate_clicked" not in st.session_state:
    st.session_state.regenerate_clicked = False

# ---------- HARDCODED USERS ----------
USERS = {
    "admin": {"password": "pass", "role": "Admin"},
    "manager": {"password": "pass", "role": "Manager"},
    "viewer": {"password": "pass", "role": "Viewer"},
}

# ---------- FAKER SETUP ----------
fake = Faker()
CSV_RISKS = "risks.csv"
CSV_COMPLIANCE = "compliance.csv"
CSV_AUDIT = "audit.csv"

# ---------- DATA GENERATORS ----------
def generate_risks(n=15):
    categories = ["Operational", "Financial", "Strategic", "Compliance", "IT", "Reputational"]
    likelihoods = ["Very Low", "Low", "Medium", "High", "Very High"]
    impacts = ["Low", "Medium", "High", "Critical"]
    data = []
    for i in range(1, n+1):
        cat = random.choice(categories)
        lik = random.choice(likelihoods)
        imp = random.choice(impacts)
        if lik in ["High", "Very High"] and imp in ["High", "Critical"]:
            level = "Critical"
        elif lik in ["High", "Very High"] or imp in ["High", "Critical"]:
            level = "High"
        elif lik == "Medium" and imp == "Medium":
            level = "Medium"
        else:
            level = "Low"
        data.append({
            "ID": f"R-{i:03d}",
            "Category": cat,
            "Description": fake.sentence(nb_words=6),
            "Likelihood": lik,
            "Impact": imp,
            "Risk Level": level,
        })
    return pd.DataFrame(data)

def generate_compliance(n=8):
    regulations = ["GDPR", "SOX", "ISO 27001", "PCI-DSS", "HIPAA", "CCPA", "NIST", "Basel III"]
    statuses = ["Compliant", "In Progress", "Non-compliant", "Not Started"]
    owners = ["DPO", "CFO", "CISO", "IT Director", "Compliance Officer", "Legal Counsel"]
    data = []
    for i in range(1, n+1):
        reg = random.choice(regulations)
        data.append({
            "Regulation": reg,
            "Requirement": f"{reg} {fake.word().capitalize()} {fake.word()} policy",
            "Status": random.choice(statuses),
            "Due Date": (datetime.now() + timedelta(days=random.randint(30, 180))).strftime("%Y-%m-%d"),
            "Owner": random.choice(owners),
        })
    return pd.DataFrame(data)

def generate_audit(n=6):
    types = ["Internal", "External", "Regulatory", "Compliance"]
    scopes = ["Financial controls", "IT security", "Compliance (GDPR)", "Supply chain", "Fraud detection", "Operational efficiency"]
    statuses = ["Completed", "In Progress", "Scheduled", "Pending Review"]
    findings = ["0 findings", "1 minor", "2 minor", "1 major", "N/A"]
    data = []
    for i in range(1, n+1):
        data.append({
            "Audit ID": f"A-{i:03d}",
            "Type": random.choice(types),
            "Scope": random.choice(scopes),
            "Date": (datetime.now() - timedelta(days=random.randint(0, 120))).strftime("%Y-%m-%d"),
            "Status": random.choice(statuses),
            "Findings": random.choice(findings),
        })
    return pd.DataFrame(data)

def load_or_generate_csv(filename, generator_func):
    if os.path.exists(filename):
        try:
            df = pd.read_csv(filename)
            if not df.empty:
                return df
        except:
            pass
    df = generator_func()
    df.to_csv(filename, index=False)
    return df

def regenerate_all_data():
    generate_risks(15).to_csv(CSV_RISKS, index=False)
    generate_compliance(8).to_csv(CSV_COMPLIANCE, index=False)
    generate_audit(6).to_csv(CSV_AUDIT, index=False)
    st.cache_data.clear()

# ---------- DATA LOADING ----------
@st.cache_data
def get_risk_data():
    return load_or_generate_csv(CSV_RISKS, generate_risks)

@st.cache_data
def get_compliance_data():
    return load_or_generate_csv(CSV_COMPLIANCE, generate_compliance)

@st.cache_data
def get_audit_data():
    return load_or_generate_csv(CSV_AUDIT, generate_audit)

def get_heatmap_data(risk_df):
    categories = risk_df["Category"].unique()
    business_units = ["Finance", "Operations", "IT", "Compliance", "HR", "Legal"]
    data = {}
    for cat in categories:
        for bu in business_units:
            if cat == "IT" and bu == "IT":
                score = random.randint(4,5)
            elif cat == "Financial" and bu == "Finance":
                score = random.randint(3,5)
            else:
                score = random.randint(1,5)
            data[(cat, bu)] = score
    df = pd.DataFrame(index=categories, columns=business_units)
    for cat in categories:
        for bu in business_units:
            df.loc[cat, bu] = data.get((cat, bu), random.randint(1,5))
    return df.astype(int)

# ---------- EXPORT FUNCTIONS ----------
def export_excel(df, filename):
    try:
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        output.seek(0)
        b64 = base64.b64encode(output.read()).decode()
        return f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}.xlsx">⬇️ Download Excel</a>'
    except Exception as e:
        return f"⚠️ Excel export failed: {e}"

def export_pdf(df, title, filename):
    try:
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import landscape, A4

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=landscape(A4))
        elements = []
        styles = getSampleStyleSheet()
        elements.append(Paragraph(f"{title} Report", styles['Title']))
        elements.append(Spacer(1, 20))
        data = [df.columns.tolist()] + df.values.tolist()
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        doc.build(elements)
        buffer.seek(0)
        b64 = base64.b64encode(buffer.read()).decode()
        return f'<a href="data:application/pdf;base64,{b64}" download="{filename}.pdf">⬇️ Download PDF</a>'
    except Exception as e:
        return f"⚠️ PDF export failed: {e}"

# ---------- LOGIN ----------
def login():
    st.title("🔐 Enterprise Risk Management – Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.session_state.role = USERS[username]["role"]
                st.rerun()
            else:
                st.error("Invalid credentials")

# ---------- PAGES ----------
def page_dashboard():
    st.title("📊 Dashboard")
    risk_df = get_risk_data()
    total = len(risk_df)
    high = len(risk_df[risk_df["Risk Level"].isin(["High", "Critical"])])
    med = len(risk_df[risk_df["Risk Level"] == "Medium"])
    low = len(risk_df[risk_df["Risk Level"] == "Low"])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Risks", total)
    col2.metric("High / Critical", high)
    col3.metric("Medium", med)
    col4.metric("Low", low)

    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("Risk Heat Map")
        heat_df = get_heatmap_data(risk_df)
        fig = px.imshow(heat_df, text_auto=True, color_continuous_scale=["green", "yellow", "red"],
                        zmin=1, zmax=5, aspect="auto", title="Severity by Category & BU")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    with col_right:
        st.subheader("Risk Distribution by Category")
        cat_counts = risk_df["Category"].value_counts().reset_index()
        cat_counts.columns = ["Category", "Count"]
        fig2 = px.pie(cat_counts, values="Count", names="Category", title="Risk Categories")
        st.plotly_chart(fig2, use_container_width=True)

def page_risks():
    st.title("📋 Risk Register")
    df = get_risk_data()
    st.dataframe(df, use_container_width=True, height=400)
    if st.session_state.role in ["Admin", "Manager"]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(export_excel(df, "Risks"), unsafe_allow_html=True)
        with col2:
            st.markdown(export_pdf(df, "Risk Register", "Risks"), unsafe_allow_html=True)

def page_compliance():
    st.title("✅ Compliance Management")
    df = get_compliance_data()
    st.dataframe(df, use_container_width=True, height=400)
    if st.session_state.role in ["Admin", "Manager"]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(export_excel(df, "Compliance"), unsafe_allow_html=True)
        with col2:
            st.markdown(export_pdf(df, "Compliance Report", "Compliance"), unsafe_allow_html=True)

def page_audit():
    st.title("📄 Audit Reports")
    df = get_audit_data()
    st.dataframe(df, use_container_width=True, height=400)
    if st.session_state.role == "Admin":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(export_excel(df, "Audit"), unsafe_allow_html=True)
        with col2:
            st.markdown(export_pdf(df, "Audit Reports", "Audit"), unsafe_allow_html=True)

# ---------- MAIN ----------
def main():
    # ---------- Process flags (logout / regenerate) ----------
    if st.session_state.get("logout_clicked", False):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.session_state.role = "Viewer"
        st.session_state.logout_clicked = False
        st.rerun()
        return  # stop further execution

    if st.session_state.get("regenerate_clicked", False):
        regenerate_all_data()
        st.session_state.regenerate_clicked = False
        st.success("All data regenerated with Faker!")
        st.rerun()
        return

    # ---------- If not logged in, show login ----------
    if not st.session_state.authenticated:
        login()
        return

    # ---------- Logged in: show sidebar & content ----------
    st.sidebar.title(f"👤 {st.session_state.username} ({st.session_state.role})")

    # Logout button (sets flag, no on_click)
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logout_clicked = True
        st.rerun()   # needed to re-run and pick up the flag

    st.sidebar.markdown("---")

    # Navigation
    allowed_pages = []
    if st.session_state.role == "Admin":
        allowed_pages = ["Dashboard", "Risk List", "Compliance", "Audit Reports"]
        if st.sidebar.button("🔄 Regenerate All Data (Faker)"):
            st.session_state.regenerate_clicked = True
            st.rerun()
    elif st.session_state.role == "Manager":
        allowed_pages = ["Dashboard", "Risk List", "Compliance"]
    else:
        allowed_pages = ["Dashboard"]

    for page_name in allowed_pages:
        if st.sidebar.button(page_name):
            st.session_state.page = page_name
            st.rerun()

    # Page routing
    page = st.session_state.page
    if page == "Dashboard":
        page_dashboard()
    elif page == "Risk List":
        page_risks()
    elif page == "Compliance":
        page_compliance()
    elif page == "Audit Reports":
        page_audit()

if __name__ == "__main__":
    main()