from flask_sqlalchemy import SQLAlchemy

from .model import *
from veri.model.TemelVeriSinifi import TemelVeriSinifi

db = SQLAlchemy(model_class=TemelVeriSinifi)