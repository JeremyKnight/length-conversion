from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')


@app.route("/l1")
def render_link1(): 
   if 'towers' in request.args:
        #towers = float(request.args['towers'])
        #num_towers = towers/1063
        return render_template('link1.html', response = 20)
    #return render_template('link1.html',response="")
   
    
"""@app.route("/l2")
def render_link2():
    if 'caterpillars' in request.args:
        caterpillars = float(request.args['caterpillars'])
        num_caterpillars = caterpillars/0.393701
        return render_template('link2.html', response = str(num_caterpillars))
    else:
        return render_template('link2.html')

@app.route("/l3")
def render_link3():
     if 'intestine' in request.args:
        intestine = float(request.args['intestine'])
        num_intestine = intestine/25
        return render_template('link3.html', response = str(num_intestine))
    else:
        return render_template('link3.html')
        """

if __name__=="__main__":
    app.run(debug=False, port=54321)
