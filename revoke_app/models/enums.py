from django.db import models


class GenederEnums(models.TextChoices):

    MALE = "Male"
    FEMALE = "Female"


class SugarEnums(models.TextChoices):

    NORMAL = "Normal"
    PRE_DIABETES = "Pre-diabetes"
    DIABETES = "Diabetes"


class BPEnums(models.TextChoices):

    HEALTHY = "Healthy"
    ELEVATED = "Elevated"
    STAGE_ONE_HYPERTENSION = "Stage 1 Hypertension"
    STAGE_TWO_HYPERTENSION = "Stage 2 Hypertension"
    HYPERTENSION_CRISIS = "Hypertension Crisis"