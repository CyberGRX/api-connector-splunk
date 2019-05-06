# CyberGRX Splunk API Connector

If you are taking a look at configuring the CyberGRX Splunk Connector, please take a look at the [Install Guide (How To)](./HOW-TO.md).

**Please Note** this connector has been formally tested against Splunk Enterprise version `7.2.4`.

This addon enables Splunk to retrieve data from the CyberGRX customer API.  You will need a valid API token to gain access to the API and begin pulling data into Splunk.  Once data is resident in your splunk system you may enrich that data and setup alarms and custom dashboards.  The CyberGRX API is versioned and will maintain backwards compatibility.

This is an addon that was built using the Splunk Add-on Builder.
- App version: 2.2.0
- App build: 12

# Development Workflows
- Make sure you have the pre-commit / pre-push hooks installed
 - If you do not have pre-commit: `brew install pre-commit`
 - Install hooks: `pre-commit install && pre-commit install --install-hooks && pre-commit install --hook-type pre-push`
- Use the app-builder in Splunk to configure the application.
- Export that application to the working directory when your changes are complete
- `make prep`
- `make build`
- Go to validate and package, check report and generate a SPL
- `make release`
- Tag a release in github and upload artifacts after releasing on splunk base
