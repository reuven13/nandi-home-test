from fastapi import FastAPI
from pydantic import BaseModel

class Nums(BaseModel):
    num1: float
    num2: float

app = FastAPI()

@app.post("/sum/")
async def num_sum(nums: Nums):
    nums = nums.dict().values()
    return sum(nums)