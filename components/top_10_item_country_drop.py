from dash import html, dcc, Output, Input,Dash, callback

def render(data):
    all_countries = data['Country'].unique()
    options = [{"label":ctry, "value":ctry} for ctry in all_countries]
    @callback(
        Output("top_10_country_drop", "value"),
        Input("year_drop_top_10", "value"),
        Input("month-dropdown-top-10","value"),
        Input("top_10_select_country_drop", "n_clicks")       
    )
    def select_all_categories(years, month,n):
        filtered_data = data.query("Year in @years and Month in @month")
        return sorted(filtered_data["Country"].unique())
    return html.Div(
        [
            html.H6("Country"),
            dcc.Dropdown(
                options = options,
                multi=True,
                id= "top_10_country_drop"
            ),
            html.Button(
                ["Select All"],
                n_clicks=0,
                id="top_10_select_country_drop"
            )
        ]
    )