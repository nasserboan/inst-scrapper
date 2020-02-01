from narcisus.scrapper import VanityBot
from secrets.secrets import pw

my_bot = VanityBot('nsboan',pw)

ls = ['howesdiego','erikclari','natanboan_']

data = {}

for person in ls:
    data[person] = my_bot.get_any_following(person)