import pandas as pd





class RatePension:

    """Represents a rate pension income stream.
    This class calculates the annual income from a rate pension based on a monthly amount and the age at which it starts.
    """

    def __init__(self, initial_value: float, yearly_contribution: float, yearly_return: float = 0.07, payout_age: int = None, capital_gains_tax: float = 0.153):
        self.initial_value = initial_value
        self.yearly_contribution = yearly_contribution
        self.yearly_return = yearly_return
        self.payout_age = payout_age
        self.capital_gains_tax = capital_gains_tax




    def yearly_payout(self, initial_value: float, yearly_return: float, payment_years: int, capital_gains_tax: float = 0.153) -> pd.DataFrame:
        """
        Returns a DataFrame with yearly payout and remaining pension balance.
        Takes into account Danish capital gains tax (PAL-skat) on returns.
        """

        if not (10 <= payment_years <= 30):
            raise ValueError("payment_years must be between 10 and 30 (inclusive)")

        # Apply capital gains tax to get net return
        r = yearly_return * (1 - capital_gains_tax)
        n = payment_years
        P = initial_value

        # Calculate fixed annual payout
        annual_payment = P * (r * (1 + r)**n) / ((1 + r)**n - 1)

        payouts = []
        balances = []

        balance = initial_value
        for year in range(1, n + 1):
            balance = balance * (1 + r) - annual_payment
            payouts.append(annual_payment)
            balances.append(balance)

        return pd.DataFrame({
            "År": range(1, n + 1),
            "Årlig udbetaling (efter PAL-skat)": payouts,
            "Saldo efter år": balances
        }).set_index("År")

