from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# 여러 JSON 파일을 통합하여 데이터 로드
def load_combined_data(folder_path):
    combined_data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                combined_data.append(json_data)
    return combined_data

# 예제 JSON 파일이 있는 폴더 경로
json_folder_path = "C:/Users/way17/Desktop/gcloud"

@app.route('/')
def display_combined_data():
    combined_data = load_combined_data(json_folder_path)
    return render_template('txt.html', data=enumerate(combined_data, start=1))

if __name__ == '__main__':
    app.run(debug=True)
