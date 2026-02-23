from flask import Flask,render_template,request
from password_checker import check_password
from port_scanner import scan_ports

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():

    strength=None
    entropy=None
    score=None
    crack=None
    color=None

    ports=None
    ip=None

    if request.method=="POST":

        if "password" in request.form:
            strength,entropy,score,crack,color=\
            check_password(request.form["password"])

        if "target" in request.form:
            ip,ports=scan_ports(
                request.form["target"]
            )

    return render_template(
        "index.html",
        strength=strength,
        entropy=entropy,
        score=score,
        crack=crack,
        color=color,
        ports=ports,
        ip=ip
    )

if __name__=="__main__":
    app.run(debug=True)
