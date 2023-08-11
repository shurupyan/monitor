from pydantic import BaseModel, HttpUrl, IPvAnyAddress
from decimal import Decimal


class ServerModel(BaseModel):
    url: str
    lat: str
    lon: str
    name: str
    country: str
    cc: str
    sponsor: str
    id: str
    host: str
    d: float
    latency: float


class ClientModel(BaseModel):
    ip: str
    lat: str
    lon: str
    isp: str
    isprating: str
    rating: str
    ispdlavg: str
    ispulavg: str
    loggedin: str
    country: str


class MeasurementModel(BaseModel):
    download: float
    upload: float
    ping: float
    server: ServerModel
    client: ClientModel
    timestamp: str
    bytes_sent: int
    bytes_received: int


example = {
    "download": 91281228.06224793,
    "upload": 26702189.43305691,
    "ping": 13.931,
    "server": {
        "url": "http://speedtest4.mts.rs:8080/speedtest/upload.php",
        "lat": "44.8206",
        "lon": "20.4622",
        "name": "Belgrade",
        "country": "Serbia",
        "cc": "RS",
        "sponsor": "Telekom mts",
        "id": "43446",
        "host": "speedtest4.mts.rs:8080",
        "d": 68.55203566938273,
        "latency": 13.931
    },
    "timestamp": "2023-03-08T14:06:00.911831Z",
    "bytes_sent": 34922496,
    "bytes_received": 114312356,
    "share": None,
    "client": {
        "ip": "80.74.160.42",
        "lat": "45.25",
        "lon": "19.8362",
        "isp": "Orion Telekom",
        "isprating": "3.7",
        "rating": "0",
        "ispdlavg": "0",
        "ispulavg": "0",
        "loggedin": "0",
        "country": "RS"
    }
}
