from flask import Flask, render_template

app = Flask(__name__)

# Фиктивные данные для примера (обычно это будет из базы данных)
users = [
    {'username': 'admin', 'role': 'admin'},
    {'username': 'moderator', 'role': 'moderator'},
    {'username': 'user', 'role': 'user'}
]

# Функция для определения контента на основе роли пользователя
def get_content_by_role(role):
    if role == 'admin':
        return {
            'title': 'Добро пожаловать, Админ!',
            'content': 'У вас полный доступ ко всем функциям системы.'
        }
    elif role == 'moderator':
        return {
            'title': 'Добро пожаловать, Модератор!',
            'content': 'Вы можете редактировать записи и комментарии.'
        }
    elif role == 'user':
        return {
            'title': 'Добро пожаловать, Пользователь!',
            'content': 'Вы можете создавать записи и просматривать френдленту.'
        }
    else:
        return {
            'title': 'Добро пожаловать!',
            'content': 'У вас нет специальных прав доступа.'
        }

@app.route('/welcome/<username>')
def welcome(username):
    # Ищем пользователя по имени
    user = next((u for u in users if u['username'] == username), None)
    if user:
        content = get_content_by_role(user['role'])
        return render_template('zadanie3.html', username=username, content=content)
    else:
        return "Пользователь не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
