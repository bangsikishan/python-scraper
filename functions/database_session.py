from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_database_session(url: str) -> sessionmaker:
    try:
        engine = create_engine(f"mysql://{url}")
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        print("\n[-] Error in DatabaseSession.py while creating a session\n")
        raise e