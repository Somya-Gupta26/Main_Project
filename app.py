from flask import Flask, render_template,request
import joblib


model = joblib.load("./models/linear_model.lb")
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')
 


@app.route("/predict", methods=['GET','POST']) 
def predict():
    if request.method=="POST":
        age=int(request.form['age'])
        gender=int(request.form['gender'])
        bmi=float(request.form['bmi'])
        children=int(request.form['children'])
        smoker=int(request.form['smoker'])
        region=int(request.form['region'])
        
        
        UNSEEN_DATA = [[age,gender,bmi,children,smoker,region]]
        
        PREDICTION = model.predict(UNSEEN_DATA)[0]
        
        return render_template('home.html', prediction_text=str(round(PREDICTION, 2)))

if __name__ == "__main__":
    app.run(debug=True)