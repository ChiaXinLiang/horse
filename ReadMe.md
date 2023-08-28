#跑程式
uvicorn matchPredictAPI:app --reload

#API 調用，輸入參數位置在input.json
curl -X POST -H "Content-Type: application/json" -d @input.json http://127.0.0.1:8000/calculate_stats/