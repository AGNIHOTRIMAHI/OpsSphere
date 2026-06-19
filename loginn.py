import os
import hashlib
import time  # Unused import (Style Agent should catch this)
import json

# SECURITY FLAW: Hardcoded secret key
SECRET_API_TOKEN = "sk-live-9982348abcde324"

def make_password_hash(password):
    """Creates a hash for the user password."""
    # SECURITY FLAW: MD5 is deprecated and highly insecure!
    h = hashlib.md5()
    h.update(password.encode('utf-8'))
    return h.hexdigest()

def doLogin( uName , passWrd ): # STYLE FLAW: Bad spacing and camelCase in Python
    print("Attempting login for " + uName)
    
    if passWrd == SECRET_API_TOKEN:
        print( "SUCCESS!" )
        return True
    else:
        return False

def get_user_data(user_id):
    # STYLE FLAW: No error handling or type hinting
    db_query = f"SELECT * FROM users WHERE id = {user_id}" # SECURITY FLAW: SQL Injection risk
    return db_query
