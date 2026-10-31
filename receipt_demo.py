"""Clean-room educational agent receipt metadata gate (31 October 2026).

NO authentication, certification, enforcement, cryptographic verification,
physical observation, AI safety claim or evidence of real action execution.
"""
import json
import sys

REQUIRED = ('receipt_id', 'claim_id', 'agent_id', 'session_id', 'resource',
            'action', 'policy_version', 'status', 'observer_id')
STATUS = ('READY_FOR_INSPECTION', 'INCOMPLETE_METADATA', 'INCONSISTENT_METADATA')


def inspect(claim, receipt):
    """Check metadata completeness and declared correspondence only.

    The claim is an ordinary dictionary with keys claim_id, agent_id, session_id,
    resource, action and policy_version. This is NOT a verifier of real events.
    """
    if not isinstance(claim, dict) or not isinstance(receipt, dict):
        return {'status': STATUS[1], 'reasons': ['record_not_object']}
    required_claim = ('claim_id', 'agent_id', 'session_id', 'resource',
                      'action', 'policy_version')
    missing_claim = [f'claim.{k}' for k in required_claim
                     if not isinstance(claim.get(k), str) or not claim[k].strip()]
    missing = missing_claim + [f'receipt.{k}' for k in REQUIRED
                             if not isinstance(receipt.get(k), str)
                             or not receipt[k].strip()]
    if missing:
        return {'status': STATUS[1], 'reasons': missing}
    mismatch = [f'mismatch:{k}' for k in required_claim
                if receipt[k] != claim[k]]
    if receipt['status'] not in ('reported_success', 'reported_failure', 'unknown'):
        mismatch.append('invalid_reported_status')
    if receipt['status'] == 'unknown':
        # An unknown report must never become evidence of actual success.
        mismatch.append('unverified_outcome')
    if mismatch:
        return {'status': STATUS[2], 'reasons': mismatch}
    return {'status': STATUS[0], 'reasons': [
        'metadata_only_not_evidence_of_execution_or_authority']}


def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python receipt_demo.py sample_receipts.json')
    with open(sys.argv[1], encoding='utf-8') as f:
        data = json.load(f)
    for item in data['cases']:
        print(item['name'], json.dumps(inspect(item['claim'], item['receipt']),
                                       sort_keys=True))

if __name__ == '__main__':
    main()
