from dash import html, dcc, Output, Input,Dash,callback

def render(data):
    all_years = data['Year'].unique()
    @callback(
        Output("slider_year_sldr", "figure"),
        Input("select_year_sldr", "value")
    )
    def select_all_years_line(n):
        return all_years
    slider = html.Div(
        [   html.H6("Year"),
            dcc.RangeSlider(
                id= "select_year_sldr",
                min=data["Year"].min(),
                max= data["Year"].max(),
                step=1,
                value = [2012,2015],
                tooltip = {'placement': 'bottom','always_visible': True},
                marks = {
                    int(data["Year"].min()):{'label': str(data["Year"].min()),'style': {'color':'blue'}}                   
                },
                
            )
            
        ]
    )
    return slider