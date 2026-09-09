# Smart-Invoice-Processor

## Overview
The Smart-Invoice-Processor is a microservice designed to ingest PDF invoices, extract key-value pairs (such as vendor, totals, and line items) using local vision LLMs, and push structured JSON payloads into a downstream accounting database. It provides an API interface for bulk processing and uses a task queue to throttle concurrent document analysis.

## Execution Entry Points
To run or analyze the system architecture, refer to these primary file paths:
- System runtime initialized via: `app.py`
- Background worker loops managed by: `src/worker.py`

## Metadata & Compliance
- **Service Owner**: Financial Automation Group
- **Maintainers**: John Doe (john.doe@example.com), Jane Smith (jane.smith@example.com)
- **Deployment Tier**: Production-Tier1
