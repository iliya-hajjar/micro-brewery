import jwt, datetime, os
from flask import Flask, request, abort, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from schema import Base, User


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://someone:someone@db_auth:3306/auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

try:
    engine = create_engine("mysql+pymysql://someone:someone@db_auth:3306/auth", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
except sqlalchemy.exc.OperationalError as e:
    session.rollback()
    print(e)


JWT_SECRET = "foo"


@app.route("/login", methods=["POST"], strict_slashes=False)
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    get_user = session.query(User).filter_by(email=auth.username)

    if get_user.first():
        email = get_user.first().email
        password = get_user.first().password

        if auth.username != email or auth.password != password:
            return "invalid credentials", 401
        else:
            return create_jwt(auth.username, JWT_SECRET, True)
    else:
        return "invalide credentials", 401


@app.route("/signup", methods=["POST"], strict_slashes=False)
def signup():
    data = request.get_json()

    try:
        set_user = User(email=data['email'], password=data['password'])
        session.add(set_user)
        session.commit()
        return jsonify({"status": 200, "user_id": set_user.id})
    except Exception as e:
        abort(400, 'Can not create user !')


@app.route("/validate", methods=["POST"], strict_slashes=False)
def validate():
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "missing credentials", 401

    encoded_jwt = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(
            encoded_jwt, JWT_SECRET, algorithms=["HS256"]
        )
    except:
        return "not authorized", 403

    return decoded, 200


def create_jwt(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
