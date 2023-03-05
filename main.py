from flask import Flask, render_template, redirect, url_for,make_response,request

import pdfkit
import jsonpickle



app = Flask(__name__)



SECRET_KEY = "this is a secret key"
app = Flask(__name__)
app.config.from_object(__name__)



@app.route("/", methods=["GET", "POST"])
def wtf():
     if request.method=="POST":
         name=request.form.get("name")
         classe = request.form.get("class")
         teacher=request.form.get("teacher")
         f=request.form.getlist('v')
         d=request.form.get("d1")

         r=request.form.get("d2")
         s=request.form.get("d3")
         s_b=request.form.get("d4")
         he=request.form.get("d5")
         he_b=request.form.get("d6")
         he_bb=request.form.get("d7")
         les=request.form.get("d8")
         has=request.form.get("d9")
         hasb=request.form.get("d10")
         behaviour=request.form.getlist("ve")
         points=request.form.getlist("point")
         home=request.form.getlist("va")
         sc=request.form.getlist("vas")
         u="../static/logo.png"
         html = render_template("index.html",messages=f,studentname=name,classe=classe,teacher=teacher,check=d,check_b=r,struggle=s,struggle_b=s_b,struggle_c=he,dif=he_b,dif_b=he_bb,dif_c=les,under=has,under_b=hasb,
                                behaviour=behaviour,points=points,home=home,sc=sc)
         options = {'enable-local-file-access': None}
         # e= pdfkit.from_file(html, "file.pdf", options=options)

         pdf = pdfkit.from_string(html, False ,css="./static/style.css",options={"enable-local-file-access": ""})
         response = make_response(pdf)
         response.headers["Content-Type"] = "application/pdf"
         response.headers["Content-Disposition"] = "inline; filename=output.pdf"
         return response

     return render_template("r.html")




# @app.route("/passed")
# def  passed():
#      return render_template("passed.html")






if __name__ == "__main__":
  app.run(debug=True)
