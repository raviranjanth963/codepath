# import os
# from flask import Flask, request, jsonify, session, send_from_directory
# from werkzeug.security import generate_password_hash, check_password_hash
# from mysql.connector import connect
# from dotenv import load_dotenv

# # Load database settings
# load_dotenv()

# app = Flask(__name__)
# app.secret_key = os.getenv("FLASK_SECRET_KEY")


# # Connect Python with MySQL
# def get_connection():
#     return connect(
#         host=os.getenv("DB_HOST"),
#         port=int(os.getenv("DB_PORT", 3306)),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME")
#     )


# # Open login page
# @app.route("/")
# def home():
#     return send_from_directory(".", "login.html")


# @app.route("/login.css")
# def css():
#     return send_from_directory(".", "login.css")


# @app.route("/login.js")
# def javascript():
#     return send_from_directory(".", "login.js")


# # CREATE ACCOUNT
# @app.route("/register", methods=["POST"])
# def register():

#     data = request.json

#     username = data["username"].strip()
#     contact = data["contact"].strip()
#     contact_type = data["contact_type"]
#     password = data["password"]

#     if len(username) < 3 or len(password) < 8:
#         return jsonify({"message": "Check your username and password."}), 400

#     if contact_type not in ["email", "phone"]:
#         return jsonify({"message": "Invalid contact type."}), 400

#     email = contact.lower() if contact_type == "email" else None
#     phone = contact if contact_type == "phone" else None

#     # Securely hash the password
#     password_hash = generate_password_hash(password)

#     db = get_connection()
#     cursor = db.cursor()

#     try:
#         sql = """
#         INSERT INTO users (username, email, phone, password_hash)
#         VALUES (%s, %s, %s, %s)
#         """

#         cursor.execute(sql, (username, email, phone, password_hash))
#         db.commit()

#         return jsonify({"message": "Account created successfully!"}), 201

#     except Exception as e:
#         db.rollback()
    
#         print("REGISTRATION ERROR:", repr(e))
    
#         return jsonify({
#             "message": "Registration failed. Check Python terminal."
#         }), 500

#     finally:
#         cursor.close()
#         db.close()


# # SIGN IN
# @app.route("/login", methods=["POST"])
# def login():

#     data = request.json

#     identifier = data["identifier"].strip()
#     login_type = data["login_type"]
#     password = data["password"]

#     db = get_connection()
#     cursor = db.cursor(dictionary=True)

#     try:
#         if login_type == "username":
#             cursor.execute(
#                 "SELECT * FROM users WHERE username = %s",
#                 (identifier,)
#             )

#         elif login_type == "phone":
#             cursor.execute(
#                 "SELECT * FROM users WHERE phone = %s",
#                 (identifier,)
#             )

#         else:
#             return jsonify({"message": "Invalid login method."}), 400

#         user = cursor.fetchone()

#         if user and check_password_hash(user["password_hash"], password):

#             session["user_id"] = user["user_id"]
#             session["username"] = user["username"]

#             return jsonify({
#                 "message": "Welcome back, " + user["username"] + "!"
#             })

#         return jsonify({"message": "Incorrect username or password."}), 401

#     finally:
#         cursor.close()
#         db.close()


# # CHECK LOGIN STATUS
# @app.route("/me")
# def me():

#     if "user_id" in session:
#         return jsonify({
#             "username": session["username"]
#         })

#     return jsonify({"message": "Not logged in."}), 401


# # LOGOUT
# @app.route("/logout", methods=["POST"])
# def logout():

#     session.clear()

#     return jsonify({"message": "Logged out successfully."})


# # Start Python server
# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=5000)









# from flask import Flask, render_template, request, jsonify, url_for

# app = Flask(__name__)


# # 1. Login page
# @app.route('/')
# def login():
#     return render_template('login.html')


# # 2. Roadmap page
# @app.route('/road_map')
# def road_map():
#     return render_template('road_map3.html')


# # 3. Login verification
# @app.route('/login', methods=['POST'])
# def login_user():

#     data = request.get_json(silent=True) or {}

#     identifier = data.get('identifier')
#     login_type = data.get('login_type')
#     password = data.get('password')

#     print("Login request received:", login_type, identifier)

#     # Username login
#     if login_type == "username":

#         if identifier == "test@gmail.com" and password == "12345":

#             print("Login successful! Redirecting to roadmap.")

