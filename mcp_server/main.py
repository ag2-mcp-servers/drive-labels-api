# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T02:04:00+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Query

from models import (
    Alt,
    FieldXgafv,
    GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest,
    GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest,
    GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse,
    GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest,
    GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse,
    GoogleAppsDriveLabelsV2betaDisableLabelRequest,
    GoogleAppsDriveLabelsV2betaEnableLabelRequest,
    GoogleAppsDriveLabelsV2betaLabel,
    GoogleAppsDriveLabelsV2betaLabelLimits,
    GoogleAppsDriveLabelsV2betaLabelPermission,
    GoogleAppsDriveLabelsV2betaListLabelLocksResponse,
    GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse,
    GoogleAppsDriveLabelsV2betaListLabelsResponse,
    GoogleAppsDriveLabelsV2betaPublishLabelRequest,
    GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest,
    GoogleAppsDriveLabelsV2betaUserCapabilities,
    GoogleProtobufEmpty,
    MinimumRole,
    View,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='An API for managing Drive Labels',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='Drive Labels API',
    version='v2beta',
    servers=[{'url': 'https://drivelabels.googleapis.com/'}],
)


@app.get(
    '/v2beta/labels',
    description=""" List labels. """,
    tags=[
        'drivelabel_management',
        'drivelabel_revision_permissions',
        'drivelabel_user_capabilities',
        'drivelabel_system_limits',
        'drivelabel_change_tracking',
        'drivelabel_revision_lock_management',
    ],
)
def drivelabels_labels_list(
    customer: Optional[str] = None,
    language_code: Optional[str] = Query(None, alias='languageCode'),
    minimum_role: Optional[MinimumRole] = Query(None, alias='minimumRole'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    published_only: Optional[bool] = Query(None, alias='publishedOnly'),
    use_admin_access: Optional[bool] = Query(None, alias='useAdminAccess'),
    view: Optional[View] = None,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/labels',
    description=""" Creates a new Label. """,
    tags=[
        'drivelabel_management',
        'drivelabel_revision_permissions',
        'drivelabel_user_capabilities',
        'drivelabel_system_limits',
        'drivelabel_change_tracking',
        'drivelabel_revision_lock_management',
    ],
)
def drivelabels_labels_create(
    language_code: Optional[str] = Query(None, alias='languageCode'),
    use_admin_access: Optional[bool] = Query(None, alias='useAdminAccess'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaLabel = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v2beta/limits/label',
    description=""" Get the constraints on the structure of a Label; such as, the maximum number of Fields allowed and maximum length of the label title. """,
    tags=['drivelabel_user_capabilities'],
)
def drivelabels_limits_get_label(
    name: Optional[str] = None,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v2beta/{name}',
    description=""" Deletes a Label's permission. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing. """,
    tags=['drivelabel_revision_permissions', 'drivelabel_management'],
)
def drivelabels_labels_revisions_permissions_delete(
    name: str,
    use_admin_access: Optional[bool] = Query(None, alias='useAdminAccess'),
    write_control_required_revision_id: Optional[str] = Query(
        None, alias='writeControl.requiredRevisionId'
    ),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v2beta/{name}',
    description=""" Gets the user capabilities. """,
    tags=[
        'drivelabel_management',
        'drivelabel_revision_permissions',
        'drivelabel_user_capabilities',
        'drivelabel_system_limits',
        'drivelabel_change_tracking',
        'drivelabel_revision_lock_management',
    ],
)
def drivelabels_users_get_capabilities(
    name: str,
    customer: Optional[str] = None,
    use_admin_access: Optional[bool] = Query(None, alias='useAdminAccess'),
    view: Optional[View] = None,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{name}:delta',
    description=""" Updates a single Label by applying a set of update requests resulting in a new draft revision. The batch update is all-or-nothing: If any of the update requests are invalid, no changes are applied. The resulting draft revision must be published before the changes may be used with Drive Items. """,
    tags=['drivelabel_management', 'drivelabel_change_tracking'],
)
def drivelabels_labels_delta(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{name}:disable',
    description=""" Disable a published Label. Disabling a Label will result in a new disabled published revision based on the current published revision. If there is a draft revision, a new disabled draft revision will be created based on the latest draft revision. Older draft revisions will be deleted. Once disabled, a label may be deleted with `DeleteLabel`. """,
    tags=['drivelabel_management'],
)
def drivelabels_labels_disable(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaDisableLabelRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{name}:enable',
    description=""" Enable a disabled Label and restore it to its published state. This will result in a new published revision based on the current disabled published revision. If there is an existing disabled draft revision, a new revision will be created based on that draft and will be enabled. """,
    tags=['drivelabel_management'],
)
def drivelabels_labels_enable(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaEnableLabelRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{name}:publish',
    description=""" Publish all draft changes to the Label. Once published, the Label may not return to its draft state. See `google.apps.drive.labels.v2.Lifecycle` for more information. Publishing a Label will result in a new published revision. All previous draft revisions will be deleted. Previous published revisions will be kept but are subject to automated deletion as needed. Once published, some changes are no longer permitted. Generally, any change that would invalidate or cause new restrictions on existing metadata related to the Label will be rejected. For example, the following changes to a Label will be rejected after the Label is published: * The label cannot be directly deleted. It must be disabled first, then deleted. * Field.FieldType cannot be changed. * Changes to Field validation options cannot reject something that was previously accepted. * Reducing the max entries. """,
    tags=['drivelabel_management'],
)
def drivelabels_labels_publish(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaPublishLabelRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{name}:updateLabelCopyMode',
    description=""" Updates a Label's `CopyMode`. Changes to this policy are not revisioned, do not require publishing, and take effect immediately. """,
    tags=['drivelabel_management'],
)
def drivelabels_labels_update_label_copy_mode(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v2beta/{parent}/locks',
    description=""" Lists the LabelLocks on a Label. """,
    tags=[
        'drivelabel_management',
        'drivelabel_revision_permissions',
        'drivelabel_user_capabilities',
        'drivelabel_system_limits',
        'drivelabel_change_tracking',
        'drivelabel_revision_lock_management',
    ],
)
def drivelabels_labels_revisions_locks_list(
    parent: str,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v2beta/{parent}/permissions',
    description=""" Lists a Label's permissions. """,
    tags=[
        'drivelabel_management',
        'drivelabel_revision_permissions',
        'drivelabel_user_capabilities',
        'drivelabel_system_limits',
        'drivelabel_change_tracking',
        'drivelabel_revision_lock_management',
    ],
)
def drivelabels_labels_revisions_permissions_list(
    parent: str,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    use_admin_access: Optional[bool] = Query(None, alias='useAdminAccess'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v2beta/{parent}/permissions',
    description=""" Updates a Label's permissions. If a permission for the indicated principal doesn't exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing. """,
    tags=['drivelabel_revision_permissions', 'drivelabel_management'],
)
def drivelabels_labels_revisions_update_permissions(
    parent: str,
    use_admin_access: Optional[bool] = Query(None, alias='useAdminAccess'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaLabelPermission = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{parent}/permissions',
    description=""" Updates a Label's permissions. If a permission for the indicated principal doesn't exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing. """,
    tags=['drivelabel_management', 'drivelabel_revision_permissions'],
)
def drivelabels_labels_revisions_permissions_create(
    parent: str,
    use_admin_access: Optional[bool] = Query(None, alias='useAdminAccess'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaLabelPermission = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{parent}/permissions:batchDelete',
    description=""" Deletes Label permissions. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing. """,
    tags=['drivelabel_revision_permissions'],
)
def drivelabels_labels_revisions_permissions_batch_delete(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v2beta/{parent}/permissions:batchUpdate',
    description=""" Updates Label permissions. If a permission for the indicated principal doesn't exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing. """,
    tags=['drivelabel_revision_permissions', 'drivelabel_management'],
)
def drivelabels_labels_revisions_permissions_batch_update(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
