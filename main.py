from flask import Flask, send_from_directory, request, render_template
import requests
import os

app = Flask(__name__)
temp_folder = 'temp'

# temp 폴더가 없으면 생성
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download-logo', methods=['GET', 'POST'])
def download_logo():
    if request.method == 'POST':
        # 구글 로고 이미지 URL
        image_url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
        response = requests.get(image_url)

        # 이미지 저장
        filename = os.path.join(temp_folder, '171202김재형.png')
        with open(filename, 'wb') as f:
            f.write(response.content)

        return render_template('download.html', message="다운로드가 완료되었습니다. 파일을 보시겠습니까?")
    else:
        return render_template('download.html', message="구글 로고를 다운로드 하시겠습니까?")

@app.route('/temp/<filename>')
def download_file(filename):
    return send_from_directory(directory=temp_folder, path=filename)

if __name__ == '__main__':
    app.run(debug=True)
