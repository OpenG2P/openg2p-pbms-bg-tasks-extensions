from .models import BeneficiaryListSummaryFamilies, BeneficiaryListSummaryStudent, BeneficiaryListSummaryFarmer


def get_models():
    return [
        BeneficiaryListSummaryFamilies,
        BeneficiaryListSummaryStudent,
        BeneficiaryListSummaryFarmer
    ]