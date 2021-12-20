from flask import Flask
from flask import Flask, render_template, flash, request , session , url_for , redirect
import joblib 
from forms import InputForm
import datetime;


app = Flask(__name__)
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'


@app.route("/" , methods=['GET', 'POST'] )
def home():
    form = InputForm(request.form) 
    model = joblib.load('XGBoost')
    if request.method == 'POST':
        inp1 = form.inp1.data
        inp2 = form.inp2.data
        inp3 = form.inp3.data
        print(f"{inp1} = {inp2} =  {inp3}")
        result2 = model.predict([[inp1, inp2 , inp3]])
    print(model.predict([[-3.410692 , 0.85440 , 0.228154]]))
    return render_template("home.html"  , form=form)


@app.route("/page2" , methods=['GET', 'POST'] )
def page2():
    # ct stores current time
    ct = datetime.datetime(2018, 9, 15)
    print("current time:-", ct)
    
    # ts store timestamp of current time
    ts = ct.timestamp()
    print("++++++++++++++")
    print("timestamp:-", int(str(ts)[:5]))
    print("++++++++++++++")
    return "page2"


