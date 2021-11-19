"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields.html5 import DateField
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length
import requests

class StockForm(FlaskForm):
    
    
    """Generate Your Graph."""
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    API_KEY = "NDN2S8ZUZVMFC79X"
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey='+API_KEY
    r = requests.get(url)
    symbols = r.json()
    

    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
        choices=[
            (symbols),
        ],
    )
                         

    chart_type = SelectField("Select Chart Type",[DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),
        ],
    )

    time_series = SelectField("Select Time Series",[DataRequired()],
        choices=[
            ("1", "1. Intraday"),
            ("2", "2. Daily"),
            ("3", "3. Weekly"),
            ("4", "4. Monthly"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")



