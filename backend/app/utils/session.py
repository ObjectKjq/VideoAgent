"""内存Session存储"""

import time
import secrets
from typing import Optional, Dict, Any
from app.config import settings


class MemorySessionStore:
    """内存Session存储"""

    def __init__(self):
        self._sessions: Dict[str, Dict[str, Any]] = {}

    def create_session(self, user_id: int, user_data: Dict[str, Any]) -> str:
        """创建Session"""
        session_id = secrets.token_urlsafe(32)
        self._sessions[session_id] = {
            "user_id": user_id,
            "user_data": user_data,
            "created_at": time.time(),
            "expires_at": time.time() + settings.session_max_age
        }
        return session_id

    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """获取Session"""
        if session_id not in self._sessions:
            return None

        session = self._sessions[session_id]
        if time.time() > session["expires_at"]:
            del self._sessions[session_id]
            return None

        return session

    def delete_session(self, session_id: str) -> bool:
        """删除Session"""
        if session_id in self._sessions:
            del self._sessions[session_id]
            return True
        return False

    def refresh_session(self, session_id: str) -> bool:
        """刷新Session过期时间"""
        if session_id not in self._sessions:
            return False

        self._sessions[session_id]["expires_at"] = time.time() + settings.session_max_age
        return True

    def get_user_id(self, session_id: str) -> Optional[int]:
        """获取Session中的用户ID"""
        session = self.get_session(session_id)
        if session:
            return session["user_id"]
        return None

    def get_user_data(self, session_id: str) -> Optional[Dict[str, Any]]:
        """获取Session中的用户数据"""
        session = self.get_session(session_id)
        if session:
            return session["user_data"]
        return None


session_store = MemorySessionStore()
