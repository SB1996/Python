# In python method overloading doesn't support....
#
# But logicaly we implement method overloading in our code(It is not actual method overloading as we saw in java
# or other object oriented programming)


class Addition:
    def sum(self, data00=None, data01=None, data02=None):
        result = 0
        if data00==None and data01==None and data02==None:
            return result
        elif data01==None and data02==None:
            result = data00
            return result
        elif data02==None:
            result = data00 + data01
            return result
        else:
            result = data00 + data01 + data02
            return result

obj = Addition()
print(f"Result : {obj.sum()}")
print(f"Result : {obj.sum(10)}")
print(f"Result : {obj.sum(10,20)}")
print(f"Result : {obj.sum(10,20,30)}")
