from flask import Flask, render_template, request
from screener import extract_resume_text
from ai import AI

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('index.html')

# @app.route('/summary')
# def show_summary():
    # return render_template('summary.html', summary=summary)

@app.route('/uploader', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        resume_text = extract_resume_text(f.filename)
        summary = AI(resume_text)
        # return summary
        # return 'file uploaded successfully'
        return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
