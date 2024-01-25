"""Constants for the Fitbit platform."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.const import (
    CONF_CLIENT_ID,
    CONF_CLIENT_SECRET,
    PERCENTAGE,
    UnitOfLength,
    UnitOfMass,
    UnitOfTime,
)

ATTR_ACCESS_TOKEN: Final = "access_token"
ATTR_REFRESH_TOKEN: Final = "refresh_token"
ATTR_LAST_SAVED_AT: Final = "last_saved_at"

ATTR_DURATION: Final = "duration"
ATTR_DISTANCE: Final = "distance"
ATTR_ELEVATION: Final = "elevation"
ATTR_HEIGHT: Final = "height"
ATTR_WEIGHT: Final = "weight"
ATTR_BODY: Final = "body"
ATTR_LIQUIDS: Final = "liquids"
ATTR_BLOOD_GLUCOSE: Final = "blood glucose"
ATTR_BATTERY: Final = "battery"

CONF_MONITORED_RESOURCES: Final = "monitored_resources"
CONF_CLOCK_FORMAT: Final = "clock_format"
ATTRIBUTION: Final = "Data provided by Fitbit.com"

FITBIT_COMPONENT="fitbit3"
FITBIT_AUTH_CALLBACK_PATH: Final = f"/api/{FITBIT_COMPONENT}/callback"
FITBIT_AUTH_START: Final = f"/api/{FITBIT_COMPONENT}"
FITBIT_USER = "Fitbit3"  # Change to a descriptive name of the device or user
FITBIT_CONFIG_FILE: Final = f"{FITBIT_COMPONENT}.conf"
FITBIT_DEFAULT_RESOURCES: Final[list[str]] = ["activities/steps"]

DEFAULT_CONFIG: Final[dict[str, str]] = {
    CONF_CLIENT_ID: "CLIENT_ID_HERE",
    CONF_CLIENT_SECRET: "CLIENT_SECRET_HERE",
}
DEFAULT_CLOCK_FORMAT: Final = "12H"


@dataclass
class FitbitRequiredKeysMixin:
    """Mixin for required keys."""

    unit_type: str | None


@dataclass
class FitbitSensorEntityDescription(SensorEntityDescription, FitbitRequiredKeysMixin):
    """Describes Fitbit sensor entity."""


FITBIT_RESOURCES_LIST: Final[tuple[FitbitSensorEntityDescription, ...]] = (
    FitbitSensorEntityDescription(
        key="activities/activityCalories",
        name=f"{FITBIT_USER} Activity Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/calories",
        name=f"{FITBIT_USER} Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/caloriesBMR",
        name=f"{FITBIT_USER} Calories BMR",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/distance",
        name=f"{FITBIT_USER} Distance",
        unit_type="",
        icon="mdi:map-marker",
    ),
    FitbitSensorEntityDescription(
        key="activities/elevation",
        name=f"{FITBIT_USER} Elevation",
        unit_type="",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/floors",
        name=f"{FITBIT_USER} Floors",
        unit_type="floors",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/heart",
        name=f"{FITBIT_USER} Resting Heart Rate",
        unit_type="bpm",
        icon="mdi:heart-pulse",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesFairlyActive",
        name=f"{FITBIT_USER} Minutes Fairly Active",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesLightlyActive",
        name=f"{FITBIT_USER} Minutes Lightly Active",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesSedentary",
        name=f"{FITBIT_USER} Minutes Sedentary",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:seat-recline-normal",
    ),
    FitbitSensorEntityDescription(
        key="activities/minutesVeryActive",
        name=f"{FITBIT_USER} Minutes Very Active",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:run",
    ),
    FitbitSensorEntityDescription(
        key="activities/steps",
        name=f"{FITBIT_USER} Steps",
        unit_type="steps",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/activityCalories",
        name=f"{FITBIT_USER} Tracker Activity Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/calories",
        name=f"{FITBIT_USER} Tracker Calories",
        unit_type="cal",
        icon="mdi:fire",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/distance",
        name=f"{FITBIT_USER} Tracker Distance",
        unit_type="",
        icon="mdi:map-marker",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/elevation",
        name=f"{FITBIT_USER} Tracker Elevation",
        unit_type="",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/floors",
        name=f"{FITBIT_USER} Tracker Floors",
        unit_type="floors",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesFairlyActive",
        name=f"{FITBIT_USER} Tracker Minutes Fairly Active",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesLightlyActive",
        name=f"{FITBIT_USER} Tracker Minutes Lightly Active",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesSedentary",
        name=f"{FITBIT_USER} Tracker Minutes Sedentary",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:seat-recline-normal",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/minutesVeryActive",
        name=f"{FITBIT_USER} Tracker Minutes Very Active",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:run",
    ),
    FitbitSensorEntityDescription(
        key="activities/tracker/steps",
        name=f"{FITBIT_USER} Tracker Steps",
        unit_type="steps",
        icon="mdi:walk",
    ),
    FitbitSensorEntityDescription(
        key="body/bmi",
        name=f"{FITBIT_USER} BMI",
        unit_type="BMI",
        icon="mdi:human",
    ),
    FitbitSensorEntityDescription(
        key="body/fat",
        name=f"{FITBIT_USER} Body Fat",
        unit_type=PERCENTAGE,
        icon="mdi:human",
    ),
    FitbitSensorEntityDescription(
        key="body/weight",
        name=f"{FITBIT_USER} Weight",
        unit_type="",
        icon="mdi:human",
    ),
    FitbitSensorEntityDescription(
        key="sleep/awakeningsCount",
        name=f"{FITBIT_USER} Awakenings Count",
        unit_type="times awaken",
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/efficiency",
        name=f"{FITBIT_USER} Sleep Efficiency",
        unit_type=PERCENTAGE,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesAfterWakeup",
        name=f"{FITBIT_USER} Minutes After Wakeup",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesAsleep",
        name=f"{FITBIT_USER} Sleep Minutes Asleep",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesAwake",
        name=f"{FITBIT_USER} Sleep Minutes Awake",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/minutesToFallAsleep",
        name=f"{FITBIT_USER} Sleep Minutes to Fall Asleep",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:sleep",
    ),
    FitbitSensorEntityDescription(
        key="sleep/startTime",
        name=f"{FITBIT_USER} Sleep Start Time",
        unit_type=None,
        icon="mdi:clock",
    ),
    FitbitSensorEntityDescription(
        key="sleep/timeInBed",
        name=f"{FITBIT_USER} Sleep Time in Bed",
        unit_type=UnitOfTime.MINUTES,
        icon="mdi:hotel",
    ),
)

FITBIT_RESOURCE_BATTERY = FitbitSensorEntityDescription(
    key="devices/battery",
    name=f"{FITBIT_USER} Battery",
    unit_type=None,
    icon="mdi:battery",
)

FITBIT_RESOURCES_KEYS: Final[list[str]] = [
    desc.key for desc in (*FITBIT_RESOURCES_LIST, FITBIT_RESOURCE_BATTERY)
]

FITBIT_MEASUREMENTS: Final[dict[str, dict[str, str]]] = {
    "en_US": {
        ATTR_DURATION: UnitOfTime.MILLISECONDS,
        ATTR_DISTANCE: "mi",
        ATTR_ELEVATION: UnitOfLength.FEET,
        ATTR_HEIGHT: "in",
        ATTR_WEIGHT: "lbs",
        ATTR_BODY: "in",
        ATTR_LIQUIDS: "fl. oz.",
        ATTR_BLOOD_GLUCOSE: f"{UnitOfMass.MILLIGRAMS}/dL",
        ATTR_BATTERY: "",
    },
    "en_GB": {
        ATTR_DURATION: UnitOfTime.MILLISECONDS,
        ATTR_DISTANCE: "kilometers",
        ATTR_ELEVATION: "meters",
        ATTR_HEIGHT: "centimeters",
        ATTR_WEIGHT: "stone",
        ATTR_BODY: "centimeters",
        ATTR_LIQUIDS: "milliliters",
        ATTR_BLOOD_GLUCOSE: "mmol/L",
        ATTR_BATTERY: "",
    },
    "metric": {
        ATTR_DURATION: UnitOfTime.MILLISECONDS,
        ATTR_DISTANCE: "kilometers",
        ATTR_ELEVATION: "meters",
        ATTR_HEIGHT: "centimeters",
        ATTR_WEIGHT: UnitOfMass.KILOGRAMS,
        ATTR_BODY: "centimeters",
        ATTR_LIQUIDS: "milliliters",
        ATTR_BLOOD_GLUCOSE: "mmol/L",
        ATTR_BATTERY: "",
    },
}

BATTERY_LEVELS: Final[dict[str, int]] = {
    "High": 100,
    "Medium": 50,
    "Low": 20,
    "Empty": 0,
}
