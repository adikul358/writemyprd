import os
from time import sleep
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from openai_funcs import get_prd, get_assistant
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

class PRDForm(Form):
    product_name = StringField('Product Name')
    feature_name = StringField('Feature Name')
    overview = TextAreaField('Give an Overview / Explanation')
    feature_list = TextAreaField('Feature List')
    user_feedback = TextAreaField('User Feedback')

@app.route('/', methods=["GET", "POST"])
def index():
    error = ""
    prd = ""
    form = PRDForm(request.form)

    if request.method == "POST":
        a1 = form.product_name.data
        a2 = form.feature_name.data
        a3 = form.overview.data
        b1 = form.feature_list.data
        b2 = form.user_feedback.data

        query = f"Write a PRD for a product named {a1} that {a3} with features including {a2}, {b1}{', for which the users have given feedback of' + b2 if b2 != '' else ''}"
        prd = get_prd(query)

    return render_template('index.html', form=form, message=error, prd=prd)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))