from openg2p_bg_task_models.models import BeneficiaryListSummary
from sqlalchemy import JSON, Float, String
from sqlalchemy.orm import mapped_column


class BeneficiaryListSummaryFamilies(BeneficiaryListSummary):
    __tablename__ = "beneficiary_list_summary_families"

    no_of_children_q3 = mapped_column(JSON, nullable=True)
    no_of_children_q2 = mapped_column(JSON, nullable=True)
    no_of_children_q1 = mapped_column(JSON, nullable=True)

