import os
# Примечание: при работе с путями не прописывайте слеши вручную, генерация должна быть программной.

print(os.path.abspath(''))
print(os.path.abspath(os.path.join('..', '..', '..', '..', 'access', 'admin.bat')))
print(os.path.join('Skillbox', 'access', 'admin.bat'))
