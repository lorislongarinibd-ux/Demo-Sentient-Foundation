import copy
import unittest
from receipt_demo import inspect

CLAIM = dict(claim_id='c-1', agent_id='agent-A', session_id='s-1',
             resource='doc:test', action='write', policy_version='p-2')
RECEIPT = dict(CLAIM, receipt_id='r-1', status='reported_success',
               observer_id='observer-B')

class ReceiptTests(unittest.TestCase):
    def test_ready_is_metadata_only(self):
        result = inspect(CLAIM, RECEIPT)
        self.assertEqual(result['status'], 'READY_FOR_INSPECTION')
        self.assertIn('metadata_only', result['reasons'][0])
    def test_missing_fields(self):
        for key in RECEIPT:
            with self.subTest(key=key):
                r=copy.deepcopy(RECEIPT); r.pop(key)
                self.assertEqual(inspect(CLAIM,r)['status'],'INCOMPLETE_METADATA')
    def test_blank_fields(self):
        for key in RECEIPT:
            with self.subTest(key=key):
                r=copy.deepcopy(RECEIPT);r[key]='  '
                self.assertEqual(inspect(CLAIM,r)['status'],'INCOMPLETE_METADATA')
    def test_mismatch(self):
        for key in CLAIM:
            with self.subTest(key=key):
                r=copy.deepcopy(RECEIPT);r[key]='other'
                self.assertEqual(inspect(CLAIM,r)['status'],'INCONSISTENT_METADATA')
    def test_missing_claim(self):
        c=copy.deepcopy(CLAIM);c.pop('session_id')
        self.assertEqual(inspect(c,RECEIPT)['status'],'INCOMPLETE_METADATA')
    def test_nonobject(self):
        self.assertEqual(inspect(CLAIM,[])['status'],'INCOMPLETE_METADATA')
    def test_reported_unknown(self):
        r=copy.deepcopy(RECEIPT);r['status']='unknown'
        self.assertEqual(inspect(CLAIM,r)['status'],'INCONSISTENT_METADATA')
    def test_unexpected_status(self):
        r=copy.deepcopy(RECEIPT);r['status']='success_certified'
        self.assertEqual(inspect(CLAIM,r)['status'],'INCONSISTENT_METADATA')
    def test_empty_observer(self):
        r=copy.deepcopy(RECEIPT);r['observer_id']=''
        self.assertEqual(inspect(CLAIM,r)['status'],'INCOMPLETE_METADATA')

if __name__=='__main__':unittest.main()
