def sharpe_ratio(portfolio_return, risk_free_rate, portfolio_std):
    return (portfolio_return - risk_free_rate) / portfolio_std
