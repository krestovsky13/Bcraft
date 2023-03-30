from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def commit(self):
        try:
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise
