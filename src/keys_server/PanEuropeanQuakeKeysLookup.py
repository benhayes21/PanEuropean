import itertools
import json

from oasislmf.utils import (
    coverages,
    peril,
)   
from oasislmf.utils.status import (
    OASIS_KEYS_SC,
    OASIS_KEYS_FL,
    OASIS_KEYS_NM,
    OASIS_KEYS_STATUS
)
from oasislmf.model_preparation.lookup import OasisBaseKeysLookup

class PanEuropeanQuakeKeysLookup(OasisBaseKeysLookup):

    def __init__(self, 
            keys_data_directory=None,
            supplier=None,
            model_name=None,
            model_version=None):

        self._peril_ids = [
            peril.PERILS['earthquake']['id'],
        ]

        self._coverage_types = [
            coverages.COVERAGE_TYPES['buildings']['id']
            ,coverages.COVERAGE_TYPES['contents']['id']
            ,coverages.COVERAGE_TYPES['bi']['id']
        ]


    def process_location(self, loc, peril_id, coverage_type):
        
        status = OASIS_KEYS_SC
        message = "OK"
        data={
            "area_peril_id": loc['locnumber'],
            "vulnerability_id": loc['constructioncode'],
            "yearbuilt": loc['yearbuilt'],
            "numberofstoreys": loc['numberofstoreys'],
            "latitude": loc['latitude'],
            "longitude": loc['longitude'],
            "occupancycode": loc['occupancycode'],
            "countrycode": loc['countrycode'],
            "postalcode": loc['postalcode'],
            "coverage_type": coverage_type
        }

        
        return {
            'loc_id': loc['loc_id'],
            'locnumber': loc['locnumber'],
            'peril_id': peril_id,
            'coverage_type': coverage_type,
            'model_data': json.dumps(data),
            'status': status,
            'message': message
        }

    def process_locations(self, locs):
        locs.columns = locs.columns.str.lower()
        if 'loc_id' not in locs:
            locs['loc_id'] = get_ids(locs, ['portnumber', 'accnumber', 'locnumber'])

        locs_seq = (loc for _, loc in locs.iterrows())
        for loc, peril_id, coverage_type in \
                itertools.product(locs_seq, self._peril_ids, self._coverage_types):
            yield self.process_location(loc, peril_id, coverage_type)
            
