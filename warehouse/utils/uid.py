import uuid
import sqlalchemy.types as types


class UUID(types.TypeDecorator):
    """Custom UUID type that stores UUIDs as binary(16) in MySQL."""

    impl = types.BINARY(16)

    def process_bind_param(self, value, dialect):
        """Convert UUID to binary format for storage in the database."""
        if value is None:
            return None
        elif isinstance(value, str):
            return uuid.UUID(value).bytes
        elif isinstance(value, uuid.UUID):
            return value.bytes
        else:
            raise TypeError("Invalid UUID value")

    def process_result_value(self, value, dialect):
        """Convert binary to UUID format when retrieved from the database."""
        if value is None:
            return None
        else:
            return uuid.UUID(bytes=value)
