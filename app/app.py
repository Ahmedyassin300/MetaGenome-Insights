from flask import Flask, render_template
import pandas as pd
from skbio import title
from statsmodels.graphics.tukeyplot import results

app = Flask(__name__)

@app.route('/')
def index():
    results = pd.read_csv('../results/blast_output.txt')
    return render_template('index.html', tables=[results.to_html(classes='data')], titles=results.columns.values)

if __name__ == '__main__':
    app.run(debug=True)