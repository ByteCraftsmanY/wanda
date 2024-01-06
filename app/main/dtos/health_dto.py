from flask_restx import Namespace, fields


class HealthDto:
    api = Namespace('health', description='app health')
