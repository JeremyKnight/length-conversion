from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')


@app.route("/l1")
def render_link1():
    #length = request.args['length'] 
     
    #return render_template('link1.html', response = response)
    return render_template('link1.html')

@app.route("/l2")
def render_link2():
    #length = request.args['length']
    
    #return render_template('link2.html', response = response)
    return render_template('link2.html')

@app.route("/l3")
def render_link3():
    #length = request.args['length']
    
    #return render_template('link3.html', response = response)
    return render_template('link3.html')

@app.route("/response")
def render_response():
    length = request.args['length']
    response= "works!"
    return render_template('response.html'), response = response)
    #The request object stores information about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have multiple values for the same key)
    #The information in args is visible in the url for the page being requested (ex. .../response?color=blue)
    
    """if length == 'something':
        response = "That's my favorite color, too!"
    else:
        response = "My favorite color is pink."
    return render_template('response.html', response = response)"""
    
    #if length comes from this link 1 then do the following code for it
    #return render_template('resonse.html', response =
    #else if length comes from link2 then do the following:
    #else if length comes from link3 the do the following
    #else go to main page    

if __name__=="__main__":
    app.run(debug=False, port=54321)

    
    
