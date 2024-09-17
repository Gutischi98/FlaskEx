from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculo', methods=['GET', 'POST'])
def calculo():
    if  request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        pintura = 9000
        sinDescuento = pintura * tarros

        descuento=None
        if edad >=18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        elif edad < 18:
            descuento = 0            

        desc = sinDescuento * descuento

        total = sinDescuento - desc

        return render_template('calculo.html', 
                           resNombre=nombre, 
                           resSinDescuento=sinDescuento, 
                           resDescuento=desc, 
                           resTotal=total)
    
    return render_template('calculo.html')




@app.route('/login')
def  login():
    return  render_template('login.html')

    


if  __name__ == '__main__':
    app.run(debug=True)
