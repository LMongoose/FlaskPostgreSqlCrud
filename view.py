import os
from flask import request, redirect, url_for, render_template
import model


def setDefaultRoutes(app, appname):
    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html", appname=appname)

    @app.route("/animes")
    def animes():
        tablename = "Animes"
        results, columns = model.list_all(tablename)
        return render_template("view.html", appname=appname, tablename=tablename, numcols=len(columns), columns=columns, results=results)

    @app.route("/characters")
    def characters():
        tablename = "Characters"
        results, columns = model.list_all(tablename)
        return render_template("view.html", appname=appname, tablename=tablename, numcols=len(columns), columns=columns, results=results)

    @app.route("/people")
    def people():
        tablename = "People"
        results, columns = model.list_all(tablename)
        return render_template("view.html", appname=appname, tablename=tablename, numcols=len(columns), columns=columns, results=results)

    @app.route("/users")
    def users():
        tablename = "Users"
        results, columns = model.list_all(tablename)
        return render_template("view.html", appname=appname, tablename=tablename, numcols=len(columns), columns=columns, results=results)

    @app.route("/animeography")
    def animeography():
        tablename = "Animeography"
        results, columns = model.list_all(tablename)
        return render_template("view.html", appname=appname, tablename=tablename, numcols=len(columns), columns=columns, results=results)

    @app.route("/staff")
    def staff():
        tablename = "Staff"
        results, columns = model.list_all(tablename)
        return render_template("view.html", appname=appname, tablename=tablename, numcols=len(columns), columns=columns, results=results)

    @app.route("/create", methods=["POST"])
    def create():
        tablename = request.cookies.get("table_name")
        if(not model.insert(tablename, request.form)):
            return "Error executing query on database."

        else:
            if(tablename == "Animes"):
                return redirect(url_for("animes"))

            elif(tablename == "Characters"):
                return redirect(url_for("characters"))

            elif(tablename == "People"):
                return redirect(url_for("people"))

            elif(tablename == "Users"):
                return redirect(url_for("users"))

            elif(tablename == "Animeography"):
                return redirect(url_for("animeography"))

            elif(tablename == "Staff"):
                return redirect(url_for("staff"))

            else:
                return "Selected table does not exists."

    @app.route("/edit")
    def edit():
        tablename = request.cookies.get("table_name")
        selected_id = request.cookies.get("selected_id")
        selected_id2 = request.cookies.get("selected_id2")
        result, columns = model.select(tablename, selected_id, selected_id2)

        if(result is None and columns is None):
            return "Selected entry does not exists."

        else:
            return render_template("edit.html", appname=appname, tablename=tablename, numcols=len(columns), columns=columns, result=result)

    @app.route("/update", methods=["POST"])
    def update():
        tablename = request.cookies.get("table_name")
        selected_id = request.cookies.get("selected_id")
        selected_id2 = request.cookies.get("selected_id2")
        if(not model.update(tablename, selected_id, selected_id2, request.form)):
            return "Error executing query on database."

        else:
            if(tablename == "Animes"):
                return redirect(url_for("animes"))

            elif(tablename == "Characters"):
                return redirect(url_for("characters"))

            elif(tablename == "People"):
                return redirect(url_for("people"))

            elif(tablename == "Users"):
                return redirect(url_for("users"))

            elif(tablename == "Animeography"):
                return redirect(url_for("animeography"))

            elif(tablename == "Staff"):
                return redirect(url_for("staff"))

            else:
                return "Selected table does not exists."

    @app.route("/delete", methods=["POST"])
    def delete():
        tablename = request.cookies.get("table_name")
        selected_id = request.cookies.get("selected_id")
        selected_id2 = request.cookies.get("selected_id2")
        if(not model.delete(tablename, selected_id, selected_id2)):
            return "Error executing query on database."

        else:
            if(tablename == "Animes"):
                return redirect(url_for("animes"))

            elif(tablename == "Characters"):
                return redirect(url_for("characters"))

            elif(tablename == "People"):
                return redirect(url_for("people"))

            elif(tablename == "Users"):
                return redirect(url_for("users"))

            elif(tablename == "Animeography"):
                return redirect(url_for("animeography"))

            elif(tablename == "Staff"):
                return redirect(url_for("staff"))

            else:
                return "Selected table does not exists."

def setErrorRoutes(app, appname):
    @app.errorhandler(401)
    def access_unauthorized(error):
        return render_template("401.html", appname=appname), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html", appname=appname), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return render_template("405.html", appname=appname), 405