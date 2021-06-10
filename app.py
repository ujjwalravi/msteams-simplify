from flask import Flask, send_file, render_template, request
import csvSimplify
import os
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv']

@app.route('/')
def hello():
    return render_template('upload.html')

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['aFile']
        f.save(f.filename)
        endtime = request.form.get("endtime")
        ext = f.filename
        if ext != '':
            file_ext = os.path.splitext(ext)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                return render_template('wrongfile.html')
        nameConverted = csvSimplify.simplifyCSV(f.filename, endtime)
        return render_template('success.html', name=[f.filename, nameConverted])

@app.route('/download/<var>', methods=['GET', 'POST'])
def download_file(var):
    return send_file(var, as_attachment=True)

if __name__ == '__main__':
    app.run(debug= True)