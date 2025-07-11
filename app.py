from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import json


app = Flask(__name__)
app.secret_key = 'shhhh_this_is_secret!'  # ✅ This line is required!

def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save users to a file
def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)

users = load_users()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']

        if username in users:
            flash('Username already exists.', 'error')
        elif password != confirm:
            flash('Passwords do not match.', 'error')
        else:
            users[username] = password
            save_users(users)
            flash('Account created! You can now log in.')
            return redirect(url_for('login'))
        
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/hot-properties')
def hot_properties():
    liked = session.get('liked_properties', [])
    return render_template('hot-properties.html', liked=liked)


@app.route('/top-agents')
def top_agents():
    return render_template('top-agents.html')

@app.route('/contact-agent', methods=['GET', 'POST'])
def contact_agent():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        agent = request.form['agent']
        # Here you'd usually send an email or store in a database
        flash(f'Message sent to {agent}!', 'success')
        return redirect(url_for('contact_agent'))
    return render_template('contact-agent.html', show_modal=session.pop('show_modal', False))


@app.route('/like-property/<property_id>')
def like_property(property_id):
    if 'user' not in session:
        flash("Please log in to like properties.", "error")
        return redirect(url_for('login'))
    
    liked = session.get('liked_properties', [])
    if property_id not in liked:
        liked.append(property_id)
        session['liked_properties'] = liked
        flash("Property liked!", "success")
    else:
        flash("You already liked this property.", "info")
    
    return redirect(url_for('hot_properties'))

@app.route('/my-likes')
def my_likes():
    if 'user' not in session:
        flash("Please log in to view liked properties.", "error")
        return redirect(url_for('login'))

    liked_ids = session.get('liked_properties', [])
    all_properties = {
        'house1': {
            'title': 'Beautiful Family Home',
            'desc': '4 bedrooms, big yard.',
            'img': 'house1.jpg'
        },
        'house2': {
            'title': 'Modern Apartment',
            'desc': 'City center location.',
            'img': 'house2.jpg'
        },
        'house3': {
            'title': 'Charming Cottage',
            'desc': 'Cozy and peaceful.',
            'img': 'house3.jpg'
        }
    }

    liked = {pid: all_properties[pid] for pid in liked_ids if pid in all_properties}
    return render_template('my-likes.html', liked=liked)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))