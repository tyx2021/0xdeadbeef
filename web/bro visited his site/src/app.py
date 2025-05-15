from flask import Flask, request, render_template, redirect, session, render_template_string
import keyword, random 
import os

app = Flask(__name__)
app.secret_key = keyword.kwlist[random.randint(1,len(keyword.kwlist))]  # hm??
app.config["FLAG"] = "deadbeef{br0_k33p5_s3cr3t5_1n_c0nf1g}"

@app.route('/', methods=['GET', 'POST'])
def bro_visiting():
    message = 'bro visited his site'
    
    if 'user' not in session:
      session['user']='guest'
    
    if session.get('user') == 'Bro':
      return redirect('/bro_visited')

    return render_template('bro_visiting.html', message=message)
  
@app.route('/bro_visited', methods=['GET', 'POST'])
def bro_visited():
    if 'user' not in session:
      session['user']='guest'
    
    if session.get('user') != 'Bro':
      return redirect('/')

    return render_template('bro_visited.html', message='deadbeef{Br0_fr_v1s1t3D_h1s_h0uS3}')

@app.route("/vibe-check")
def vibe_check():
    vibe = request.args.get("vibe", "")

    return render_template_string(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Vibe Check</title>
            <link rel="stylesheet" href="{{{{ url_for('static', filename='style.css') }}}}">
        </head>
        <body>
            <div class="container">
                <h1>You are a:</h1>
                <p>{vibe}pilled {vibe}maxxer</p>
                <img src="{{{{ url_for('static', filename='bro.jpeg') }}}}" alt="bro image" style="max-width: 100%; border-radius: 12px; margin-top: 20px;">
                <p><a href="/">Go back</a></p>
            </div>
        </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3126',debug=True)
