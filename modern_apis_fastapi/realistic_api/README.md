
# **Weather Service** A restful weather service

The Course weather service

## **Endpoints**
* **Current weather in a city**: </br>
  `GET /api/weather/{city}?country={country}`

* **Parameters**: </br>
  - **Required**: `city={city}` - the city want to get the weather at.
  - Optional: `state={state}` - the state of the city (Us only, two letter abbreviations)
  - Optional: `country={country}` - country, US if none specific (two letter abreviations)
  - Optional: `units={units}` - units: {metric, imperial, standard}, defaults to metric.
