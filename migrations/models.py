from tortoise import fields
from tortoise.models import Model


class Metadata(Model):
    version = fields.IntField()


class Server(Model):
    id = fields.IntField(pk=True)


class ActivityTrackingSettings(Model):
    id = fields.IntField(pk=True)
    server_id = fields.ForeignKeyField('models.Server', related_name='activity_tracking_settings')
    time_period = fields.IntField()
    role_id = fields.IntField()
    message_count = fields.IntField()


class ActivityTrackingChannels(Model):
    channel = fields.IntField()
    activity_tracking = fields.ForeignKeyField('models.ActivityTrackingSettings', related_name='activity_tracking_channels')


class MessageLog(Model):
    channel_id = fields.IntField()
    user_id = fields.IntField()
    time = fields.IntField()
    server = fields.ForeignKeyField('models.Server', related_name='message_logs')


class WelcomeConfigSettings(Model):
    server_id = fields.IntField(pk=True)
    detection_word = fields.CharField(max_length=255)
    role_id = fields.IntField()
    welcome_channel_id = fields.IntField()