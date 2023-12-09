from dash import html, dcc, Output, Input,Dash, callback

def render(data):
    all_categories = data['Product_Category'].unique()

    @callback(
        Output("cat_drop", "value"),      
        Input("year_drop", "value"),
        Input("select-category-button", "n_clicks")        
    )
    def select_all_categories(years,n):
        filtered_data = data.query("Year in @years")
        return sorted(filtered_data["Product_Category"].unique())
    return html.Div(
        [
            html.H6("Category"),
            dcc.Dropdown(
                options = [{"label":category, "value":category} for category in all_categories],
                multi=True,
                id= "cat_drop"
            ),
            html.Button(
                ["Select All"],
                n_clicks=0,
                id="select-category-button"
            )
        ]
    )