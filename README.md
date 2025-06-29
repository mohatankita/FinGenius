# 🧠 FinGenius: AI-Powered Investment Portfolio Manager

**FinGenius** is a full-stack web application that empowers users to optimize and manage investment portfolios using AI and data science. It leverages machine learning techniques and financial analytics to provide intelligent asset allocation, risk analysis, and performance visualization through an interactive and modern UI.

---

## 🎯 Key Features

### 🔄 Portfolio Optimization (AI-Powered)

- Accepts a list of assets and date range
- Uses machine learning to compute the optimal portfolio weights
- Calculates expected return and risk (volatility)
- Implements Mean-Variance Optimization (Efficient Frontier)

### 📈 Performance Visualization

- Compare performance of selected assets over time
- View portfolio returns and volatility visually
- Time-series charts and dynamic interaction

### 🔥 Risk Heatmap (Coming Soon)

- Correlation matrix of assets visualized as a heatmap
- Visual aid to identify diversification and clustering

### 📊 Interactive Charts

- Pie chart of optimized portfolio weights
- Line charts and heatmaps built with D3.js
- Material UI components for polished UX

---

## 🧠 AI & Machine Learning Stack

- 📈 **Portfolio Optimization** using Markowitz Theory
- 📉 **Covariance Matrix** for risk modeling
- 🔍 Future: LSTM or predictive analytics for trend prediction

---

## 🧰 Tech Stack

### Frontend

- ⚛️ React + TypeScript
- 🎨 Material UI (MUI)
- 📊 D3.js for custom visualizations
- 🌐 Axios for API requests

### Backend

- 🐍 Python with Flask (REST API)
- 📉 Pandas + NumPy for financial math
- 📚 Scikit-learn, SciPy for optimization
- 💹 yfinance to fetch historical asset data

### Tooling

- ⚡ Vite for React app
- 💻 Cursor IDE or VSCode
- ✅ Git + GitHub for version control

---

## 🚀 Roadmap

| Feature                    | Status     |
| -------------------------- | ---------- |
| Portfolio Optimizer API    | ⏳ Planned |
| D3 Pie Chart Integration   | ⏳ Planned |
| React Form + Material UI   | ⏳ Planned |
| Performance Line Chart     | ⏳ Planned |
| Risk Heatmap Visualization | ⏳ Planned |
| User Authentication (JWT)  | ⏳ Planned |
| Predictive Models (LSTM)   | ⏳ Planned |
| Portfolio Rebalancing AI   | ⏳ Planned |

---

## 📂 Project Structure

---

## 🧪 Getting Started

### 🐍 Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
python app/main.py
```

### 🐍 Frontend (React)

cd frontend
npm install
npm run dev
