from dash import html, dcc, Output, Input,Dash,callback

def render(data):
    all_months = data["Month"].unique()
    options=[{"label":month, "value":month} for month in all_months]
    @callback(
        Output("month-dropdown-top-10","value"),
        Input("month_button_top_10", "n_clicks"),     
    )
    def select_all_months(n):   
        return sorted(data["Month"].unique())
    return html.Div(
        [
            html.H6("Month"),
            dcc.Dropdown(
                options=options,
                multi=True,
                id = "month-dropdown-top-10"
            ),
            html.Button(
                ["Select All"],
                id="month_button_top_10",
                n_clicks=0
            )

        ]
    )