import api_connector_splunk_declare

from splunktaucclib.rest_handler.endpoint import (
    field,
    validator,
    RestModel,
    MultipleModel,
)
from splunktaucclib.rest_handler import admin_external, util
from splunk_aoblib.rest_migration import ConfigMigrationHandler

util.remove_http_proxy_env_vars()

fields_logging = [
    field.RestField(
        'loglevel',
        required=False,
        encrypted=False,
        default='INFO',
        validator=None)
]
model_logging = RestModel(fields_logging, name='logging')

fields_additional_parameters = [
    field.RestField(
        'cybergrx_api',
        required=False,
        encrypted=False,
        default='https://api.cybergrx.com',
        validator=validator.String(
            min_len=0,
            max_len=8192,
        ))
]
model_additional_parameters = RestModel(
    fields_additional_parameters, name='additional_parameters')

endpoint = MultipleModel(
    'api_connector_splunk_settings',
    models=[model_logging, model_additional_parameters],
)

if __name__ == '__main__':
    admin_external.handle(
        endpoint,
        handler=ConfigMigrationHandler,
    )
