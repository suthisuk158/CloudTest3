from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "6006021612158 สุธิศกัดิ์ พรมอ่อน"



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
