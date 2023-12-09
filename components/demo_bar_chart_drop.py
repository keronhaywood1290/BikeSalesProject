from dash import html, dcc, Output, Input,Dash, callback

def render(data):
    all_countries = data["Country"].unique()
    @callback(
        Output("demo_country_drop", "value"),
        Input("demo_slct_country_btn", "n_clicks")       
    )
    def select_all_countries(n):
        return all_countries
        
    dropdown = html.Div(
        [
            html.H6("Country"),
            dcc.Dropdown(
                options = [{"label":country, "value":country} for country in all_countries],
                multi=True,
                id= "demo_country_drop"
            ),
            html.Button(
                ["Select All"],
                n_clicks=0,
                id="demo_slct_country_btn"
            )
        ]
    )
    return dropdown