#             return jsonify({
#                 "message": "Login successful!",
#                 "redirect": url_for('road_map')
#             }), 200

#     # Phone login
#     elif login_type == "phone":

#         if identifier == "1234567890" and password == "12345":

#             print("Login successful! Redirecting to roadmap.")

#             return jsonify({
#                 "message": "Login successful!",
#                 "redirect": url_for('road_map')
#             }), 200

#     # Invalid login
#     return jsonify({
#         "message": "Invalid username, phone number or password!"
#     }), 401


# if __name__ == '__main__':
#     app.run(debug=True)



# @app.route('/road_map')
# def road_map():
#     return render_template('road_map3.html')




import os
from flask import (
    Flask, request, jsonify, session,
    send_from_directory, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector import connect
from dotenv import load_dotenv

# Load database settings
load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY") or "dev-only-change-this-key"


# CONNECT PYTHON WITH MYSQL
def get_connection():
    return connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


# LOGIN PAGE
@app.route("/")
def home():
    return send_from_directory(".", "login.html")


# LOGIN CSS
@app.route("/login.css")
def css():
    return send_from_directory(".", "login.css")


# LOGIN JAVASCRIPT
@app.route("/login.js")
def javascript():
    return send_from_directory(".", "login.js")


# ROADMAP PAGE
@app.route("/road_map")
def road_map():
    return send_from_directory(".", "road_map3.html")


# CREATE ACCOUNT
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json(silent=True) or {}

    username = (data.get("username") or "").strip()
    contact = (data.get("contact") or "").strip()
    contact_type = data.get("contact_type")
    password = data.get("password") or ""

    if len(username) < 3 or len(password) < 8:
        return jsonify({
            "message": "Check your username and password."
        }), 400

    if not contact or contact_type not in ["email", "phone"]:
        return jsonify({
            "message": "Invalid contact details."
        }), 400

    email = contact.lower() if contact_type == "email" else None
    phone = contact if contact_type == "phone" else None

    password_hash = generate_password_hash(password)

    db = get_connection()
    cursor = db.cursor()

    try:
        sql = """
        INSERT INTO users (username, email, phone, password_hash)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (username, email, phone, password_hash)
        )

        db.commit()

        return jsonify({
            "message": "Account created successfully!"
        }), 201

    except Exception as e:
        db.rollback()
        print("REGISTRATION ERROR:", repr(e))

        return jsonify({
            "message": "Registration failed. Check Python terminal."
        }), 500

    finally:
        cursor.close()
        db.close()


# SIGN IN
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json(silent=True) or {}

    identifier = (data.get("identifier") or "").strip()
    login_type = data.get("login_type")
    password = data.get("password") or ""

    if not identifier or not password:
        return jsonify({
            "message": "Please enter your login details."
        }), 400

    db = get_connection()
    cursor = db.cursor(dictionary=True)

    try:

        if login_type == "username":

            cursor.execute(
                "SELECT * FROM users WHERE username = %s",
                (identifier,)
            )

        elif login_type == "phone":

            cursor.execute(
                "SELECT * FROM users WHERE phone = %s",
                (identifier,)
            )

        else:
            return jsonify({
                "message": "Invalid login method."
            }), 400

        user = cursor.fetchone()

        if user and check_password_hash(
            user["password_hash"], password
        ):

            # Save login session
            session["user_id"] = user["user_id"]
            session["username"] = user["username"]

            print("LOGIN SUCCESSFUL:", user["username"])

            # Send roadmap URL to JavaScript
            return jsonify({
                "message": "Welcome back, " + user["username"] + "!",
                "redirect": url_for("road_map")
            }), 200

        return jsonify({
            "message": "Incorrect username or password."
        }), 401

    finally:
        cursor.close()
        db.close()


# CHECK LOGIN STATUS
@app.route("/me")
def me():

    if "user_id" in session:
        return jsonify({
            "username": session["username"]
        })

    return jsonify({
        "message": "Not logged in."
    }), 401


# LOGOUT
@app.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "message": "Logged out successfully."
    })


# START PYTHON SERVER
if __name__ == "__main__":
    app.run(
        debug=True,
        # host="127.0.0.1",
        # port=5000
        host="live server",
        port=5502
    )

@app.route("/road_map")
def road_map():

    if "user_id" not in session:
        return jsonify({"message": "Please sign in first."}), 401

    return send_from_directory(".", "road_map3.html")