# coding: UTF-8
from flask import Flask,render_template,request,redirect,url_for,session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin,current_user
from src.entity.user import User
from src.loginService import LoginService
from src.managementService import ManagementService
from src.attendanceService import AttendanceService
from src.signUpService import SignUpService

app = Flask(__name__)

app.secret_key = "secret_key_am"
app.config.update({'DEBUG': True })
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"
loginService = LoginService()
managementService = ManagementService()
attendanceService = AttendanceService()
signUpService = SignUpService()

@app.errorhandler(401)
@app.errorhandler(500)
def error_handller(error):
    return render_template('login.html', errormessage=str(error.code) + " " + error.name), error.code

@login_manager.user_loader
def load_user(user_id):
    return loginService.searchUser(user_id)

@app.route("/login")
def login():
    if 'errormessage' in session:
        errormessage = session["errormessage"]
        session.pop("errormessage", None)
        return render_template("login.html", errormessage=errormessage)
    return render_template("login.html")

@app.route("/loginAction", methods=['GET', 'POST'])
def loginAction():
    username = request.form["username"]
    password = request.form["password"]
    user = loginService.loginUser(username,password)
    if user is not None:
        login_user(user)
        return redirect(request.args.get("next") or url_for("index"))
    else:
        session["errormessage"] = "ユーザーが存在しませんでした。"
        return redirect("/login")

@app.route("/index")
@login_required
def index():
    values = managementService.searchItemList(current_user.user_no)
    # values = managementService.searchItemList2(current_user)
    # index.html をレンダリングする
    return render_template("index.html", values=values, user=current_user)

@app.route("/createAction", methods=['GET', 'POST'])
def createAction():
    # sign_up.html をレンダリングする
    return render_template("sign_up.html")

@app.route("/registerAction", methods=['POST'])
def registerAction():
    employeeNumber = request.form["employeeNumber"]
    username = request.form["username"]
    userid = request.form["userid"]
    password = request.form["password"]
    signUpService.registerAction(employeeNumber, username, userid, password)
    # 登録後login.html をリダイレクトする
    return redirect("/login")


@app.route("/attendance")
def attendance():
    '''
    カードリーダーからの受信
    '''
    cardId = request.args.get("id")
    return str(attendanceService.existIdAndAttendance(cardId))

if __name__ == "__main__":
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0', port=5000)
