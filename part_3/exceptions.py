class CKKSError(Exception):
    """Errore base del dominio CKKS."""


class InvalidLevelError(CKKSError):
    """Il livello richiesto non appartiene alla catena dei moduli."""


class InvalidModulusChainError(CKKSError):
    """La catena dei moduli non è valida."""


class RescalingError(CKKSError):
    """Il rescaling non può essere eseguito."""