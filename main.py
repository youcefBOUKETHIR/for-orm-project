from  sqlalchemy import create_engine


engine = create_engine('sqlite:///Alexandria.db')

connect = engine.connect()

connect.close()