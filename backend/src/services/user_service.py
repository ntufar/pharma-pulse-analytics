from typing import List, Optional
from ..models.user import User

class UserService:
    def __init__(self):
        self.users: List[User] = []

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_all_users(self) -> List[User]:
        return self.users

    def update_user(self, user_id: str, updated_user: User) -> Optional[User]:
        for i, user in enumerate(self.users):
            if user.id == user_id:
                self.users[i] = updated_user
                return updated_user
        return None

    def delete_user(self, user_id: str) -> bool:
        initial_len = len(self.users)
        self.users = [u for u in self.users if u.id != user_id]
        return len(self.users) < initial_len
