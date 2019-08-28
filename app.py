# coding: UTF-8
from flask import Flask,render_template,request,redirect,url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from src.entity.user import User
from src.loginService import LoginService
from src.managementService import ManagementService
from src.attendanceService import AttendanceService

app = Flask(__name__)

app.secret_key = "secret_key_am"
app.config.update({'DEBUG': True })
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"
loginService = LoginService()
managementService = ManagementService()
attendanceService = AttendanceService()

@login_manager.user_loader
def load_user(user_id):
    return loginService.searchUser(user_id)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginAction", methods=['GET', 'POST'])
def loginAction():
    username = request.form["username"]
    password = request.form["password"]
    user = User(username,password)
    login_user(user)
    return redirect(request.args.get("next") or url_for("index"))

@app.route("/index")
@login_required
def index():
    values = managementService.searchItemList()
    # index.html をレンダリングする
    return render_template("index.html", values=values)


@app.route("/attendance")
def attendance():
    '''
    カードリーダーからの受信
    '''
    cardId = request.form["id"]
    return attendanceService.existIdAndAttendance(cardId)

if __name__ == "__main__":
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0', port=5000)
