import enum


class G2PRegistryType(enum.Enum):
    RATION_CARD_APPLICANTS = "ration_card_applicants"
    INDIVIDUALS = "individuals"
    FAMILIES = "families"
    ELEC_MONTHLY_AVG = "elec_monthly_avg"
    GOVT_EMPLOYEES = "govt_employees"
    LAND_HOLDINGS = "land_holdings"
    LRS_BRS_APPLICATION = "lrs_brs_application"
    PROFESSIONAL_TAX_PAYERS = "professional_tax_payers"
    RESIDENTIAL_HOUSES = "residential_houses"
    VEHICLE_OWNERSHIP = "vehicle_ownership"
    OTHER = "other"
