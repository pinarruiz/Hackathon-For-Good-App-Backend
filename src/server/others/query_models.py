from pydantic import BaseModel

class Coordinates(BaseModel):
    latitude: float = 50.45466
    longitude: float = 30.5238

    def to_list(self):
        return [self.latitude, self.longitude]

class ImageCoordinates(BaseModel):
    image: str = "Base64 Image"
    coordinates: Coordinates

class ProcessedCoordinates(BaseModel):
    user_coordinates: Coordinates
    target_coordinates: Coordinates

class ProcessedResponse(BaseModel):
    container_type: str = "Papel"
    processed_coordinates: ProcessedCoordinates

class DecoderResponse(BaseModel):
    values: dict = {
        1 : "Envases",
        2 : "Vidrio",
        3 : "Restos",
        4 : "Organica",
        5 : "Papel o Carton"
    }