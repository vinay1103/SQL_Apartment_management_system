from database import check_user_exists, authenticate_user, close_connection,ret_type

def login(username, password):
    user_exists = check_user_exists(username)
    is_authenticated = authenticate_user(username, password)
    if user_exists and is_authenticated:
        # Get the user_id from your authentication mechanism
        return ret_type(username)
    else:
        return None