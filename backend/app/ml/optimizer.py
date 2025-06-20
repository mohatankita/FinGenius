import yfinance as yf
import numpy as np
import pandas as pd
from scipy.optimize import minimize

def fetch_data(assets, start, end):
    data = yf.download(assets, start=start, end=end, auto_adjust=False)
    # Handle both multi-asset and single-asset cases
    if isinstance(data.columns, pd.MultiIndex):
        if 'Adj Close' in data.columns.levels[0]:
            adj_close = data['Adj Close']
        else:
            raise ValueError("Missing 'Adj Close' in multi-asset data.")
    elif 'Adj Close' in data.columns:
        adj_close = data['Adj Close']
    else:
        raise ValueError("'Adj Close' not found in downloaded data.")

    return adj_close.dropna()

def portfolio_performance(weights, mean_returns, cov_matrix):
    """
    Calculate expected return and risk (standard deviation) for a portfolio.
    """
    returns = np.dot(weights, mean_returns)
    risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, risk

def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
    """
    Calculate the negative Sharpe ratio for minimization.
    Handles division by zero by returning a large positive number.
    """
    p_return, p_risk = portfolio_performance(weights, mean_returns, cov_matrix)
    if p_risk == 0:
        return 1e6  # Large penalty for zero risk (degenerate case)
    return -(p_return - risk_free_rate) / p_risk

def optimize_portfolio(assets, start_date, end_date):
    """
    Optimize portfolio weights to maximize Sharpe ratio.
    Returns a dict with optimized weights, expected return, and risk.
    Handles errors and edge cases gracefully.
    """
    try:
        data = fetch_data(assets, start_date, end_date)
        returns = data.pct_change().dropna()
        if returns.empty:
            raise ValueError("Not enough data to calculate returns.")
        mean_returns = returns.mean()
        cov_matrix = returns.cov()

        num_assets = len(assets)
        initial_weights = num_assets * [1. / num_assets]
        bounds = tuple((0, 1) for _ in range(num_assets))
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

        result = minimize(
            negative_sharpe_ratio,
            initial_weights,
            args=(mean_returns, cov_matrix),
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )

        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")

        opt_weights = result.x
        exp_return, risk = portfolio_performance(opt_weights, mean_returns, cov_matrix)

        return {
            "optimized_weights": dict(zip(assets, np.round(opt_weights, 4))),
            "expected_return": round(exp_return, 4),
            "risk": round(risk, 4)
        }
    except Exception as e:
        return {"error": str(e)}
