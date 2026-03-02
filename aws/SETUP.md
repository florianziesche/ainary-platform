# AWS Setup — mia-local

## Account
- Account ID: `350655711792`
- User: `mia-local`
- Region: `eu-central-1` (default)

## Services
| Service | Use | Resource Pattern |
|---------|-----|-----------------|
| S3 | Shared files, assets | `ainary-shared-*`, `ainary-mia-*` |
| DynamoDB | Echtzeit-Comms-Tabelle | `ainary-*` |
| SES | Emails von florian@ainaryventures.com | Domain: ainaryventures.com |
| Polly | TTS | * |
| Bedrock | Claude etc. | * |
| Transcribe | Audio → Text | * |

## SES Setup
1. Domain `ainaryventures.com` verifizieren (TXT + 3x DKIM CNAME) ✅ DNS gesetzt
2. Sender: `florian@ainaryventures.com`
3. Region: `eu-central-1`

## IAM Policy
Die Permissions Boundary muss `iam-policy-mia.json` enthalten.

### Anleitung (AWS Console):
1. IAM → Users → mia-local → Permissions boundary
2. "Set boundary" → Create policy → JSON → Inhalt von `iam-policy-mia.json` einfügen
3. Name: `MiaLocalBoundary`
4. Speichern

Alternativ CLI (braucht Admin-Rechte):
```bash
aws iam create-policy --policy-name MiaLocalPolicy --policy-document file://aws/iam-policy-mia.json
aws iam attach-user-policy --user-name mia-local --policy-arn arn:aws:iam::350655711792:policy/MiaLocalPolicy
aws iam put-user-permissions-boundary --user-name mia-local --permissions-boundary arn:aws:iam::350655711792:policy/MiaLocalPolicy
```

## Credentials
Konfiguriert via `aws configure`. Nicht im Repo speichern.
