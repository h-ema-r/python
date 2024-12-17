# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.32
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1ContainerResizePolicy(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'resource_name': 'str',
        'restart_policy': 'str'
    }

    attribute_map = {
        'resource_name': 'resourceName',
        'restart_policy': 'restartPolicy'
    }

    def __init__(self, resource_name=None, restart_policy=None, local_vars_configuration=None):  # noqa: E501
        """V1ContainerResizePolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resource_name = None
        self._restart_policy = None
        self.discriminator = None

        self.resource_name = resource_name
        self.restart_policy = restart_policy

    @property
    def resource_name(self):
        """Gets the resource_name of this V1ContainerResizePolicy.  # noqa: E501

        Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.  # noqa: E501

        :return: The resource_name of this V1ContainerResizePolicy.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this V1ContainerResizePolicy.

        Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.  # noqa: E501

        :param resource_name: The resource_name of this V1ContainerResizePolicy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_name is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_name`, must not be `None`")  # noqa: E501

        self._resource_name = resource_name

    @property
    def restart_policy(self):
        """Gets the restart_policy of this V1ContainerResizePolicy.  # noqa: E501

        Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.  # noqa: E501

        :return: The restart_policy of this V1ContainerResizePolicy.  # noqa: E501
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this V1ContainerResizePolicy.

        Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.  # noqa: E501

        :param restart_policy: The restart_policy of this V1ContainerResizePolicy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and restart_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `restart_policy`, must not be `None`")  # noqa: E501

        self._restart_policy = restart_policy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ContainerResizePolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ContainerResizePolicy):
            return True

        return self.to_dict() != other.to_dict()
