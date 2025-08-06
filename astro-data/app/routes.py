from fastapi import FastAPI
from app import gaia, npc

router = APIrouter()

@router.get("/sync/gaia")
def sync_gaia():
    result = gaia.fetch_and_store()
    return{"status": "GATA sync concluido", "data": result}

@router.get("/sync/npc")
def sync_npc():
    result = npc.fetch_and_store()
    return {"status": "NPC sync concluido", "data": result}

@router.get("/sync/simbad")
def sync_simbad():
    result = simbad.fetch_and_store()
    return {"status": "SIMBAD sync concluído", "data": result}