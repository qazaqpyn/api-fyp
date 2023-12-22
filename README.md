# KDV API

## Set up 
```pip install flask```
```pip install libkdv```

## Run
    run `app.py` file 
    
## Example: 

### Request:     
    URL: `http://127.0.0.1:5000/generate` METHOD: `POST`
        body structure (example):
```
            {
                "params": {
                    "kdvType": "KDV",
                    "gps": true,
                    "bandwidthS": 1000,
                    "rowP": 800,
                    "colP": 640,
                    "bandwidthT":6,
                    "tPixel": 32,
                    "nThreads": 8
                },
                "data": [
                    [109.513275, 18.245386],
                    [109.70136, 18.32075],
                    [109.38009, 18.297674],
                    [109.430954, 18.293081],
                    [109.53363, 18.29658],
                    [109.44988, 18.300335],
                    [109.62179, 18.227533],
                    [109.78003, 18.402117],
                    [109.498146, 18.261425],
                    [109.52124, 18.297764],
                    [109.38047, 18.297615],
                    [109.49532, 18.26565],
                    [109.528694, 18.300205],
                    [109.5088, 18.271883],
                    [109.582146, 18.282848],
                    [109.48144, 18.269518],
                    [109.515045, 18.295343],
                    [109.492744, 18.27925],
                    [109.49725, 18.279707],
                    [109.571075, 18.274916],
                    [109.74804, 18.391016],
                    [109.573746, 18.282217],
                    [109.626625, 18.228107],
                    [109.20548, 18.305998],
                    [109.50912, 18.25439],
                    [109.47484, 18.290024],
                    [109.51658, 18.223713],
                    [109.51464, 18.255003],
                    [109.48248, 18.268753],
                    [109.51323, 18.234306]
                ]
            }
```

## Response:
```
    {
        "data": [
            [
                109.20548,
                18.288206464786608,
                0.004450203189
            ],
            [
                109.20548,
                18.288485657272602,
                0.01074070617
            ],
            [
                109.20548,
                18.288764849767592,
                0.0169317152
            ],
            [
                109.20548,
                18.289044042253586,
                0.02302323027
            ],
            [
                109.20548,
                18.289323234739584,
                0.02901525139
            ]
        ],
        "middle": [
            109.51612530665066,
            18.29044000469256
        ]
    }
```