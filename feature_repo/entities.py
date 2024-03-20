from feast import (
    Entity,
)

user = Entity(name="user", join_keys=["user_id"],description='Entity to represent user for loan default prediction')







