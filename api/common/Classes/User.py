from api.database.database import get_db,close_db




class User:



    @classmethod
    def authenticateUser(self,username,password):
        db,c = get_db()
        c.execute(
            """
            SELECT user_id FROM user
            WHERE username = %s and password = %s
            """,(username,password)
        )
        result = c.fetchone()
        close_db
        return result

    @classmethod
    def getUserById(self,user_id):
        db,c = get_db()
        c.execute(
            """
            SELECT user_id,username,created_at FROM user
            WHERE user_id = %s
            """,(user_id,)
        )
        result = c.fetchone()
        close_db
        return result