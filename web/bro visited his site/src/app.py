from flask import Flask, request, render_template, redirect, session
import keyword, random 
import os

app = Flask(__name__)
app.secret_key = keyword.kwlist[random.randint(1,len(keyword.kwlist))]  # hm??

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3126',debug=True)
