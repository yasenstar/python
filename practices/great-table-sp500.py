from great_tables import GT
from great_tables.data import sp500

# Define the start and end dates for the data range
start_date = "2010-06-07"
end_date = "2010-06-14"

# Filter sp500 using Pandas to dates between `start_date` and `end_date`
sp500_mini = sp500[(sp500["date"] >= start_date) & (sp500["date"] <= end_date)]

# Create a display table based on the `sp500_mini` table data
(
    GT(sp500_mini)
    .tab_header(title="S&P 500", subtitle=f"{start_date} to {end_date}")
    .fmt_currency(columns=["open", "high", "low", "close"])
    .fmt_date(columns="date", date_style="wd_m_day_year")
    .fmt_number(columns="volume", compact=True)
    .cols_hide(columns="adj_close")
)