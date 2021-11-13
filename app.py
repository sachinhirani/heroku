from flask import Flask, render_template, request
import joblib

app_flask = Flask(__name__)

loaded_model = joblib.load('dib_78.pkl')

@app_flask.route('/homepage') #decorator 
def homepage(): 
    return render_template('homepage.html') 
    
@app_flask.route('/predict', methods =['Post']) #decorator 
def predict(): 
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    
    prediction = loaded_model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    
    if prediction[0]==1:
        val = 'Dibatic'
    else:
        val = 'Not Dibatic'
    
    return render_template ('result.html', value=val)
if __name__=='__main__':
    app_flask.run(debug=True)