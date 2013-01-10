# -*- coding: utf-8 -*-
"""
List of Galician provinces for use as select choices.
"""
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _


PROVINCE_CHOICES = (
    ('15', _('A Coruña')),
    ('27', _('Lugo')),
    ('32', _('Ourense')),
    ('36', _('Pontevedra')),
)


PROVINCES_WITH_MUNICIPALITIES = {
    '15': [
        '15001',
        '15002',
        '15003',
        '15004',
        '15005',
        '15006',
        '15007',
        '15008',
        '15009',
        '15010',
        '15011',
        '15012',
        '15013',
        '15014',
        '15015',
        '15016',
        '15017',
        '15018',
        '15019',
        '15901',
        '15020',
        '15021',
        '15022',
        '15023',
        '15024',
        '15025',
        '15026',
        '15027',
        '15028',
        '15029',
        '15030',
        '15031',
        '15032',
        '15033',
        '15034',
        '15035',
        '15036',
        '15037',
        '15038',
        '15039',
        '15041',
        '15040',
        '15042',
        '15043',
        '15045',
        '15044',
        '15046',
        '15047',
        '15048',
        '15049',
        '15050',
        '15051',
        '15053',
        '15052',
        '15054',
        '15055',
        '15056',
        '15057',
        '15058',
        '15059',
        '15060',
        '15061',
        '15062',
        '15063',
        '15064',
        '15065',
        '15066',
        '15067',
        '15068',
        '15069',
        '15070',
        '15071',
        '15072',
        '15073',
        '15074',
        '15075',
        '15076',
        '15077',
        '15078',
        '15079',
        '15080',
        '15081',
        '15082',
        '15083',
        '15084',
        '15085',
        '15086',
        '15088',
        '15087',
        '15089',
        '15091',
        '15090',
        '15092',
        '15093',
    ],
    '27': [
        '27001',
        '27002',
        '27003',
        '27004',
        '27901',
        '27005',
        '27006',
        '27007',
        '27902',
        '27008',
        '27009',
        '27010',
        '27011',
        '27012',
        '27013',
        '27016',
        '27014',
        '27015',
        '27017',
        '27018',
        '27019',
        '27020',
        '27022',
        '27023',
        '27024',
        '27027',
        '27028',
        '27026',
        '27029',
        '27030',
        '27031',
        '27032',
        '27033',
        '27034',
        '27035',
        '27037',
        '27038',
        '27039',
        '27040',
        '27041',
        '27042',
        '27044',
        '27045',
        '27047',
        '27046',
        '27048',
        '27049',
        '27043',
        '27050',
        '27051',
        '27052',
        '27053',
        '27054',
        '27056',
        '27055',
        '27057',
        '27058',
        '27059',
        '27060',
        '27061',
        '27062',
        '27063',
        '27064',
        '27065',
        '27066',
        '27021',
        '27025',
    ],
    '32': [
        '32001',
        '32002',
        '32003',
        '32004',
        '32005',
        '32006',
        '32008',
        '32009',
        '32007',
        '32010',
        '32011',
        '32012',
        '32013',
        '32014',
        '32015',
        '32016',
        '32018',
        '32017',
        '32019',
        '32020',
        '32022',
        '32021',
        '32023',
        '32024',
        '32025',
        '32029',
        '32026',
        '32027',
        '32028',
        '32030',
        '32031',
        '32033',
        '32034',
        '32035',
        '32038',
        '32039',
        '32040',
        '32041',
        '32042',
        '32043',
        '32044',
        '32045',
        '32046',
        '32047',
        '32048',
        '32049',
        '32050',
        '32051',
        '32052',
        '32054',
        '32053',
        '32055',
        '32056',
        '32057',
        '32058',
        '32059',
        '32060',
        '32061',
        '32063',
        '32064',
        '32062',
        '32065',
        '32066',
        '32067',
        '32068',
        '32069',
        '32071',
        '32073',
        '32072',
        '32074',
        '32075',
        '32076',
        '32070',
        '32077',
        '32078',
        '32079',
        '32080',
        '32081',
        '32082',
        '32083',
        '32084',
        '32085',
        '32086',
        '32088',
        '32087',
        '32089',
        '32090',
        '32091',
        '32092',
        '32032',
        '32036',
        '32037',
    ],
    '36': [
        '36020',
        '36001',
        '36003',
        '36002',
        '36004',
        '36005',
        '36006',
        '36007',
        '36008',
        '36010',
        '36009',
        '36011',
        '36012',
        '36013',
        '36014',
        '36015',
        '36016',
        '36017',
        '36018',
        '36019',
        '36021',
        '36022',
        '36023',
        '36901',
        '36024',
        '36025',
        '36026',
        '36027',
        '36028',
        '36029',
        '36030',
        '36031',
        '36032',
        '36033',
        '36034',
        '36035',
        '36036',
        '36037',
        '36041',
        '36043',
        '36042',
        '36044',
        '36038',
        '36039',
        '36040',
        '36045',
        '36046',
        '36047',
        '36048',
        '36049',
        '36050',
        '36051',
        '36052',
        '36053',
        '36054',
        '36055',
        '36056',
        '36057',
        '36059',
        '36058',
        '36060',
        '36061',
    ],
}
