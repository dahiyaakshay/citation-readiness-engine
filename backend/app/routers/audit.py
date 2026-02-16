from fastapi import APIRouter
from app.models.auditModels import AuditRequest
from app.services.citationAuditService import run_citation_audit

router = APIRouter(prefix="/audit", tags=["Audit"])

@router.post("/")
def audit(request: AuditRequest):
    return run_citation_audit(request)
