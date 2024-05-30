from fastapi import FastAPI
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import correlation

app = FastAPI()


@app.get('/')
async def read_root():
    correlation.create_heatmap()
    return {"message": "Correlation heatmap generated successfully!"}
