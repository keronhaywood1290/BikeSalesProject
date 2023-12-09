from dash import html, dcc, Output, Input,Dash,callback

def render(data):
    subCat = data["Sub_Category"].unique()
    options = [{"label":cat, "value":cat} for cat in subCat]
    @callback(
        Output("subcat_drop","value"),
        Input("cat_drop","value"),
        Input("subCat_button", "n_clicks")       
    )
    def select_subcats(cat,n):
        filtered_data = data.query("Product_Category in @cat")
        return sorted(filtered_data["Sub_Category"].unique())
    return html.Div(
        [
            html.H6("Sub Category"),
            dcc.Dropdown(
                options=[{"label":category, "value":category} for category in subCat],
                multi=True,
                id = "subcat_drop"
            ),
            html.Button(
                ["Select All"],
                id="subCat_button",
                n_clicks=0
            )

        ]
    )