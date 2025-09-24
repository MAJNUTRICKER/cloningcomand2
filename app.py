from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = "meta_secret_123"
KEY_FILE = "keys.txt"

# Helper functions
def read_keys():
    keys = []
    with open(KEY_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                key, status = line.split(":")
                keys.append({"key": key, "status": status})
    return keys

def write_keys(keys):
    with open(KEY_FILE, "w") as f:
        for k in keys:
            f.write(f"{k['key']}:{k['status']}\n")

# User page
@app.route('/')
def index():
    keys = read_keys()
    return render_template('user.html', keys=keys)

# Admin page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    keys = read_keys()
    if request.method == 'POST':
        action = request.form['action']
        key_value = request.form['key']
        for k in keys:
            if k["key"] == key_value:
                if action == "approve":
                    k["status"] = "approved"
                elif action == "remove":
                    keys.remove(k)
                break
        write_keys(keys)
        flash(f"Action '{action}' performed on {key_value}", "success")
        return redirect(url_for('admin'))
    return render_template('admin.html', keys=keys)

if __name__ == '__main__':
    app.run(debug=True, port=8080)            if k["key"] == key_value:
                if action == "approve":
                    k["status"] = "approved"
                elif action == "remove":
                    keys.remove(k)
                break
        write_keys(keys)
        flash(f"Action {action} performed on {key_value}", "success")
        return redirect(url_for('admin'))
    return render_template('admin.html', keys=keys)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
