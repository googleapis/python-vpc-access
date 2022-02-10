# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.vpcaccess_v1.services.vpc_access_service import pagers
from google.cloud.vpcaccess_v1.types import vpc_access
from google.protobuf import empty_pb2  # type: ignore
from .transports.base import VpcAccessServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import VpcAccessServiceGrpcAsyncIOTransport
from .client import VpcAccessServiceClient


class VpcAccessServiceAsyncClient:
    """Serverless VPC Access API allows users to create and manage
    connectors for App Engine, Cloud Functions and Cloud Run to have
    internal connections to Virtual Private Cloud networks.
    """

    _client: VpcAccessServiceClient

    DEFAULT_ENDPOINT = VpcAccessServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = VpcAccessServiceClient.DEFAULT_MTLS_ENDPOINT

    connector_path = staticmethod(VpcAccessServiceClient.connector_path)
    parse_connector_path = staticmethod(VpcAccessServiceClient.parse_connector_path)
    common_billing_account_path = staticmethod(
        VpcAccessServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        VpcAccessServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(VpcAccessServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        VpcAccessServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        VpcAccessServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        VpcAccessServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(VpcAccessServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        VpcAccessServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(VpcAccessServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        VpcAccessServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            VpcAccessServiceAsyncClient: The constructed client.
        """
        return VpcAccessServiceClient.from_service_account_info.__func__(VpcAccessServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            VpcAccessServiceAsyncClient: The constructed client.
        """
        return VpcAccessServiceClient.from_service_account_file.__func__(VpcAccessServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return VpcAccessServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> VpcAccessServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            VpcAccessServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(VpcAccessServiceClient).get_transport_class, type(VpcAccessServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, VpcAccessServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the vpc access service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.VpcAccessServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = VpcAccessServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_connector(
        self,
        request: Union[vpc_access.CreateConnectorRequest, dict] = None,
        *,
        parent: str = None,
        connector_id: str = None,
        connector: vpc_access.Connector = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a Serverless VPC Access connector, returns an
        operation.


        .. code-block::

            from google.cloud import vpcaccess_v1

            def sample_create_connector():
                # Create a client
                client = vpcaccess_v1.VpcAccessServiceClient()

                # Initialize request argument(s)
                request = vpcaccess_v1.CreateConnectorRequest(
                    parent="parent_value",
                    connector_id="connector_id_value",
                )

                # Make the request
                operation = client.create_connector(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vpcaccess_v1.types.CreateConnectorRequest, dict]):
                The request object. Request for creating a Serverless
                VPC Access connector.
            parent (:class:`str`):
                Required. The project and location in which the
                configuration should be created, specified in the format
                ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            connector_id (:class:`str`):
                Required. The ID to use for this
                connector.

                This corresponds to the ``connector_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            connector (:class:`google.cloud.vpcaccess_v1.types.Connector`):
                Required. Resource to create.
                This corresponds to the ``connector`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.vpcaccess_v1.types.Connector`
                Definition of a Serverless VPC Access connector.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, connector_id, connector])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = vpc_access.CreateConnectorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if connector_id is not None:
            request.connector_id = connector_id
        if connector is not None:
            request.connector = connector

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_connector,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            vpc_access.Connector,
            metadata_type=vpc_access.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_connector(
        self,
        request: Union[vpc_access.GetConnectorRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> vpc_access.Connector:
        r"""Gets a Serverless VPC Access connector. Returns NOT_FOUND if the
        resource does not exist.


        .. code-block::

            from google.cloud import vpcaccess_v1

            def sample_get_connector():
                # Create a client
                client = vpcaccess_v1.VpcAccessServiceClient()

                # Initialize request argument(s)
                request = vpcaccess_v1.GetConnectorRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_connector(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vpcaccess_v1.types.GetConnectorRequest, dict]):
                The request object. Request for getting a Serverless VPC
                Access connector.
            name (:class:`str`):
                Required. Name of a Serverless VPC
                Access connector to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.vpcaccess_v1.types.Connector:
                Definition of a Serverless VPC Access
                connector.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = vpc_access.GetConnectorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_connector,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_connectors(
        self,
        request: Union[vpc_access.ListConnectorsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConnectorsAsyncPager:
        r"""Lists Serverless VPC Access connectors.

        .. code-block::

            from google.cloud import vpcaccess_v1

            def sample_list_connectors():
                # Create a client
                client = vpcaccess_v1.VpcAccessServiceClient()

                # Initialize request argument(s)
                request = vpcaccess_v1.ListConnectorsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_connectors(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vpcaccess_v1.types.ListConnectorsRequest, dict]):
                The request object. Request for listing Serverless VPC
                Access connectors in a location.
            parent (:class:`str`):
                Required. The project and location
                from which the routes should be listed.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.vpcaccess_v1.services.vpc_access_service.pagers.ListConnectorsAsyncPager:
                Response for listing Serverless VPC
                Access connectors.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = vpc_access.ListConnectorsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_connectors,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListConnectorsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_connector(
        self,
        request: Union[vpc_access.DeleteConnectorRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a Serverless VPC Access connector. Returns NOT_FOUND if
        the resource does not exist.


        .. code-block::

            from google.cloud import vpcaccess_v1

            def sample_delete_connector():
                # Create a client
                client = vpcaccess_v1.VpcAccessServiceClient()

                # Initialize request argument(s)
                request = vpcaccess_v1.DeleteConnectorRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_connector(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vpcaccess_v1.types.DeleteConnectorRequest, dict]):
                The request object. Request for deleting a Serverless
                VPC Access connector.
            name (:class:`str`):
                Required. Name of a Serverless VPC
                Access connector to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = vpc_access.DeleteConnectorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_connector,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=vpc_access.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-vpc-access",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("VpcAccessServiceAsyncClient",)
