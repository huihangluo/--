from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("Main.html")

@app.route("/PRODUCT")
def PDRODUCT():
    return render_template("/Product/product_main.html")

@app.route("/PRODUCT/Relion 615 series")
def PRODUCT__Relion_615_series():
    return render_template("/PRODUCT/product_615.html")

@app.route("/PRODUCT/Relion 615 series/REC 615")
def PRODUCT__Relion_615_series__REC615():
    return render_template("/PRODUCT/product_615_REC615.html")


if __name__=="__main__":
    app.run()
