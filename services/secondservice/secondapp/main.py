from fastapi import FastAPI

app = FastAPI()

class KeyValService:
    #class attribute
    test_dict = dict()

    #setter for our app
    def set_key_and_val(self, key, val):
        keys = self.test_dict.keys()
        if key in keys:
            return {"Error" : "Key already exists"}
        self.test_dict[key] = val
        return self.test_dict[key]

    #getter
    def get_val(self, key):
        keys = self.test_dict.keys()
        if key not in keys:
            return {"Error": "Key does not exist"}
        return self.test_dict[key]

test_dict = KeyValService()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-dict-value/{dict_key}")
def get_dict(dict_key: str):
    val = test_dict.get_val(dict_key)
    return val

@app.put("/update-dict/{dict_key}/{dict_value}")
def update_dict(dict_key: str, dict_value: str):
    return test_dict.set_key_and_val(dict_key, dict_value)