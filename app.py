from flask import Flask, render_template, request, jsonify
from grammar_model.model import GrammarCorrector

app = Flask(__name__)

# Initialize the grammar corrector model
grammar_corrector = GrammarCorrector()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/correct', methods=['POST'])
def correct_text():
    text = request.form['text']

    # Correct grammar using the model
    corrected_text = grammar_corrector.correct_grammar(text)

    # Send corrected text as JSON response
    return jsonify({'corrected_text': corrected_text})


if __name__ == '__main__':
    app.run(debug=True)
