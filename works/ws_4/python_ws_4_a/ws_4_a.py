# 아래에 코드를 작성하시오.

from conf import settings
from utils import create_url

my_name = settings.NAME
my_url = settings.MAIN_URL

result = create_url.create_url(name=my_name, main_url=my_url)
print(result)