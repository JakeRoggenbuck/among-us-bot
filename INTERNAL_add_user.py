from database import DatabaseCommunicator

user_id = input("User id: ")
guild_id = input("Guild id: ")
perm = input("Perm: ")
db = DatabaseCommunicator(guild_id)
db.auth.find_one_and_update(
    {"user_id": user_id}, {"$push": {"access": perm}}, upsert=True
)
