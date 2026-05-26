# My Project - Version 1.0.1 (Hotfix)

def login(username, password):
    # Hotfix: handle empty password crash
    if not username or not password:
        return "Error: Username and password required"
    return "Login successful"

def dashboard():
    return "Dashboard loaded"
