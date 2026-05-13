from .models import (
    BeneficiaryListSummaryFamilies,
    BeneficiaryListSummaryFarmer,
    BeneficiaryListSummaryHousehold,
    BeneficiaryListSummaryStudent,
)


def get_models():
    return [
        BeneficiaryListSummaryFamilies,
        BeneficiaryListSummaryStudent,
        BeneficiaryListSummaryFarmer,
        BeneficiaryListSummaryHousehold,
    ]