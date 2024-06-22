from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище задач (в памяти для простоты)
tasks = []

@app.route('/')
def index():
    return render_template('zadanie2index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task']
        if task_name:
            tasks.append(task_name)
            return redirect(url_for('index'))
    return render_template('zadanie2addtask.html')

if __name__ == '__main__':
    app.run(debug=True)
