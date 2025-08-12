import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import datetime as dt

import os

x = os.getcwd()

date = dt.date.today()

