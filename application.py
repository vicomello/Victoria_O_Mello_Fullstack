from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcular():
    # Abrindo o arquivo em que serão salvos os resultados
    fieldnames = ['numero', 'resultado']
    try:
        f = open("data.csv", "x", newline='')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    except FileExistsError:
        f = open("data.csv", "a", newline='')
        writer = csv.DictWriter(f, fieldnames=fieldnames)

    divisores = list()
    if request.method == "GET":
        return render_template("page.html")
    elif request.method == "POST":
        # Pegando o número do digitado no formulário e calculando seus divisores
        number = request.form.get("number")
        if number.isdigit():
            x = int(number)
            if x > 0:
                for i in range(1, (x + 1)):
                    if (x / i).is_integer():
                        divisores.append(i)
                if len(divisores) == 2:
                    message = ("{} é primo".format(x))
                else:
                    message = ("A lista de divisores é {}".format(divisores))
                # Escrevendo as informações no arquivo csv
                writer.writerow({'numero': x, 'resultado': divisores})
            else:
                message = "Você deve digitar um número natural positivo!"
        else:
            message = "Você deve digitar um número natural!"

        f.close()
        return render_template("page.html", message=message)
