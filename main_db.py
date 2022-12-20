from db_class import Database

database = Database()
database.connect()
database.insert_initial_data()
database.print()
#database.insert(4,23,'Ann')
#database.print()
database.delete(person_id=2)
database.print()
database.delete_all()
database.print()
