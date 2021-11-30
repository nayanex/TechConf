import abc
from sqlalchemy import update


class AbstractRepository(abc.ABC):
    def add(self, model):
        self._add(model)

    def get(self, id):
        return self._get(id)

    def get_all(self, *args, **kwargs):
        return self._get_all(*args, **kwargs)

    def update(self, id, updated_props):
        return self._update(id, updated_props)

    @abc.abstractmethod
    def _add(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_all(self, *args, **kwargs):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session, model):
        super().__init__()
        self.session = session
        self.model = model

    def _add(self, model):
        self.session.add(model)

    def _get(self, id):
        return self.session.query(self.model).filter_by(id=id).first()

    def _get_all(self, *args, **kwargs):
        """Return all records matching given filters."""
        return self.session.query(self.model).filter(*args, **kwargs).all()

    def _update(self, id, updated_props):
        """Update an entity with the given properties."""
        entity = self.session.query(self.model).filter_by(id=id).one()

        for key, value in updated_props.items():
            if not hasattr(entity, key):
                raise KeyError(key)
            setattr(entity, key, value)
        self.session.flush()
