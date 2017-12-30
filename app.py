from flask import Flask , render_template , request , redirect , url_for
import numpy as np
from boston_predict import PredictBostonData
from wtforms import Form, BooleanField,SubmitField , IntegerField, PasswordField, validators

app = Flask(__name__)


class RegistrationForm(Form):
    LSTAT = IntegerField('LSTAT')
    CRIR = IntegerField('CRIR')
    Age = IntegerField('A')
    submit = SubmitField('Submit')


@app.route('/result', methods=['GET','POST'])
def index():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        boston_data = PredictBostonData(form.LSTAT.data, form.CRIR.data, form.Age.data)
        user = boston_data.predict()
        return render_template('result.html', user=user)


    return render_template('index.html',form=form)


if __name__ == '__main__':
    app.debug=True    # デバッグモード有効化
    app.run(host='0.0.0.0')
