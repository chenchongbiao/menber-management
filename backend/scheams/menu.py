from tortoise.contrib.pydantic import pydantic_model_creator
from models import Menu

Menu_Pydantic = pydantic_model_creator(Menu, name="Menu", exclude=['update_at', 'delete_at'])
MenuIn_Pydantic = pydantic_model_creator(Menu, name="MenuIn", exclude_readonly=True)
