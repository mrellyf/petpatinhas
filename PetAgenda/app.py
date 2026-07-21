from flask import Flask, render_template, request, redirect
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="petagenda",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():

    if request.method == "POST":
        tutor = request.form["tutor"]
        pet = request.form["pet"]
        servico = int(request.form["servico"])
        data = request.form["data"]
        horario = request.form["hora"]

        cursor.execute("""
            INSERT INTO agendamento
            (nome_tutor, nome_pet, data, horario, servico)
            VALUES (%s, %s, %s, %s, %s)
        """, (tutor, pet, data, horario, servico))

        conn.commit()

        return redirect("/listar")

    return render_template("cadastrar.html")

@app.route("/listar")
def listar():

    cursor.execute("""
        SELECT
            a.id,
            a.nome_tutor,
            a.nome_pet,
            s.nome_servico,
            a.data,
            a.horario
        FROM agendamento a
        INNER JOIN servicos s
            ON a.servico = s.id
        ORDER BY a.id
    """)

    agendamentos = cursor.fetchall()

    return render_template(
        "listar.html",
        agendamentos=agendamentos
    )
    #return render_template("listar.html", agendamentos=agendamentos)

@app.route("/editar/<int:id>")
def editar(id):

    cursor.execute("""
        SELECT
            id,
            nome_tutor,
            nome_pet,
            servico,
            data,
            horario
        FROM agendamento
        WHERE id = %s
    """, (id,))

    agendamento = cursor.fetchone()

    cursor.execute("SELECT * FROM servicos")
    servicos = cursor.fetchall()

    return render_template(
        "editar.html",
        agendamento=agendamento,
        servicos=servicos
    )
    

@app.route("/pets/atualizar/<int:id>", methods=["POST"])
def atualizar(id):

    tutor = request.form["tutor"]
    pet = request.form["pet"]
    servico = int(request.form["servico"])
    data = request.form["data"]
    hora = request.form["hora"]

    cursor.execute("""
        UPDATE agendamento
        SET
            nome_tutor = %s,
            nome_pet = %s,
            servico = %s,
            data = %s,
            horario = %s
        WHERE id = %s
    """, (tutor, pet, servico, data, hora, id))

    conn.commit()

    return redirect("/listar")
    

@app.route("/excluir/<int:id>")
def excluir(id):

    cursor.execute(
        "DELETE FROM agendamento WHERE id = %s",
        (id,)
    )

    conn.commit()

    return redirect("/listar")

if __name__ == "__main__":
    app.run(debug=True)