from fastapi import APIRouter, Request

from ..others.query_models import Coordinates, ImageCoordinates, ProcessedCoordinates, ProcessedResponse, DecoderResponse
from ..others.helpers import get_distance

ia_router = APIRouter()

@ia_router.post("/give_trash", tags=["IA"], response_model=ProcessedResponse)
async def give_trash(request: Request, image_coordinates: ImageCoordinates):
    trash_type = 2
    trash_locations = request.app.state.locations[trash_type]
    trash_distances = {get_distance(image_coordinates.coordinates, trash_location): trash_location for trash_location in trash_locations}
    sorted_trash_distances = sorted(trash_distances)
    processed_coordinates = ProcessedCoordinates(
        user_coordinates = image_coordinates.coordinates,
        target_coordinates=trash_distances[sorted_trash_distances[0]]
    )
    return ProcessedResponse(processed_coordinates = processed_coordinates)

@ia_router.get("/get_decode", tags=["IA"], response_model=DecoderResponse)
async def give_decoder(request: Request):
    return DecoderResponse()