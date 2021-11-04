from tortoise.contrib.pydantic import pydantic_model_creator

from models import Admin

Admin_Pydantic = pydantic_model_creator(Admin, name="Admin",exclude=['password', 'update_at', 'delete_at'])
AdminIn_Pydantic = pydantic_model_creator(Admin, name="AdminIn", exclude_readonly=True)
