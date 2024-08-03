def conexion():
    server = 'JORD'
    database = 'ec4evaluacion'
    username = 'sa'
    password = '1239875'
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador adecuado instalado

    conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'
    return conn_str