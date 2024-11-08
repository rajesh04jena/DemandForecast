from forecast.external.vest.transformations.kde import KDE
from forecast.external.vest.transformations.power import PowerTransform

TRANSFORMATION_MODELS = \
    dict(kde=KDE,
         power=PowerTransform)

TRANSFORMATION_MODELS_FAST = \
    dict(power=PowerTransform)
