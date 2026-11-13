
from flask import (
    flash, request, session, redirect,
    url_for, render_template, Blueprint, abort
)
from dao.evento_dao import EventoDAO
from models.evento import Evento

evento_bp = Blueprint('eventos', __name__)


@evento_bp.before_request
def exigir_login():
    if 'usuario_id' not in session:
        flash("Você precisa estar logado para acessar esta página.")
        return redirect(url_for('autenticacao.login'))


@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        evento = Evento(
            nome=request.form["nome"],
            data=request.form["data"],
            local=request.form["local"],
            vagas=request.form["vagas"]
        )

        EventoDAO.salvar(evento)
        flash("Evento cadastrado com sucesso!")

        return redirect(url_for("eventos.index"))

    return render_template(
        "index.html",
        eventos=EventoDAO.listar()
    )


@evento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    evento = EventoDAO.buscar_por_id(id)

    if evento is None:
        abort(404)

    if request.method == "POST":
        EventoDAO.atualizar(
            evento,
            request.form["nome"],
            request.form["data"],
            request.form["local"],
            request.form["vagas"]
        )

        flash("Evento atualizado com sucesso!")
        return redirect(url_for("eventos.index"))

    return render_template("editar.html", evento=evento)


@evento_bp.route("/deletar/<int:id>", methods=["POST"])
def deletar(id):
    evento = EventoDAO.buscar_por_id(id)

    if evento is None:
        abort(404)

    EventoDAO.deletar(evento)
    flash("Evento excluído com sucesso!")

    return redirect(url_for("eventos.index"))
