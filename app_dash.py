import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from District_Crop_Recommendation_Testing import DistrictCropRecommendation
from Soil_Crop_Recommendation_Testing import SoilCropPrediction
from Yield_Prediction_Testing import YieldPrediction

app = dash.Dash(__name__)

# Define layout for each dashboard with styling
def generate_input_row(label, id, type, value):
    return html.Div([
        html.Label(label, style={'margin-right': '10px'}),
        dcc.Input(id=id, type=type, value=value, style={'margin-right': '20px'})
    ], style={'margin-bottom': '15px'})

crop_recommendation_layout = html.Div([
    html.H2('Crop Recommendation'),
    generate_input_row('State:', 'state-input-crop', 'text', 'Tamil Nadu'),
    generate_input_row('District:', 'district-input-crop', 'text', 'COIMBATORE'),
    generate_input_row('Season:', 'season-input-crop', 'text', 'Kharif'),
    html.Button('Submit', id='submit-button-crop', n_clicks=0),
    html.Div(id='crop-recommendation-output')
])

soil_crop_prediction_layout = html.Div([
    html.H2('Soil Crop Prediction'),
    generate_input_row('Parameter 1:', 'param1-input-soil', 'number', 0),
    generate_input_row('Parameter 2:', 'param2-input-soil', 'number', 11),
    generate_input_row('Parameter 3:', 'param3-input-soil', 'number', 101),
    generate_input_row('Parameter 4:', 'param4-input-soil', 'number', 10.2),
    generate_input_row('Parameter 5:', 'param5-input-soil', 'number', 100),
    html.Button('Submit', id='submit-button-soil', n_clicks=0),
    html.Div(id='soil-crop-prediction-output')
])

yield_prediction_layout = html.Div([
    html.H2('Yield Prediction'),
    generate_input_row('State:', 'state-input-yield', 'text', 'Tamil Nadu'),
    generate_input_row('District:', 'district-input-yield', 'text', 'ERODE'),
    generate_input_row('Season:', 'season-input-yield', 'text', 'Kharif'),
    generate_input_row('Crop:', 'crop-input-yield', 'text', 'Rice'),
    generate_input_row('Parameter 1:', 'param1-input-yield', 'number', 55347),
    html.Button('Submit', id='submit-button-yield', n_clicks=0),
    html.Div(id='yield-prediction-output')
])

# Define callbacks to update outputs based on user interactions
@app.callback(Output('crop-recommendation-output', 'children'),
              [Input('submit-button-crop', 'n_clicks')],
              [dash.dependencies.State('state-input-crop', 'value'),
               dash.dependencies.State('district-input-crop', 'value'),
               dash.dependencies.State('season-input-crop', 'value')])
def update_crop_recommendation(n_clicks, state, district, season):
    if n_clicks > 0:
        crops = DistrictCropRecommendation(state, district, season)
        return html.Div([
            html.P(f"Recommended Crops: {', '.join(crops)}")
        ])

@app.callback(Output('soil-crop-prediction-output', 'children'),
              [Input('submit-button-soil', 'n_clicks')],
              [dash.dependencies.State('param1-input-soil', 'value'),
               dash.dependencies.State('param2-input-soil', 'value'),
               dash.dependencies.State('param3-input-soil', 'value'),
               dash.dependencies.State('param4-input-soil', 'value'),
               dash.dependencies.State('param5-input-soil', 'value')])
def update_soil_crop_prediction(n_clicks, param1, param2, param3, param4, param5):
    if n_clicks > 0:
        predicted_crop, city, curr_temperature, curr_humidity = SoilCropPrediction(param1, param2, param3, param4, param5)
        return html.Div([
            html.P(f"Predicted Crop: {predicted_crop}"),
            html.P(f"City: {city}"),
            html.P(f"Temperature: {curr_temperature}"),
            html.P(f"Humidity: {curr_humidity}")
        ])

@app.callback(Output('yield-prediction-output', 'children'),
              [Input('submit-button-yield', 'n_clicks')],
              [dash.dependencies.State('state-input-yield', 'value'),
               dash.dependencies.State('district-input-yield', 'value'),
               dash.dependencies.State('season-input-yield', 'value'),
               dash.dependencies.State('crop-input-yield', 'value'),
               dash.dependencies.State('param1-input-yield', 'value')])
def update_yield_prediction(n_clicks, state, district, season, crop, param1):
    if n_clicks > 0:
        predicted_yield = YieldPrediction(state, district, season, crop, param1)
        return html.Div([
            html.P(f"Predicted Yield: {predicted_yield}")
        ])

# Create the app layout
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Crop Recommendation', children=[crop_recommendation_layout]),
        dcc.Tab(label='Soil Crop Prediction', children=[soil_crop_prediction_layout]),
        dcc.Tab(label='Yield Prediction', children=[yield_prediction_layout]),
    ]),
], style={'max-width': '800px', 'margin': '50px auto'})

if __name__ == '__main__':
    app.run_server()
