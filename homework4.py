immutable_var = 1, "daemond", True
print(immutable_var)
immutable_var[0] = 8 # кортеж является неизменяемой коллекцией, за исключениеем случаев когда внитри кортежа дополнительно содержится список
mutable_list = [3, 'knife','cucumber']
mutable_list[1] = False
print(mutable_list)