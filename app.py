import os
from flask import Flask, render_template_string, request, send_file, redirect, url_for

app = Flask(__name__)

# সাধারণ একটি হোম পেজ যেখানে ব্যবহারকারী ফাইল আপলোড করতে পারবেন
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML to APK Converter</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; text-align: center; padding: 50px; }
        .container { background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        input[type="file"] { margin: 20px 0; }
        button { background: #28a745; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; }
        button:hover { background: #218838; }
    </style>
</head>
<body>
    <div class="container">
        <h2>HTML / ZIP to APK Generator</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".html,.zip" required><br>
            <button type="submit">Generate APK</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    # এখানে আপনার ফাইল প্রসেসিং বা জেনারেশনের লজিক থাকবে
    return "APK generation feature is processing!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
