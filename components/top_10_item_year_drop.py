from dash import html, dcc, Output, Input,Dash,callback

def render(data):
    all_years = data['Year'].unique()

    @callback(
        Output("year_drop_top_10", "value"),
        Input("select-year-button-top-10", "n_clicks")
    )
    def select_all_years_top_10(n):
        return sorted(data["Year"].unique())
    return html.Div(
        [
            html.H6("Year"),
            dcc.Dropdown(
                options = [{"label":year, "value":year} for year in all_years],
                multi=True,
                id= "year_drop_top_10"
            ),
            html.Button(
                ["Select All"],
                n_clicks=0,
                id="select-year-button-top-10"
            )
        ]
    )
    