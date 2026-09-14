\# HERMES WORKSPACE TOOLS \& SKILLS MANIFEST



\## ENVIRONMENT \& RUNTIME

\- Python Executable: `%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe`

\- Working Directory: `C:\\Users\\saifh\\agent\_workspace`

\- Primary Database: `C:\\Users\\saifh\\agent\_workspace\\abaya\_inventory.db`



\## STRICT EXECUTION RULES FOR HERMES

1\. NEVER write new Python code for tasks that match the tools listed below.

2\. ALWAYS invoke the corresponding pre-built script directly via Windows Terminal (cmd.exe / PowerShell).

3\. Conserve LLM reasoning tokens and prevent API Rate Limits (429) by executing commands directly.



\---



\## REGISTERED SKILLS CATALOG



\### Tool 1: Master Operations Pipeline (Orchestrator)

\- \*\*File:\*\* `hermes\_master\_runner.py`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" C:\\Users\\saifh\\agent\_workspace\\hermes\_master\_runner.py`

\- \*\*Options:\*\* Add `--dry-run` to test without sending external alerts.

\- \*\*Function:\*\* Checks SQLite inventory, extracts products with stock <= 5, generates restock PDF, and dispatches a live alert to the Telegram channel.



\### Tool 2: Inventory \& Database Engine

\- \*\*File:\*\* `test\_database.py`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" C:\\Users\\saifh\\agent\_workspace\\test\_database.py`

\- \*\*Function:\*\* Queries SQLite catalog, evaluates profit margins per abaya, and detects low-stock items.



\### Tool 3: PDF Invoice \& Packing Slip Generator

\- \*\*File:\*\* `test\_invoice\_engine.py`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" C:\\Users\\saifh\\agent\_workspace\\test\_invoice\_engine.py`

\- \*\*Function:\*\* Compiles structured commercial invoices and packing slips into printable A4 PDFs.



\### Tool 4: Web Scraping \& Market Monitor

\- \*\*File:\*\* `test\_scraper.py`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" C:\\Users\\saifh\\agent\_workspace\\test\_scraper.py`

\- \*\*Function:\*\* Launches headless Microsoft Edge to scrape competitor pricing and product data silently.



\### Tool 5: Image Resolution \& Catalog Optimizer

\- \*\*File:\*\* `test\_image\_engine.py`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" C:\\Users\\saifh\\agent\_workspace\\test\_image\_engine.py`

\- \*\*Function:\*\* Crops, resizes (1080x1350), and formats product imagery for Instagram and e-commerce stores.



\### Tool 6: Telegram Mobile Alert Dispatcher

\- \*\*File:\*\* `telegram\_notifier.py`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" C:\\Users\\saifh\\agent\_workspace\\telegram\_notifier.py`

\- \*\*Function:\*\* Sends real-time operational notifications and alerts to Saif's Telegram phone app.



\### Tool 7: Static Code Linter

\- \*\*File:\*\* `flake8`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\flake8.exe" <path\_to\_file>`

\- \*\*Function:\*\* Verifies PEP8 compliance and detects indentation or syntax bugs prior to executing new scripts.



\### Tool 8: Task Scheduler Daemon

\- \*\*File:\*\* `test\_scheduler.py`

\- \*\*Command:\*\* `"%LOCALAPPDATA%\\hermes\\hermes-agent\\venv\\Scripts\\python.exe" C:\\Users\\saifh\\agent\_workspace\\test\_scheduler.py`

\- \*\*Function:\*\* Executes cyclical tasks natively in user-space Python without system freezing.

