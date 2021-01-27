# REST API for insurance cost calculating with FastAPI

## Project Structure

<pre>
.                                                                 
├── services                    # different purpose services      
    ├── __init.py__             # python package init file        
    ├── insurance.py            # insurance related services      
    └── tariffs.py              # tariffs related services        
├── .gitignore                  # .gitignore file                 
├── docker-compose.yml          # yml file for docker-compose     
├── Dockerfile                  # Dockerfile                      
├── main.py                     # FastAPI app                     
├── models.py                   # tortoise models                 
├── README.md                   # <-- you are here                
└── requirements.txt            # python requirements       
</pre>      

## How to run

1. Install Docker Compose: https://docs.docker.com/compose/install/

2. Run docker-compose:
```
sudo docker-compose up --build
```

## REST API endpoints

1. Load tariffs:
- Route: ``` /tariffs ```
- Method: POST
- Data params: json*
- Response: json*

2. Get tariffs:
- Route: ``` /tariffs ```
- Method: GET
- Response: json*

3. Calculate insurance cost::
- Route: ``` /insurance_cost ```
- Method: POST
- Data params: Cargo object
- Response: Cargo object

4. Get all cargos:
- Route: ``` /cargos ```
- Method: GET
- Response: List of Cargo objects

json* in the following format:
<pre>
{
  "2020-01-01": [
    {
      "cargo_type": "Glass",
      "rate": "0.04"
    },
    ...
  ],
  ...
}
</pre>

## Usage example

1. Check current tariffs:  <br/>
GET to ``` /tariff ```  
Response: {}  <br/>
*no current tarrifs*

2. Load new tarrifs:  <br/>
POST to ``` /tariff ```
<pre>
data = {
  "2020-01-01": [
    {
      "cargo_type": "Glass",
      "rate": "0.04"
    },
    {
      "cargo_type": "Other",
      "rate": "0.01"
    }
  ],
  "2020-01-02": [
    {
      "cargo_type": "Glass",
      "rate": "0.035"
    },
    {
      "cargo_type": "Other",
      "rate": "0.015"
    }
  ]
}
</pre>
Response: *same as data*  </br>
*You can do POST request with FastAPI interactive docs by going to ``` /docs ``` or with Postman: https://www.postman.com/

3. Calculate insurance cost for new cargo:  <br/>
POST to ``` /insurance_cost ```
<pre>
data = {
  "id": 1,
  "date": "2020-01-01",
  "cargo_type": "Glass",
  "declared_cost": 1000,
  "insurance_cost": null
}

Response = {
  "id": 1,
  "date": "2020-01-01",
  "cargo_type": "Glass",
  "declared_cost": 1000,
  "insurance_cost": 40
}
</pre>
*Calculated insurance cost 40 = 1000 x 0.04 for cargo at date 2020-01-01 of type Glass (rate = 0.05)*

4. Get list of all cargos:  <br/>
GET to ``` /cargos ```
<pre>
Reponse =  [
  {
    "id": 1,
    "date": "2020-01-01",
    "cargo_type": "Glass",
    "declared_cost": 1000,
    "insurance_cost": 40
  }
]
</pre>
*Newly added cargo object*

# Imlementation Details
- REST API is developed with the FastAPI framework
- Models are developed with tortoise orm
- PostgreSQL is used as a database server
- Deployment is done with Docker Compose
- Project is developed with Git

- Tariff Model has the following format:
  <pre>
  {
    id: Int,
    date: Date,
    cargo_type: String,
    rate: Float,
  }
  </pre>

- Cargo Model has the following format:
  <pre>
  {
    id: Int,
    date: Date,
    cargo_type: String,
    declared_cost: Float,
    insurance_cost: Float
  }
  </pre>
  
