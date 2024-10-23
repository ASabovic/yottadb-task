import mg_python

#Set the connection details for YottaDB
mg_python.m_set_host(0, "::1", 7041, "", "")

#Set up the environment variables for YottaDB
envvars = "";
envvars = envvars + "ydb_dir=/root/.yottadb\n"
envvars = envvars + "ydb_rel=r2.00_x86_64\n"
envvars = envvars + "ydb_gbldir=/root/.yottadb/r2.00_x86_64/g/yottadb.gld\n"
envvars = envvars + "ydb_routines=/root/.yottadb/r2.00_x86_64/o/utf8*(/root/.yottadb/r2.00_x86_64/r root/.yottadb/r) /usr/local/lib/yottadb/r200/libyottadbutil.so\n"
envvars = envvars + "ydb_ci=/usr/local/lib/yottadb/r200/zmgsi.ci\n"
envvars = envvars + "\n"

#Bind the server API for YottaDB
result_api = mg_python.m_bind_server_api(0, "YottaDB", "/usr/local/lib/yottadb/r200", "", "", envvars, "") or False
print(f"Server API bind result: {result_api}")

#Set the value in YottaDB
name_set = mg_python.m_set(0, "^Customer", 1, "Customer_1")
print("Set ^Customer(1) = 'Customer_1'")

#Get the value from YottaDB
name = mg_python.m_get(0, "^Customer", 1)
print(f"Retrieved name from ^Customer(1): {name}")
print(f"Type of retrieved value: {type(name)}")

#Release the server API
mg_python.m_release_server_api(0)