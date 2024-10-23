import mg_python

db=0

# Set the connection details for YottaDB
mg_python.m_set_host(db, "localhost", 7041, "", "")
mg_python.m_set_uci(db, "USER")

print("\nmg_python version: ", mg_python.m_ext_version())

result = mg_python.m_set(db, "^Customer", 1, "Customer_1")
result = mg_python.m_get(db, "^Customer", 1)
result_2 = mg_python.m_set(db, "^Customer", 2, "Customer_2")
result2 = mg_python.m_get(db, "^Customer", 2)
print(result, result2)

math_result = mg_python.m_function(0, "add^math", 3, 3)
mg_python.m_set(db, "^MathResult", 1, math_result)
retrieved_result = mg_python.m_get(db, "^MathResult", 1)
print(f"Math result: {math_result}")
print(f"Retrieved result from YottaDB: {retrieved_result}")