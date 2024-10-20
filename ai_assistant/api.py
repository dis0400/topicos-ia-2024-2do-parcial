from fastapi import FastAPI, Depends, Query
from llama_index.core.agent import ReActAgent
from ai_assistant.agent import TravelAgent
from ai_assistant.models import AgentAPIResponse
from ai_assistant.tools import reserve_flight, reserve_bus, reserve_hotel, reserve_restaurant

def get_agent() -> ReActAgent:
    return TravelAgent().get_agent()


app = FastAPI(title="AI Agent")


@app.get("/recommendations/cities")
def recommend_cities(
    notes: list[str] = Query(...), agent: ReActAgent = Depends(get_agent)
):
    prompt = f"recommend cities in bolivia with the following notes: {notes}"
    return AgentAPIResponse(status="OK", agent_response=str(agent.chat(prompt)))

@app.post("/reservations/flight")
def reserve_flight_api(
    departure: str, destination: str, date: str
):
    reservation = reserve_flight(date, departure, destination)
    return {"status": "success", "reservation": reservation}

@app.post("/reservations/bus")
def reserve_bus_api(
    departure: str, destination: str, date: str
):
    reservation = reserve_bus(date, departure, destination)
    return {"status": "success", "reservation": reservation}

@app.post("/reservations/hotel")
def reserve_hotel_api(
    checkin_date: str, checkout_date: str, hotel: str, city: str
):
    reservation = reserve_hotel(checkin_date, checkout_date, hotel, city)
    return {"status": "success", "reservation": reservation}

@app.post("/reservations/restaurant")
def reserve_restaurant_api(
    reservation_time: str, restaurant: str, city: str
):
    reservation = reserve_restaurant(reservation_time, restaurant, city)
    return {"status": "success", "reservation": reservation}
