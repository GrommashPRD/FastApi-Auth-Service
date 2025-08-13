from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

SUCCESS_LOGINS = Counter('successful_logins', 'Количество успешных авторизаций')
FAILED_LOGINS = Counter('failed_logins', 'Количество неуспешных авторизаций')


instrumentator = Instrumentator()