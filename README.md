# 🏏 IPL Win Predictor 🔮

**Real-time IPL match predictor built with Flask and Machine Learning**

This web application predicts the winning probability of IPL teams based on real-time match data like score, overs, wickets, and target. Built using a trained ML model and wrapped with a sleek and simple Flask frontend.

---

## 🔗 Live Demo

👉 [Click here to try the app](https://ipl-match-win-probability-predictor.onrender.com)  

---

## 🚀 Features

- 🧠 Predicts win probability between two IPL teams
- 📊 Uses current score, target, overs, and wickets
- ⚙️ Machine learning model trained on past IPL data
- 💡 Smart input validations (e.g., overs ≤ 20, wickets ≤ 10)
- 💻 Simple Flask-based web interface

---

## 🛠 Tech Stack

- **Frontend**: HTML + CSS via Jinja2 (Flask templates)
- **Backend**: Python, Flask
- **ML/DS Libraries**: Pandas, scikit-learn
- **Model File**: `pipe.pkl` (loaded with `pickle`)

---

## 📁 Project Structure

```
ipl-win-predictor/
├── app.py                 # Main Flask app
├── pipe.pkl               # Trained machine learning pipeline
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   └── background.jpg     # Optional background image
├── requirements.txt       # List of dependencies
└── README.md              # This file
```

---

## 🧠 How It Works

The app takes the following inputs from the user:

- Batting team
- Bowling team
- Match city
- Target score
- Current score
- Overs completed
- Wickets lost

Then, it calculates:

- `runs_left = target - score`
- `balls_left = 120 - (overs * 6)`
- `wickets_remaining = 10 - wickets`
- `crr = score / overs`
- `rrr = runs_left / (balls_left / 6)`

These values are fed into a machine learning pipeline, which outputs the probabilities of win/loss for the batting team.

---

## ▶️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/CARLOX62/IPL-Match-Win-Predictor

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

# 5. Visit in browser
Navigate to https://ipl-match-win-probability-predictor.onrender.com
```

---

## 📸 Screenshots

| Input Form | Prediction Result |
|------------|-------------------|
| ![Input](./static/input.png) | ![Output](./static/output.png) |


---

## 🙋‍♂️ Author

**Aniket Kumar**  
[GitHub](https://github.com/CARLOX62) • [LinkedIn](https://www.linkedin.com/in/aniket-kumar-86b2221ba/)

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

---

## ⭐ Show Some Love

If you liked the project, please consider giving it a ⭐ on GitHub.  
It inspires me to keep building and sharing more! 😄
