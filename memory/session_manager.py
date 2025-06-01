# Simple placeholder for session memory handling
# You can expand this with MOYA memory APIs

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def store_message(self, session_id, sender, content):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append({'sender': sender, 'content': content})

    def get_session_history(self, session_id):
        return self.sessions.get(session_id, [])
