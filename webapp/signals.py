"""Attach signals to this app's models."""
# -*- coding: utf-8 -*-
import json

import channels.layers
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from .Entities.Conversions import Conversions

from .BL.CurrenciesBL import CurrenciesBL as cbl
from .Models.Currency import Currency


def send_message(event):
    message = event['text']
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.send)(text_data=json.dumps(
        message
    ))


@receiver(post_save, sender=Conversions)
def conversion_listeners(sender, instance, **kwargs):
    
    group_name = 'exchange-{}'.format(instance.user_id)

    fromCrncy =  Currency()
    fromCrncy.Id =  instance.from_id
    fromCrncy.userId =  instance.user_id

    toCrncy =  Currency()
    toCrncy.Id =  instance.to_id
    toCrncy.userId =  instance.user_id
    message = None

    if kwargs['created']:
        message = {
            'cnvOps': 'add',
            'cnvId': instance.id,
            'fromShortName': cbl.selectCurrency(fromCrncy).shortName,
            'toShortName': cbl.selectCurrency(toCrncy).shortName,
            'cnvRate': instance.rate
        }
    else:
        message = {
            'cnvOps': 'update',
            'cnvId': instance.id,
            'fromShortName': cbl.selectCurrency(fromCrncy).shortName,
            'toShortName': cbl.selectCurrency(toCrncy).shortName,
            'cnvRate': instance.rate
        }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_message',
            'text': message
        }
    )

@receiver(post_delete, sender=Conversions)
def remove_conversion_listeners(sender, instance, **kwargs):

    group_name = 'exchange-{}'.format(instance.user_id)

    message = {
        'cnvOps': 'delete',
        'cnvId': instance.id
    }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_message',
            'text': message
        }
    )