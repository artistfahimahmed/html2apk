<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML2APK - সহজে আপনার ওয়েবসাইটকে অ্যান্ড্রয়েড অ্যাপে রূপান্তর করুন</title>
    <style>
        :root {
            --primary: #4f46e5;
            --primary-hover: #4338ca;
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #22c55e;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .converter-card {
            background-color: var(--card-bg);
            width: 100%;
            max-width: 550px;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .logo-area h1 {
            font-size: 28px;
            margin-bottom: 8px;
            color: #ffffff;
            letter-spacing: 0.5px;
        }
        .logo-area h1 span { color: var(--primary); }
        .logo-area p {
            color: var(--text-muted);
            font-size: 15px;
            margin-bottom: 30px;
        }
        .upload-box {
            border: 2px dashed rgba(148, 163, 184, 0.3);
            border-radius: 12px;
            padding: 30px 20px;
            background: rgba(15, 23, 42, 0.4);
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 25px;
            position: relative;
        }
        .upload-box:hover {
            border-color: var(--primary);
            background: rgba(79, 70, 229, 0.05);
        }
        .upload-box input[type="file"] {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            opacity: 0;
            cursor: pointer;
        }
        .upload-icon {
            font-size: 40px;
            color: var(--primary);
            margin-bottom: 10px;
        }
        .upload-text {
            font-size: 16px;
            color: var(--text-color);
            font-weight: 500;
        }
        .upload-hint {
            font-size: 13px;
            color: var(--text-muted);
            margin-top: 5px;
        }
        .btn-submit {
            background-color: var(--primary);
            color: white;
            border: none;
            width: 100%;
            padding: 14px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s ease;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
        }
        .btn-submit:hover {
            background-color: var(--primary-hover);
        }
        .features {
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            font-size: 13px;
            color: var(--text-muted);
        }
        .feature-item { display: flex; align-items: center; gap: 6px; }
        .feature-item span { color: var(--accent); font-weight: bold; }
    </style>
</head>
<body>

    <div class="converter-card">
        <div class="logo-area">
            <h1>HTML<span>2</span>APK</h1>
            <p>আপনার এইচটিএমএল ফাইল বা গেমটিকে পলকে রূপান্তর করুন অ্যান্ড্রয়েড অ্যাপে!</p>
        </div>

        <form action="/convert" method="POST" enctype="multipart/form-data">
            <div class="upload-box">
                <div class="upload-icon">📁</div>
                <div class="upload-text" id="file-label">আপনার `.html` বা `.zip` ফাইল এখানে ড্রপ করুন অথবা ব্রাউজ করুন</div>
                <div class="upload-hint">সর্বোচ্চ ফাইলের আকার ৫০ মেগাবাইট</div>
                <input type="file" name="html_file" id="html_file" accept=".html,.zip" required onchange="updateFileName(this)">
            </div>

            <button type="submit" class="btn-submit">🚀 মুহূর্তেই APK তৈরি করুন</button>
        </form>

        <div class="features">
            <div class="feature-item"><span>✔</span> ১০০% নিরাপদ</div>
            <div class="feature-item"><span>✔</span> কোনো কোডিং ছাড়াই</div>
            <div class="feature-item"><span>✔</span> সরাসরি ডাউনলোড</div>
        </div>
    </div>

    <script>
        function updateFileName(input) {
            const label = document.getElementById('file-label');
            if (input.files && input.files[0]) {
                label.textContent = "সিলেক্ট করা হয়েছে: " + input.files[0].name;
            }
        }
    </script>
</body>
</html>
