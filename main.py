from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':

    @app.route('/')
    @app.route('/home')
    def index():
        return "Главная страница"


    @app.route('/about')
    def about():
        return "About page"


    @app.route('/user')
    def user():
        return "User page"


    @app.route('/user/<string:name>/<int:id>')
    def user_id(name, id):
        return "user_id page: " + name + ' - ' + str(id)


    app.run()
