from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/search')
def my_form():
    return render_template('WebPage1.html')

@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()
    return """
        <html>
            <body>
            </body>
        </html>
        """, 401