from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the model
try:
    with open('pipe.pkl', 'rb') as f:
        pipe = pickle.load(f)
except Exception as e:
    raise Exception(f"Model not loaded: {str(e)}")

teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Kolkata Knight Riders',
    'Royal Challengers Bangalore', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Bangalore', 'Hyderabad', 'Kolkata', 'Mumbai', 'Visakhapatnam',
    'Indore', 'Durban', 'Chandigarh', 'Delhi', 'Dharamsala', 'Ahmedabad',
    'Chennai', 'Ranchi', 'Nagpur', 'Mohali', 'Pune', 'Bengaluru', 'Jaipur',
    'Port Elizabeth', 'Centurion', 'Raipur', 'Sharjah', 'Cuttack',
    'Johannesburg', 'Cape Town', 'East London', 'Abu Dhabi', 'Kimberley',
    'Bloemfontein'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    if request.method == 'POST':
        try:
            batting_team = request.form['batting_team']
            bowling_team = request.form['bowling_team']
            city = request.form['city']
            target = int(request.form['target'])
            score = int(request.form['score'])
            overs = float(request.form['overs'])
            wickets = int(request.form['wickets'])

            if wickets > 10 or overs > 20:
                error = "Wickets can't exceed 10 and overs can't exceed 20."
            else:
                runs_left = target - score
                balls_left = 120 - (overs * 6)
                wickets_remaining = 10 - wickets
                crr = score / overs if overs > 0 else 0
                rrr = runs_left / (balls_left / 6) if balls_left > 0 else 0

                input_df = pd.DataFrame({
                    'batting_team': [batting_team],
                    'bowling_team': [bowling_team],
                    'city': [city],
                    'runs_left': [runs_left],
                    'balls_left': [balls_left],
                    'wickets': [wickets_remaining],
                    'total_runs_x': [target],
                    'crr': [crr],
                    'rrr': [rrr]
                })

                result = pipe.predict_proba(input_df)
                win = round(result[0][1]*100)
                loss = round(result[0][0]*100)
                prediction = {
                    'batting': batting_team,
                    'bowling': bowling_team,
                    'win': win,
                    'loss': loss
                }

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', teams=teams, cities=cities, prediction=prediction, error=error)


if __name__ == '__main__':
    app.run(debug=True)
