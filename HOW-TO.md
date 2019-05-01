# Configuration of the splunk connector
There are 2 steps to successful Splunk integration.  
1. Retrieve a CyberGRX API Token
1. Install and configure the Splunk Connector

## Install the Splunk Connector
Download the latest release and add an addon into your splunk install.  This app has been tested against Splunk Enterprise `7.4.2`

## Configure the Splunk Connector
Configuring the Splunk Connector is pretty straight forward.  A successful integration will require a CyberGRX API Token, so if you dont have that go get one now.

The workflow is pretty simple:
 - Enter the CyberGRX app
 - Create 3 new inputs, one for each primary data source, you can re-use the API Token for each data source.
 - Make sure you use the full token copied from the CyberGRX user interface.
 - An area to be careful is the proper configuration of a collection interval, the connector polls the full third party ecosystem, recommendations are provided in the table below.
 - Thats it, you should start to see events showing up in your dashboard.

 ### Recommended collection intervals for each data type
| Data Type                    | Collection Interval (seconds) | Hours  |
| ---------------------------- |:-----------------------------:| ------:|
| ThirdParty_CyberGRX          | 43200                         | 12     |
| AssessmentScore_GRX          | 172800                        | 48     |
| GapsAndRemediations_CyberGRX | 172800                        | 48     |

### CyberGRX Application Configuration Workflow
![cybergrx-input-configuration]
![add-data-source]
![configured-all-data-sources]

## Retrieve a CyberGRX API Token
You must have an active CyberGRX account that has the ability to manage users. 

The workflow is pretty simple:
 - Enter `Manage my company user accounts` using the top right navigational element
 - Click the tab to `Manage Access Tokens`
 - Click the button to `Add a new token`
 - Accept the promt creating a token
 - Show the secret and copy it, this is the only time that this token will be available over the API!
 - Close the dialog and configure your token in the Splunk connector

 ### CyberGRX Management Workflow
 ![enter-user-management]
 ![add-a-token]
 ![confirm-new-token]
 ![view-token]
 ![copy-secret]


[enter-user-management]: /docs/enter-user-management.png "Click top right icon and enter `Manage my company user accounts`"

[add-a-token]: /docs/add-a-token.png "Click the tab to `Manage Access Tokens` and Add a new token"

[confirm-new-token]: /docs/confirm-new-token.png "Accept the promt creating a token"

[view-token]: /docs/make-sure-you-view.png "Before leaving view the token secret"

[copy-secret]: /docs/copy-secret.png "Show the secret and copy it, this is the only time that this token will be available over the API!"

[cybergrx-input-configuration]: /docs/cybergrx-input-configuration.png "Manage the CyberGRX app"

[add-data-source]: /docs/add-data-source.png "Create a new input"

[configured-all-data-sources]: /docs/configured-all-data-sources.png "Fully configured app"