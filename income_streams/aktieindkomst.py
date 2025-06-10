import pandas as pd





class Aktieindkomst:
    """Represents an income stream from stock dividends.
    This class calculates the annual income from stock dividends based on a monthly amount and the age at which it starts.
    """

    def __init__(self, initial_value: float, yearly_return: float = 0.07, yearly_dividend: float = 0.02,yearly_realization: float = 0, capital_gains_tax: dict = {'0': 0.27, '1': 0.42}):
        self.initial_value = initial_value
        self.yearly_return = yearly_return 
        self.yearly_dividend = yearly_dividend
        self.yearly_realization = yearly_realization
        self.capital_gains_tax = capital_gains_tax

        self.yearly_income = self.calculate_yearly_income()



    def calculate_yearly_income(
        self,
        initial_value: float = None,
        yearly_return: float = None,
        yearly_dividend: float = None,
        yearly_realization: float = None,
        sim_years: int = 20
    ) -> pd.DataFrame:
        """Calculates the yearly income from stock dividends and capital gains realization."""

        # Fallback to self values if arguments are None
        initial_value = initial_value if initial_value is not None else self.initial_value
        yearly_return = yearly_return if yearly_return is not None else self.yearly_return
        yearly_dividend = yearly_dividend if yearly_dividend is not None else self.yearly_dividend
        yearly_realization = yearly_realization if yearly_realization is not None else self.yearly_realization

        # Containers
        start_balances = []
        end_balances = []
        dividends = []
        yearly_realizations = []
        aktieindkomst = []

        balance = initial_value
        for year in range(1, sim_years + 1):
            start_balance = balance

            # Growth
            balance *= (1 + yearly_return)

            # Dividend
            dividend = balance * yearly_dividend
            balance -= dividend

            # Realized gain
            realization = balance * yearly_realization
            balance -= realization

            end_balance = balance

            # Append data
            start_balances.append(start_balance)
            end_balances.append(end_balance)
            dividends.append(dividend)
            yearly_realizations.append(realization)
            aktieindkomst.append(dividend + realization)

        return pd.DataFrame({
            "År": range(1, sim_years + 1),
            "Startsaldo": start_balances,
            "Udbytte": dividends,
            "Realiseret gevinst": yearly_realizations,
            "Slutsaldo": end_balances,
            "Aktieindkomst": aktieindkomst
        }).set_index("År")