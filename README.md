# Test task for Webtronics
## RESTful API microservice using FastAPI for statistics counters.
## Local launch of the project
```
git clone https://github.com/krestovsky13/webtronics
docker-compose up --build
```
## Docs:
### Swagger/Redoc - (/docs, /redoc)
### - api/v1/statistic/save:
#### Statistics are created or aggregated by date
```
REQUEST:
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/statistic/save' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "date": "2023-02-28",
  "views": 13,
  "clicks": 64,
  "cost": 75.32
}'
Request body schema:
date - string format YYYY-MM-DD, required
views - positive integer, optional
clicks - positive integer, optional
cost - positive [integer, float], optional
RESPONSE:
Successful Response - 200
Response body:
{
  "date": "2023-02-28",
  "views": 13,
  "clicks": 64,
  "cost": 75.32
}
```
### - api/v1/statistic/show:
#### Statistics for the period
```
REQUEST:
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/statistic/show?sort_by=date&order_by=desc' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "from": "2021-03-30",
  "to": "2023-03-30"
}'
Request body schema:
from - string format YYYY-MM-DD, required
to - string format YYYY-MM-DD, required
Request query params:
sort_by - column of models [date, views, clicks, cost], optional
order_by - [asc, desc], optional
RESPONSE:
Successful Response - 200
Response body:
[
  {
    "date": "2023-02-28",
    "views": 13,
    "clicks": 64,
    "cost": 75.32,
    "cpc": 1.18,
    "cpm": 5790
  },
  {
    "date": "2023-01-30",
    "views": 5,
    "clicks": 7,
    "cost": 5.32,
    "cpc": 0.76,
    "cpm": 1060
  }
]
```
### - api/v1/statistic/reset:
#### Reset all statistics
```
REQUEST:
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/v1/statistic/reset' \
  -H 'accept: application/json'
RESPONSE:
Successful Response - 200
Response body:
{
  "msg": "Statistics cleared successfully"
}
```
