import json

from fastapi import APIRouter, Request
from variamos.libs.mx_graph import MXGraph


router = APIRouter()


@router.post("/mx-graph-to-json")
async def mx_graph_to_json(request: Request) -> str:
    mx_graph = await request.body()
    feature_model_data = MXGraph.parse_string(mx_graph.decode("utf-8"))

    return json.dumps(feature_model_data)
