class UserApi(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)

    def post(self):
        try:
            data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if User.query.filter_by(username=data["username"]).first():
            return {"message": "Username already exists"}, 400

        user = user_datastore.create_user(
            username=data["username"],
            email=data["email"],
            password=hash_password(data["password"]),
        )

        db.session.commit()

        return user_schema.dump(user), 201

    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        try:
            data = request.get_json()
            for key, value in data.items():
                if hasattr(user, key) and value is not None:
                    setattr(user, key, value)
            db.session.commit()
            return user_schema.dump(user)
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        try:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500
