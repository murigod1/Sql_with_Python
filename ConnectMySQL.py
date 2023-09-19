# from sqlalchemy import create_engine

# # Configuração da conexão com o banco de dados
# user = 'seu_usuario'
# password = 'sua_senha'
# host = 'localhost'
# database = 'nome_do_banco_de_dados'

# # Criar uma string de conexão
# connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

# # Criar o engine de conexão
# engine = create_engine(connection_string)

# # Estabelecer a conexão
# conn = engine.connect()

# # A partir daqui, podemos executar consultas ou operações no banco de dados
# ## […]

# # Fechar a conexão quando terminar
# conn.close()


# -------------------------------------------------------------------------------------

# import mysql.connector

# # Configuração da conexão com o banco de dados
# HOST = 'localhost'
# USERNAME = 'seu_usuario'
# PASSWORD = 'sua_senha'
# DATABASE = 'nome_do_banco_de_dados'

# # Estabelecer a conexão
# connection = mysql.connector.connect(
# host= HOST,
# user= USERNAME,
# password= PASSWORD,
# database= DATABASE
# )

# # Testar estabelecimento de conexão
# if not(connection.is_connected()):
#     print("Não conectado com MySQL Server")

# A partir daqui, podemos executar consultas ou operações no banco de dados
## […]

# Fechar a conexão quando terminar
# conn.close()

# Link para documentação
# https://dev.mysql.com/doc/connector-python/en/