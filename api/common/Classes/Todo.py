from api.database.database import get_db,close_db


class TodoModel:


    #obtains todo data filtering by an specific ID.
    @classmethod
    def getTodoById(self,todo_id):

        #creates a connections with the database.
        db,c = get_db()
        #retrieves the data from the database.
        c.execute(
            """
            SELECT * FROM todo WHERE id = %s
            """,(todo_id,)
        )
        result = c.fetchone()
        close_db()
        return result


    @classmethod
    def createTodo(self,title,body):

        #creates a connections with the database.
        db,c = get_db()
        #creates the new record.
        c.execute(
            """
            INSERT INTO todo (title,body)
            VALUES (%s, %s)
            """,(title,body)
        )
        #commits the changes.
        db.commit()
        close_db()

    @classmethod
    def deleteTodo(self,todo_id):
        db,c = get_db()

        #delest the todo with the given id.
        c.execute(
            """
            DELETE FROM todo
            WHERE id = %s
            """,(todo_id,)
        )
        
        db.commit()
        close_db()
    
    @classmethod 
    def updateTodo(self,todo_id,title,body):
        db,c = get_db()


        #updat the todo with the given ID andata.
        c.execute(
            """
            UPDATE todo
            SET title = %s, body = %s
            WHERE id = %s
            """,(title,body,todo_id)
        )
        db.commit()
        close_db()
        