import abc
import model


class AbstractRepository(abc.ABC):
    def add(self, notification: model.Notification):
        self._add(notification)

    def get(self, id) -> model.Notification:
        notification = self._get(id)
        return notification

    @abc.abstractmethod
    def _add(self, notification: model.Notification):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id) -> model.Notification:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, notification):
        self.session.add(notification)

    def _get(self, id):
        return self.session.query(model.Notification).filter_by(id=id).first()
