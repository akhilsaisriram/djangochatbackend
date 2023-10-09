# # utils.py

# import redis

# class CustomChannelManager:
#     def __init__(self):
#         self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

#     def add_user_to_group(self, user_channel, group_name):
#         self.redis_client.sadd(group_name, user_channel)

#     def remove_user_from_group(self, user_channel, group_name):
#         self.redis_client.srem(group_name, user_channel)

#     def get_online_users_in_group(self, group_name):
#         return self.redis_client.smembers(group_name)
