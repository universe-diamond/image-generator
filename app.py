from boltiotai import openai
import os
from flask import Flask, render_template, request

openai.api_key = 'oia3k94smQk1LiU_DZjRppHvKv827tJ05o2yXMOpROg' #os.environ['OPENAI_API_KEY']

def generate_tutorial(components):
  response = openai.Images.create(
      prompt=components,
      model="dall-e-3",
      size="1024x1024",
      response_format="url")
  image_url = response['data'][0]['url']
  return image_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
  output = ""

  if request.method == 'POST':
    components = request.form['components']
    output = generate_tutorial(components)

  return render_template('index.html',output=output)

@app.route('/generate', methods=['POST'])
def generate():
 components = request.form['components']
 return generate_tutorial(components)

if __name__ == '__main__':            
 app.run(host='0.0.0.0', port=8080)