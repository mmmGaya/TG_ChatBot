from aiogram.utils import executor
from dialog_db import create_db
from create_bot import dp
from handlers import client, admin

# -----Connect to DB--------
create_db.connect_to_database()

#---------Register client handlers-----
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)



executor.start_polling(dp, skip_updates=True)




