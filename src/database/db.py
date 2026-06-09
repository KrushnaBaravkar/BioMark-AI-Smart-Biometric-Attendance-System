from src.database.config import supabase
import bcrypt

# Hashing the passward
def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

# Matching the present password and the hashed password that is stored at the Username of that user
def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


# Check for the unique username, return false if username is taken initially.
def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

# creat teacher's account.
def create_teacher(username, password, name):
    data = {
        "username" : username,
        "password" : hash_pass(password),
        "name" : name
    }
    response = supabase.table("teachers").insert(data).execute()
    return response.data

# Teacher's login.
def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None

def get_all_students():
    response = supabase.table('students').select("*").execute()
    return response.data

# creating new student 
def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {'name': new_name, 'face_embedding':face_embedding, "voice_embedding": voice_embedding}
    response = supabase.table('students').insert(data).execute()
    return response.data