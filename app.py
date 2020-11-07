from flask import Flask, render_template, request

from inference import get_disease_name

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods = ['POST'])
def result():
	file = request.files['file']
	print(request.files)
	image = file.read()
	disease, remidies = get_disease_name(image_bytes=image)
	ind = disease.find('__')
	plant_name = disease[:ind]
	print(plant_name)
	disease_name = disease[ind+2:]
	remidy = remidies['remidy']
	cite = remidies['cite']

	return render_template('result.html',plant= plant_name, disease = disease_name, cite=cite, remidy= remidy)



if __name__ == '__main__':
    app.run()