import enum


class G2PRegistryType(enum.Enum):
    WORKER = "worker"
    WORKER_DAILY = "worker_daily"
    WORKER_MONTHLY = "worker_monthly"
    OTHER = "other"
